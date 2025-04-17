import logging
import subprocess
import shlex
import signal

logger = logging.getLogger(__name__)

class PipeSubprocessError(subprocess.SubprocessError):
    '''
    It's a base exception class of pipesubprocess
    '''
    def __init__(self, popen_args, stdout=None, stderr=None):
        self.popen_args = popen_args
        self.stdout = stdout
        self.stderr = stderr

    @property
    def output(self):
        return self.stdout


class TimeoutExpired(PipeSubprocessError):
    '''
    Raised when timeout expired for run(), communicate(), or wait()
    '''
    def __init__(self, popen_args, timeout, stdout=None, stderr=None):
        super().__init__(popen_args, stdout=stdout, stderr=stderr)
        self.timeout = timeout

    def __repr__(self):
        cmds_string = [pa.name for pa in self.popen_args].join(' | ')
        return f'Commands: "{cmds_string}" timed out after {self.timeout} seconds.'


class CalledProcessError(PipeSubprocessError):
    '''
    Raised when run(check=True) is executed and exit with non-zero return code.
    '''
    def __init__(self, popen_args, returncodes, stdout=None, stderr=None):
        super().__init__(popen_args, stdout=stdout, stderr=stderr)
        self.returncodes = returncodes

    def __repr__(self):
        ret_str = None
        for i in range(len(self.returncodes)):
            ret = self.returncodes[i]
            pa = self.popen_args[i]
            if ret and ret < 0:
                try:
                    s = f"'{pa.name}' died with {signal.Signals(-ret)}."
                except ValueError:
                    s = f"'{pa.name}' died with signal {-ret}."
            else:
                s = f"'{pa.name}' exited with {ret}"
            if ret_str:
                ret_str += f' {s}'
            else:
                ret_str = s
        return ret_str
