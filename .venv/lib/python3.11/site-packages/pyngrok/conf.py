__copyright__ = "Copyright (c) 2018-2025 Alex Laird"
__license__ = "MIT"

import os
import platform
from typing import Callable, Optional

from pyngrok.installer import get_ngrok_bin
from pyngrok.log import NgrokLog

DEFAULT_CONFIG_PATH: Optional[str] = None

system = platform.system().lower()
if system == "darwin":
    _config_rel_path = os.path.join("Library", "Application Support", "ngrok")
elif system in ["windows", "cygwin"]:
    _config_rel_path = os.path.join("AppData", "Local", "ngrok")
else:
    _config_rel_path = os.path.join(".config", "ngrok")
DEFAULT_NGROK_DIR = os.path.join(os.path.expanduser("~"), _config_rel_path)
DEFAULT_NGROK_CONFIG_PATH = os.path.join(DEFAULT_NGROK_DIR, "ngrok.yml")
DEFAULT_NGROK_PATH = os.path.join(DEFAULT_NGROK_DIR, get_ngrok_bin())


class PyngrokConfig:
    """
    An object containing ``pyngrok``'s configuration for interacting with the ``ngrok`` binary. All values are
    optional when it is instantiated, and default values will be used for parameters not passed.

    Use :func:`~pyngrok.conf.get_default` and :func:`~pyngrok.conf.set_default` to interact with the default
    ``pyngrok_config``, or pass another instance of this object as the ``pyngrok_config`` keyword arg to most
    methods in the :mod:`~pyngrok.ngrok` module to override the default.

    .. code-block:: python

        from pyngrok import conf, ngrok

        # Here we update the entire default config
        pyngrok_config = conf.PyngrokConfig(ngrok_path="/usr/local/bin/ngrok")
        conf.set_default(pyngrok_config)

        # Here we update just one variable in the default config
        conf.get_default().ngrok_path = "/usr/local/bin/ngrok"

        # Here we leave the default config as-is and pass an override
        pyngrok_config = conf.PyngrokConfig(ngrok_path="/usr/local/bin/ngrok")
        ngrok.connect(pyngrok_config=pyngrok_config)
    """

    def __init__(self,
                 ngrok_path: Optional[str] = None,
                 config_path: Optional[str] = None,
                 auth_token: Optional[str] = os.environ.get("NGROK_AUTHTOKEN"),
                 region: Optional[str] = None,
                 monitor_thread: bool = True,
                 log_event_callback: Optional[Callable[[NgrokLog], None]] = None,
                 startup_timeout: int = 15,
                 max_logs: int = 100,
                 request_timeout: float = 4,
                 start_new_session: bool = False,
                 ngrok_version: str = "v3",
                 api_key: Optional[str] = os.environ.get("NGROK_API_KEY"),
                 config_version: str = "2") -> None:
        #: The path to the ``ngrok`` binary, defaults to being placed in the same directory as
        #: `ngrok's configs <https://ngrok.com/docs/agent/config/v2>`_.
        self.ngrok_path: str = DEFAULT_NGROK_PATH if ngrok_path is None else ngrok_path
        #: The path to the ``ngrok`` config, defaults to ``None`` and ``ngrok`` manages it.
        self.config_path: Optional[str] = DEFAULT_CONFIG_PATH if config_path is None else config_path
        #: A ``ngrok`` authtoken to pass to commands (overrides what is in the config). If a value is not passed, will
        #: attempt to use the environment variable ``NGROK_AUTHTOKEN`` if it is set.
        self.auth_token: Optional[str] = auth_token
        #: The region in which ``ngrok`` should start.
        self.region: Optional[str] = region
        #: Whether ``ngrok`` should continue to be monitored (for logs, etc.) after startup is complete.
        self.monitor_thread: bool = monitor_thread
        #: A callback that will be invoked each time ``ngrok`` emits a log. The function should take
        #: one argument of type :py:class:`str`. ``monitor_thread`` must be set to ``True`` or the function will
        #: stop being called after ``ngrok`` finishes starting.
        self.log_event_callback: Optional[Callable[[NgrokLog], None]] = log_event_callback
        #: The max timeout, in seconds, to wait for ``ngrok`` to start.
        self.startup_timeout: int = startup_timeout
        #: The max number of logs to store in :class:`~pyngrok.process.NgrokProcess`'s ``logs`` variable.
        self.max_logs: int = max_logs
        #: The max timeout, in seconds, when making requests to ``ngrok``'s API.
        self.request_timeout: float = request_timeout
        #: Passed to :py:class:`subprocess.Popen` when launching ``ngrok``. (Python 3 and POSIX only).
        self.start_new_session: bool = start_new_session
        #: The major version of ``ngrok`` installed.
        self.ngrok_version: str = ngrok_version
        #: A ``ngrok`` API key.
        self.api_key: Optional[str] = api_key
        #: The ``ngrok`` config version.
        self.config_version = config_version


_default_pyngrok_config: PyngrokConfig = PyngrokConfig()


def get_default() -> PyngrokConfig:
    """
    Get the default config to be used with methods in the :mod:`~pyngrok.ngrok` module. To override the
    default individually, the ``pyngrok_config`` keyword arg can also be passed to most of these methods,
    or set a new default config with :func:`~pyngrok.conf.set_default`.

    :return: The default ``pyngrok_config``.
    """
    if _default_pyngrok_config is None:
        set_default(PyngrokConfig())

    return _default_pyngrok_config


def set_default(pyngrok_config: PyngrokConfig) -> None:
    """
    Set a new default config to be used with methods in the :mod:`~pyngrok.ngrok` module. To override the
    default individually, the ``pyngrok_config`` keyword arg can also be passed to most of these methods.

    :param pyngrok_config: The new ``pyngrok_config`` to be used by default.
    """
    global _default_pyngrok_config

    _default_pyngrok_config = pyngrok_config


def get_config_path(pyngrok_config: PyngrokConfig) -> str:
    """
    Return the ``config_path`` if set on the given ``pyngrok_configg``, otherwise return ``ngrok``'s default path.

    :param pyngrok_config: The ``pyngrok`` configuration to first check for a ``config_path``.
    :return: The path to the config file.
    """
    if pyngrok_config.config_path is not None:
        return pyngrok_config.config_path
    else:
        return DEFAULT_NGROK_CONFIG_PATH
