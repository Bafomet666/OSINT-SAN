import logging
from shlex import split as shlex_split

from .constants import DEVNULL, PIPE, STDOUT
from .exceptions import CalledProcessError
from .popen import Popen
from .popen_args import PopenArgs

logger = logging.getLogger(__name__)

def _get_args_list(cmdlist, shlex=True):
    '''
    Get a list of splitted argument list
    '''
    args_list = []
    for cmd in cmdlist:
        #logging.debug(f'cmd={cmd}, type={type(cmd)}')
        if isinstance(cmd, str):
            if shlex:
                logging.debug('... is shlexed str')
                args_list.append(shlex_split(cmd))
            else:
                #logging.debug('... is str')
                args_list.append(cmd)
        elif isinstance(cmd, list):
            #logging.debug('... is list')
            args_list.append(cmd)
        else:
            raise ValueError(f'{args} is not list or str')

    return args_list


def run(*cmdlist, shlex=True, stdin=None, input=None, stdout=None, stderr=None, capture_output=True, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=True, env=None, universal_newlines=None):
    '''
    args_list: List of string/list.
    '''
    if not isinstance(cmdlist, list) and not isinstance(cmdlist, tuple):
        raise ValueError(f'{cmdlist} must be list')

    if capture_output and (stdout or stderr):
        raise ValueError('Both capture_output and stdout/stderr are specified.')
    elif capture_output:
        stdout = PIPE
        stderr = PIPE
    if input and stdin:
        raise ValueError('Both input and stdin are specified.')
    elif input:
        stdin = PIPE

    if len(cmdlist) == 1:
        args_list = _get_args_list(cmdlist[0], shlex=shlex)
    else:
        args_list = _get_args_list(cmdlist, shlex=shlex)
    popen_args_list = [PopenArgs(args, shell=shell, cwd=cwd, env=env) for args in args_list]
    logger.debug(popen_args_list)

    p = Popen(popen_args_list, stdin=stdin, stdout=stdout, stderr=stderr, errors=errors, encoding=encoding, text=text, universal_newlines=universal_newlines)

    outs, errs = p.communicate(input=input, timeout=timeout)

    result = CompletedProcess(popen_args_list, p.poll(), stdout=outs, stderr=errs)
    if check:
        result.check_returncodes()
    return result

class CompletedProcess:
    def __init__(self, popen_args_list, returncodes, stdout=None, stderr=None):
        self.popen_args_list = popen_args_list
        self.returncodes = returncodes
        self.stdout = stdout
        self.stderr = stderr

    def check_returncodes(self):
        if self.returncodes is None:
            need_raise = True
        elif any(self.returncodes):
            need_raise = True

        if need_raise:
            raise CalledProcessError(self.popen_args_list, self.returncodes, stdout=self.stdout, stderr=self.stderr)


    def __repr__(self):
        cmdlist = [pa.name for pa in self.popen_args_list]

        if self.stdout:
            stdout_repr = "%d lines" % self.stdout.count("\n")
        else:
            stdout_repr = "None"

        if self.stderr:
            stderr_repr = "%d lines" % self.stderr.count("\n")
        else:
            stderr_repr = "None"

        return f"CompletedProcess(cmdlist={cmdlist}, returncodes={self.returncodes}, stdout={stdout_repr}, stderr={stderr_repr})"
