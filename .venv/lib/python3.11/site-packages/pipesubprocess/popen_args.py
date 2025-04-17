import subprocess

from .constants import PIPE

class PopenArgs:
    '''
    The possible arguments are Popen arguments except for
    stdin/stdout and name. name is set to popen object.
    This parameter is used to call pipesubcommand.Popen.
    stdin and stdout are ignored when piped to another process.
    '''
    def __init__(self, args, bufsize=-1, executable=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), name=None):
        self._name = name
        self.stderr = stderr
        self.popen_kwargs = {
            'args': args,
            'bufsize': bufsize,
            'executable': executable,
            'preexec_fn': preexec_fn,
            'close_fds': close_fds,
            'shell': shell,
            'cwd': cwd,
            'env': env,
            'startupinfo': startupinfo,
            'creationflags': creationflags,
            'restore_signals': restore_signals,
            'start_new_session': start_new_session,
            'pass_fds': pass_fds,
        }
        if self.stderr == subprocess.PIPE:
            raise NotImplementedError("PIPE cannot be set for stderr.")

    @property
    def args(self):
        return self.popen_kwargs['args']

    @property
    def name(self):
        if self._name:
            return self._name
        elif isinstance(self.args, str):
            return self.args
        else:
            return self.args[0]

    @property
    def fullname(self):
        if self._name:
            return self._name
        elif isinstance(self.args, str):
            return self.args
        else:
            return ' '.join(self.args)

    def __repr__(self):
        return f"<PipeArgs args='{' '.join(self.args)}'>"

    def __str__(self):
        from pprint import pformat
        return pformat({'name': self.name,
                        'stderr': self.stderr,
                        'popen_kwargs': self.popen_kwargs}, indent=4)


