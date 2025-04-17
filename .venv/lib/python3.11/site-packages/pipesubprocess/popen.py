#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import copy
import logging
import os
import subprocess
import threading
import time

from .constants import PIPE, STDOUT, DEVNULL
from .exceptions import TimeoutExpired

logger = logging.getLogger(__name__)

class Popen:
    '''
    It wraps multiple subprocess.popen and provides I/F like subprocess.Popen.
    '''
    polling_interval = 0.1
    '''
    Parameters
    ----------
    popen_args_list
        The list of pipechildren.PopenArgs
    stderr
        Specify One of pipechildren.DEVNULL, pipechildren.STDOUT, or file-like object
    '''
    def __init__(self, popen_args_list, stdin=None, stdout=None, stderr=None, universal_newlines=None, encoding=None, errors=None, text=None, _debug_communicate_io=False):
        self.text = universal_newlines or encoding or errors or text
        self.encoding = encoding
        self.popen_args_list = popen_args_list
        self.processes = []
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.stderr_write_end = None
        self.outs = None
        self.errs = None
        self.pids = []
        self.returncodes = []

        self._debug_communicate_io = _debug_communicate_io

        self._communicate_called = False
        self._workers = {
            "stderr_drainer": None,
            "close_stderr_write_end_worker": None,
            "waiter": None,
            "stdin_worker": None,
            "stdout_worker": None,
            "stderr_worker": None
        }
        self._stop_workers = False


        '''
        Call popen with each popen_args and connect stdout -> stdin
        between subprocesses.
        '''
        # previous stdout goes into current stdin
        prev_out = stdin
        for i in range(len(self.popen_args_list)):
            pa = self.popen_args_list[i]
            if i == len(self.popen_args_list) - 1:
                # Last
                _stdout = stdout
            else:
                _stdout = subprocess.PIPE

            _stderr = pa.stderr if pa.stderr else stderr

            p = subprocess.Popen(stdout=_stdout,
                                 stdin=prev_out,
                                 stderr=_stderr,
                                 text=self.text,
                                 encoding=self.encoding,
                                 **pa.popen_kwargs)

            setattr(p, "name", pa.name)
            logger.info(f"Popening({pa.fullname})")
            if i > 0:
                """
                piped stdout/stdin is connected between subprocesses and used in
                forked sub-processes. We should release them not to prevent pipe close.
                """
                self.processes[-1].stdout.close()
                self.processes[-1].stdout = None

            self.processes.append(p)
            self.pids.append(p.pid)
            prev_out = p.stdout

        #self._start_pipe_closer()

        if stdin is PIPE:
            self.stdin = self.processes[0].stdin
        else:
            self.stdin = None

        if stdout is PIPE:
            self.stdout = self.processes[-1].stdout
        else:
            self.stdout = None

        if stderr is PIPE:
            logger.debug("stderr is PIPE")
            if len(self.processes) == 1:
                self.stderr = self.processes[0].stderr
            else:
                r, w = os.pipe()
                if self.text:
                    self.stderr = os.fdopen(r, 'r')
                    self.stderr_write_end = os.fdopen(w, 'w')
                else:
                    self.stderr = os.fdopen(r, 'rb')
                    self.stderr_write_end = os.fdopen(w, 'wb')
                self._start_stderr_drainer()
        else:
            self.stderr = None
            self.stderr_write_end = stderr
            if stderr:
                self._start_stderr_drainer()

    @staticmethod
    def _work_text_drainer(_self, name, reader, data_writer):
        '''
        Generic thread reader to read data from <reader> and write
        data to callback data_writer(data).

        NOTE: It is STATIC method.
        Called like self._work_text_drainer(self)

        data_writer() gets binary data as 1st argument and needs to return
        False if writer is no longer avaialb.e
        '''
        logger.debug(f"_work_text_drainer {name} started")
        while (not _self._stop_workers):
            line = reader.readline()
            if not line:
                break
            if _self._debug_communicate_io:
                logger.debug(f"{name} -> {line}")
            if not data_writer(line):
                break
        logger.debug(f"_work_text_drainer {name} finished.")


    @staticmethod
    def _work_binary_drainer(_self, name, reader, data_writer):
        '''
        Generic thread reader to read data from <reader> and write
        data to callback data_writer(data).

        NOTE: It is STATIC method.
        Called like self._work_binary_drainer(self)

        data_writer() gets binary data as 1st argument and need to return
        False if writer is no longer avaialb.e
        '''
        logger.debug(f"_work_binary_drainer {name} started")
        while (not _self._stop_workers):
            data = reader.read(4096)
            if not data:
                break
            if _self._debug_communicate_io:
                logger.debug(f"{name} -> {data}")
            if not data_writer(data):
                logger.debug(f"{name} -> EOF")
                break
        logger.debug(f"_work_binary_drainer {name} finished.")


    def _start_stderr_drainer(self):
        '''
        drain stderr from all sub-processes and gather to one piped stderr
        '''

        stderr_drainer = []

        def stderr_write_end_writer(data):
            if self.stderr_write_end.closed:
                return False
            else:
                self.stderr_write_end.write(data)
                return True

        for p in self.processes:
            name=f"{p.name}_stderr_drainer"

            if self.text:
                drainer = lambda: self._work_text_drainer(self,
                                                          name,
                                                          p.stderr,
                                                          stderr_write_end_writer)
            else:
                drainer = lambda: self._work_binary_drainer(self,
                                                            name,
                                                            p.stderr,
                                                            stderr_write_end_writer)

            t = threading.Thread(name=name, target=drainer)
            t.start()
            stderr_drainer.append(t)

        self._workers["stderr_drainer"] = stderr_drainer

        if self.stderr:
            # We need close worker otherwise reader cannot finish reading.
            def work_close_stderr_write_end():
                logger.debug(f"work_close_stderr_write_end started")
                drainers = self._workers["stderr_drainer"]
                while not self._stop_workers:
                    alive = False
                    for t in drainers:
                        if t.is_alive():
                            alive = True
                            break
                    if not alive:
                        break
                logger.debug(f"work_close_stderr_write_end finished")
                self.stderr_write_end.close()

            close_stderr_write_end_worker = threading.Thread(
                target=work_close_stderr_write_end,
                name=name)
            close_stderr_write_end_worker.start()
            self._workers["close_stderr_write_end_worker"] = close_stderr_write_end_worker

    def __enter__(self):
        return self

    def __exit__(self):
        # To support "with pipechildren.Popen() as p:"
        self.wait()

    def poll(self):
        '''
        Check if child process has terminated. Set and return returncode list attribute. Otherwise, returns None.

        Returns
        ----------
        returncode
            list of returncode of subprocesses.
        '''
        self.returncodes = [p.poll() for p in self.processes]
        if None in self.returncodes:
            return None
        return self.returncodes

    def wait(self, timeout=None):
        '''
        Wait for child processes to terminate. Set and return returncode attribute.

        If the process does not terminate after timeout seconds,
        raise a TimeoutExpired exception.
        It is safe to catch this exception and retry the wait.

        Returns
        ----------
        returncodes
            list of returncodes of subprocesses.
        '''
        logger.debug("wait started")
        def work_wait(name, p, timeout):
            logger.debug(f"waiter {name} started")
            ret = None
            try:
                ret = p.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                logger.debug(f"waiter {name} timed out.")
            else:
                logger.debug(f"waiter {name} finished")
            return ret

        waiter = []
        for p in self.processes:
            name = f"{p.name}_waiter"
            t = threading.Thread(
                target=lambda: work_wait(name, p, timeout),
                name=name)

            t.start()
            waiter.append(t)
        self._workers["waiter"] = waiter
        for t in waiter:
            t.join()
        self._workers["waiter"] = None

        returncodes = self.poll()
        if returncodes is None:
            raise TimeoutExpired(self.popen_args_list, timeout, stdout=self.outs, stderr=self.errs)
        logger.debug("wait finished")
        return returncodes

    def _time_left_sec(self, timeout_at):
        if timeout_at:
            time_left_sec = (timeout_at - datetime.now()).total_seconds()
            if time_left_sec < 0:
                return 0
            else:
                return time_left_sec
        return None

    def get_timeout_at(self, timeout):
        return datetime.now() + timedelta(seconds=timeout)

    def _start_communicate_pipes(self, input=input):
        '''
        Start threads below. It's called only once when communicate is called first time.
        - Thread1: write <input> to stdin if stdin is PIPE and <input> is given.
        - Thread2: read stdout to outs if stdout is PIPE
        - Thread3: read stderr to errs if stderr is PIPE
        '''
        logger.debug("_start_communicate_pipes called")

        def work_stdin(input=None):
            '''
            Thread worker to write <input> to stdin
            '''
            logger.debug("stdin_worker started")
            start = 0
            step = 4096
            end = start + step
            while not self._stop_workers and not self.stdin.closed:
                if len(input) > end:
                    if self._debug_communicate_io:
                        logger.debug(f"->stdin {input[start:end]}")
                    self.stdin.write(input[start:end])
                else:
                    if self._debug_communicate_io:
                        logger.debug(f"->stdin {input[start:]}")
                    self.stdin.write(input[start:])
                    break
                start += step
                end += step
            self.stdin.close()
            logger.debug("stdin_worker finished")

        def add_to_outs_writer(data):
            '''
            Writer used by stdout drainer thread
            '''
            self.outs += data
            return True

        def add_to_errs_writer(data):
            '''
            Writer used by stderr drainer thread
            '''
            self.errs += data
            return True

        if input and self.stdin:
            stdin_worker = threading.Thread(
                target=lambda: work_stdin(input=input),
                name="stdin_worker")
            stdin_worker.start()
            self._workers["stdin_worker"] = stdin_worker
        elif self.stdin:
            self.stdin.close()

        if self.stdout:
            if self.text:
                self.outs = ''
                drainer = lambda: self._work_text_drainer(self,
                                                          'stdout_drainer',
                                                          self.stdout,
                                                          add_to_outs_writer)
            else:
                self.outs = b''
                drainer = lambda: self._work_binary_drainer(self,
                                                            'stdout_drainer',
                                                            self.stdout,
                                                            add_to_outs_writer)
            stdout_worker = threading.Thread(
                target=drainer,
                name="stdout_worker")
            stdout_worker.start()
            self._workers["stdout_worker"] = stdout_worker

        if self.stderr:
            if self.text:
                self.errs = ''
                drainer = lambda: self._work_text_drainer(self,
                                                          'stderr_drainer',
                                                          self.stderr,
                                                          add_to_errs_writer)
            else:
                self.errs = b''
                drainer = lambda: self._work_binary_drainer(self,
                                                            'stderr_drainer',
                                                            self.stderr,
                                                            add_to_errs_writer)
            stderr_worker = threading.Thread(
                target=drainer,
                name="stderr_worker")
            stderr_worker.start()
            self._workers["stderr_worker"] = stderr_worker

    def communicate(self, input=None, timeout=None):
        '''
        Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.
        Wait for process to terminate. The optional input argument should be data to be sent
        to the upper stream child process, or None, if no data should be sent to the child.
        If streams were opened in text mode, input must be a string. Otherwise, it must be bytes.

        Returns
        ----------
        stdout_data
            stdout of down most process
        stderr_data
            stderr of whole process if pipechildren.PIPE is specified.
        The data will be strings if streams were opened in text mode; otherwise, bytes.
        '''
        logger.debug("communicate called")
        if len(self.processes) == 1:
            # In this case, just call subprocess.communicate
            self.outs, self.errs = self.processes[0].communicate(input=input, timeout=timeout)
            return self.outs, self.errs

        firsttime = True
        if self._communicate_called:
            firsttime = False
        self._communicate_called = True

        if firsttime:
            self._start_communicate_pipes(input=input)

        timeout_at = None
        if timeout:
            timeout_at = self.get_timeout_at(timeout)

        self.wait(timeout=timeout)

        # If self.wait() timedout, it raises to caller out of thie method.
        # If we reach here, all processes have finished.
        # Close stdin first then wait for the end of output workers.
        if self.stdin:
            self.stdin.close()

        timedout = False
        if self._workers["stdin_worker"]:
            timeout_left = self._time_left_sec(timeout_at)
            self._workers["stdin_worker"].join(timeout=timeout_left)
            timedout = self._workers["stdin_worker"].is_alive()

        if self._workers["stdout_worker"] and not timedout:
            timeout_left = self._time_left_sec(timeout_at)
            self._workers["stdout_worker"].join(timeout=timeout_left)
            timedout = self._workers["stdout_worker"].is_alive()

        if self._workers["stderr_worker"] and not timedout:
            timeout_left = self._time_left_sec(timeout_at)
            self._workers["stderr_worker"].join(timeout=timeout_left)
            if not timedout:
                timedout = self._workers["stderr_worker"].is_alive()

        if timedout:
            raise TimeoutExpired(self.popen_args_list, timeout, stdout=self.outs, stderr=self.errs)

        # Guard all workers from running just in case.
        self._stop_workers = True

        # Close up pipes
        if self.stdout:
            self.stdout.close()

        if self.stderr:
            self.stderr.close()

        for p in self.processes:
            if p.stderr:
                p.stderr.close()

        return self.outs, self.errs

    def kill(self, *args):
        if args and isinstance(args[0], list):
            for i in args[0]:
                self.processes[i].kill()
        else:
            for p in self.processes:
                p.kill()

    def terminate(self, *args):
        if args and isinstance(args[0], list):
            for i in args[0]:
                self.processes[i].terminate()
        else:
            for p in self.processes:
                p.terminate()

    def send_signal(self, signal, *args):
        if args and isinstance(args[0], list):
            for i in args[0]:
                self.processes[i].send_signal(signal)
        else:
            for p in self.processes:
                p.send_signal(signal)

