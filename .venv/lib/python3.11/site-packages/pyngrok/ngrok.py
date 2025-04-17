#!/usr/bin/env python

__copyright__ = "Copyright (c) 2018-2025 Alex Laird"
__license__ = "MIT"

import json
import logging
import os
import socket
import sys
import uuid
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from pyngrok import __version__, conf, installer, process
from pyngrok.conf import PyngrokConfig
from pyngrok.exception import PyngrokError, PyngrokNgrokHTTPError, PyngrokNgrokURLError, PyngrokSecurityError
from pyngrok.installer import get_default_config
from pyngrok.process import NgrokProcess

logger = logging.getLogger(__name__)


class NgrokTunnel:
    """
    An object containing information about a ``ngrok`` tunnel.
    """

    def __init__(self,
                 data: Dict[str, Any],
                 pyngrok_config: PyngrokConfig,
                 api_url: Optional[str]) -> None:
        #: The original tunnel data.
        self.data: Dict[str, Any] = data
        #: The ``pyngrok`` configuration to use when interacting with the ``ngrok``.
        self.pyngrok_config: PyngrokConfig = pyngrok_config
        #: The API URL for the ``ngrok`` web interface.
        self.api_url: Optional[str] = api_url

        #: The ID of the tunnel.
        self.id: Optional[str] = data.get("ID", None)
        #: The name of the tunnel.
        self.name: Optional[str] = data.get("name")
        #: The protocol of the tunnel.
        self.proto: Optional[str] = data.get("proto")
        #: The tunnel URI, a relative path that can be used to make requests to the ``ngrok`` web interface.
        self.uri: Optional[str] = data.get("uri")
        #: The public ``ngrok`` URL.
        self.public_url: Optional[str] = data.get("public_url")
        #: The config for the tunnel.
        self.config: Dict[str, Any] = data.get("config", {})
        #: Metrics for `the tunnel <https://ngrok.com/docs/agent/api/#list-tunnels>`_.
        self.metrics: Dict[str, Any] = data.get("metrics", {})

    def __repr__(self) -> str:
        return f"<NgrokTunnel: \"{self.public_url}\" -> \"{self.config['addr']}\">" if self.config.get(
            "addr", None) else "<pending Tunnel>"

    def __str__(self) -> str:  # pragma: no cover
        return f"NgrokTunnel: \"{self.public_url}\" -> \"{self.config['addr']}\"" if self.config.get(
            "addr", None) else "<pending Tunnel>"

    def refresh_metrics(self) -> None:
        """
        Get the latest metrics for the tunnel and update the ``metrics`` variable.

        :raises: :class:`~pyngrok.exception.PyngrokError`: When the API does not return ``metrics``.
        """
        logger.info(f"Refreshing metrics for tunnel: {self.public_url}")

        data = api_request(f"{self.api_url}{self.uri}", method="GET",
                           timeout=self.pyngrok_config.request_timeout)

        if "metrics" not in data:
            raise PyngrokError("The ngrok API did not return \"metrics\" in the response")

        self.data["metrics"] = data["metrics"]
        self.metrics = self.data["metrics"]


_current_tunnels: Dict[str, NgrokTunnel] = {}


def install_ngrok(pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Download, install, and initialize ``ngrok`` for the given config. If ``ngrok`` and its default
    config is already installed, calling this method will do nothing.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    if not os.path.exists(pyngrok_config.ngrok_path):
        installer.install_ngrok(pyngrok_config.ngrok_path, ngrok_version=pyngrok_config.ngrok_version)

    config_path = conf.get_config_path(pyngrok_config)

    # Install the config to the requested path
    if not os.path.exists(config_path):
        installer.install_default_config(config_path, ngrok_version=pyngrok_config.ngrok_version)


def set_auth_token(token: str,
                   pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Set the ``ngrok`` auth token in the config file, enabling authenticated features (for instance,
    opening multiple tunnels concurrently, custom domains, etc.).

    If ``ngrok`` is not installed at :class:`~pyngrok.conf.PyngrokConfig`'s ``ngrok_path``, calling this method
    will first download and install ``ngrok``.

    :param token: The auth token to set.
    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    process.set_auth_token(pyngrok_config, token)


def set_api_key(key: str,
                pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Set the ``ngrok`` API key in the config file, enabling more features (for instance, labeled tunnels).

    If ``ngrok`` is not installed at :class:`~pyngrok.conf.PyngrokConfig`'s ``ngrok_path``, calling this method
    will first download and install ``ngrok``.

    :param key: The API key to set.
    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    process.set_api_key(pyngrok_config, key)


def get_ngrok_process(pyngrok_config: Optional[PyngrokConfig] = None) -> NgrokProcess:
    """
    Get the current ``ngrok`` process for the given config's ``ngrok_path``.

    If ``ngrok`` is not installed at :class:`~pyngrok.conf.PyngrokConfig`'s ``ngrok_path``, calling this method
    will first download and install ``ngrok``.

    If ``ngrok`` is not running, calling this method will first start a process with
    :class:`~pyngrok.conf.PyngrokConfig`.

    Use :func:`~pyngrok.process.is_process_running` to check if a process is running without also implicitly
    installing and starting it.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    :return: The ``ngrok`` process.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    return process.get_process(pyngrok_config)


def _apply_edge_to_tunnel(tunnel: NgrokTunnel,
                          pyngrok_config: PyngrokConfig) -> None:
    if not tunnel.public_url and pyngrok_config.api_key and tunnel.id:
        tunnel_response = api_request(f"https://api.ngrok.com/tunnels/{tunnel.id}", method="GET",
                                      auth=pyngrok_config.api_key)
        if "labels" not in tunnel_response or "edge" not in tunnel_response["labels"]:
            raise PyngrokError(
                f"Tunnel {tunnel.data['ID']} does not have \"labels\", use a Tunnel configured on an Edge.")

        edge = tunnel_response["labels"]["edge"]
        if edge.startswith("edghts_"):
            edges_prefix = "https"
        elif edge.startswith("edgtcp"):
            edges_prefix = "tcp"
        elif edge.startswith("edgtls"):
            edges_prefix = "tls"
        else:
            raise PyngrokError(f"Unknown Edge prefix: {edge}.")

        edge_response = api_request(f"https://api.ngrok.com/edges/{edges_prefix}/{edge}", method="GET",
                                    auth=pyngrok_config.api_key)

        if "hostports" not in edge_response or len(edge_response["hostports"]) < 1:
            raise PyngrokError(
                f"No Endpoint is attached to your Edge {edge}, login to the ngrok "
                f"dashboard to attach an Endpoint to your Edge first.")

        tunnel.public_url = f"{edges_prefix}://{edge_response['hostports'][0]}"
        tunnel.proto = edges_prefix


def _interpolate_tunnel_definition(pyngrok_config: PyngrokConfig,
                                   options: Dict[str, Any],
                                   addr: Optional[str] = None,
                                   proto: Optional[Union[str, int]] = None,
                                   name: Optional[str] = None) -> None:
    config_path = conf.get_config_path(pyngrok_config)

    if os.path.exists(config_path):
        config = installer.get_ngrok_config(config_path, ngrok_version=pyngrok_config.ngrok_version)
    else:
        config = get_default_config(pyngrok_config.ngrok_version, pyngrok_config.config_version)

    tunnel_definitions = config.get("tunnels", {})
    # If a "pyngrok-default" tunnel definition exists in the ngrok config, use that
    if not name and "pyngrok-default" in tunnel_definitions:
        name = "pyngrok-default"

    # Use a tunnel definition for the given name, if it exists
    if name and name in tunnel_definitions:
        tunnel_definition = tunnel_definitions[name]

        if "labels" in tunnel_definition and "bind_tls" in options:
            raise PyngrokError("\"bind_tls\" cannot be set when \"labels\" is also on the tunnel definition.")

        addr = tunnel_definition.get("addr") if not addr else addr
        proto = tunnel_definition.get("proto") if not proto else proto
        # Use the tunnel definition as the base, but override with any passed in options
        tunnel_definition.update(options)
        options.clear()
        options.update(tunnel_definition)

    if "labels" in options and not pyngrok_config.api_key:
        raise PyngrokError(
            "\"PyngrokConfig.api_key\" must be set when \"labels\" is on the tunnel definition.")

    addr = str(addr) if addr else "80"
    # Only apply a default proto label if "labels" isn't defined
    if not proto and "labels" not in options:
        proto = "http"

    if not name:
        if not addr.startswith("file://"):
            name = f"{proto}-{addr}-{uuid.uuid4()}"
        else:
            name = f"{proto}-file-{uuid.uuid4()}"

    options.update({
        "name": name,
        "addr": addr,
        "proto": proto
    })


def _upgrade_legacy_params(pyngrok_config: PyngrokConfig,
                           options: Dict[str, Any]) -> None:
    if pyngrok_config.ngrok_version == "v3":
        if "bind_tls" in options:
            if options.get("bind_tls") is True or options.get("bind_tls") == "true":
                options["schemes"] = ["https"]
            elif not options.get("bind_tls") is not False or options.get("bind_tls") == "false":
                options["schemes"] = ["http"]
            else:
                options["schemes"] = ["http", "https"]

            options.pop("bind_tls")

        if "auth" in options:
            auth = options.get("auth")
            if isinstance(auth, list):
                options["basic_auth"] = auth
            else:
                options["basic_auth"] = [auth]

            options.pop("auth")


def connect(addr: Optional[str] = None,
            proto: Optional[Union[str, int]] = None,
            name: Optional[str] = None,
            pyngrok_config: Optional[PyngrokConfig] = None,
            **options: Any) -> NgrokTunnel:
    """
    Establish a new ``ngrok`` tunnel for the given protocol to the given port, returning an object representing
    the connected tunnel.

    If a `tunnel definition in ngrok's config file
    <https://ngrok.com/docs/agent/config/v2/#tunnel-configurations>`_ matches the given
    ``name``, it will be loaded and used to start the tunnel. When ``name`` is ``None`` and a "pyngrok-default" tunnel
    definition exists in ``ngrok``'s config, it will be loaded and used. Any ``kwargs`` passed as ``options`` will
    override properties from the loaded tunnel definition.

    If ``ngrok`` is not installed at :class:`~pyngrok.conf.PyngrokConfig`'s ``ngrok_path``, calling this method
    will first download and install ``ngrok``.

    ``pyngrok`` is compatible with ``ngrok`` v2 and v3, but by default it will install v3. To install v2 instead,
    set ``ngrok_version`` to "v2" in :class:`~pyngrok.conf.PyngrokConfig`:

    If ``ngrok`` is not running, calling this method will first start a process with
    :class:`~pyngrok.conf.PyngrokConfig`.

    .. note::

        ``ngrok`` v2's default behavior for ``http`` when no additional properties are passed is to open *two* tunnels,
        one ``http`` and one ``https``. This method will return a reference to the ``http`` tunnel in this case. If
        only a single tunnel is needed, pass ``bind_tls=True`` and a reference to the ``https`` tunnel will be
        returned.

    :param addr: The local port to which the tunnel will forward traffic, or a
        `local directory or network address <https://ngrok.com/docs/http/#file-serving>`_,
        defaults to "80".
    :param proto: A valid `tunnel protocol
        <https://ngrok.com/docs/agent/config/v2/#tunnel-configurations>`_, defaults to "http".
    :param name: A friendly name for the tunnel, or the name of a `ngrok tunnel definition
        <https://ngrok.com/docs/agent/config/v2/#tunnel-configurations>`_ defined in ``ngrok``'s config file.
    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    :param options: Remaining ``kwargs`` are passed as `configuration for the ngrok
        tunnel <https://ngrok.com/docs/agent/config/v2/#tunnel-configurations>`_.
    :return: The created ``ngrok`` tunnel.
    :raises: :class:`~pyngrok.exception.PyngrokError`: When the tunnel definition is invalid, or the response does
        not contain ``public_url``.
    """
    if "labels" in options:
        raise PyngrokError("\"labels\" cannot be passed to connect(), define a tunnel definition in the config file.")

    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    _interpolate_tunnel_definition(pyngrok_config, options, addr, proto, name)

    proto = options.get("proto")
    name = options.get("name")

    # Remove proto when "labels" is defined
    if "labels" in options:
        options.pop("proto")

    _upgrade_legacy_params(pyngrok_config, options)

    logger.info(f"Opening tunnel named: {name}")

    api_url = get_ngrok_process(pyngrok_config).api_url

    logger.debug(f"Creating tunnel with options: {options}")

    tunnel = NgrokTunnel(api_request(f"{api_url}/api/tunnels", method="POST", data=options,
                                     timeout=pyngrok_config.request_timeout),
                         pyngrok_config, api_url)

    if pyngrok_config.ngrok_version == "v2" and proto == "http" and options.get("bind_tls", "both") == "both":
        tunnel = NgrokTunnel(api_request(f"{api_url}{tunnel.uri}%20%28http%29", method="GET",
                                         timeout=pyngrok_config.request_timeout),
                             pyngrok_config, api_url)

    _apply_edge_to_tunnel(tunnel, pyngrok_config)

    if tunnel.public_url is None:
        raise PyngrokError(
            f"\"public_url\" was not populated for tunnel {tunnel}, but is required for pyngrok to function.")

    _current_tunnels[tunnel.public_url] = tunnel

    return tunnel


def disconnect(public_url: str,
               pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Disconnect the ``ngrok`` tunnel for the given URL, if open.

    :param public_url: The public URL of the tunnel to disconnect.
    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    # If ngrok is not running, there are no tunnels to disconnect
    if not process.is_process_running(pyngrok_config.ngrok_path):
        return

    api_url = get_ngrok_process(pyngrok_config).api_url

    if public_url not in _current_tunnels:
        get_tunnels(pyngrok_config)

        # One more check, if the given URL is still not in the list of tunnels, it is not active
        if public_url not in _current_tunnels:
            return

    tunnel = _current_tunnels[public_url]

    logger.info(f"Disconnecting tunnel: {tunnel.public_url}")

    api_request(f"{api_url}{tunnel.uri}", method="DELETE",
                timeout=pyngrok_config.request_timeout)

    _current_tunnels.pop(public_url, None)


def get_tunnels(pyngrok_config: Optional[PyngrokConfig] = None) -> List[NgrokTunnel]:
    """
    Get a list of active ``ngrok`` tunnels for the given config's ``ngrok_path``.

    If ``ngrok`` is not installed at :class:`~pyngrok.conf.PyngrokConfig`'s ``ngrok_path``, calling this method
    will first download and install ``ngrok``.

    If ``ngrok`` is not running, calling this method will first start a process with
    :class:`~pyngrok.conf.PyngrokConfig`.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    :return: The active ``ngrok`` tunnels.
    :raises: :class:`~pyngrok.exception.PyngrokError`: When the response was invalid or does not
        contain ``public_url``.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    api_url = get_ngrok_process(pyngrok_config).api_url

    _current_tunnels.clear()
    for tunnel in api_request(f"{api_url}/api/tunnels", method="GET",
                              timeout=pyngrok_config.request_timeout)["tunnels"]:
        ngrok_tunnel = NgrokTunnel(tunnel, pyngrok_config, api_url)
        _apply_edge_to_tunnel(ngrok_tunnel, pyngrok_config)

        if ngrok_tunnel.public_url is None:
            raise PyngrokError(
                f"\"public_url\" was not populated for tunnel {ngrok_tunnel}, "
                f"but is required for pyngrok to function.")

        _current_tunnels[ngrok_tunnel.public_url] = ngrok_tunnel

    return list(_current_tunnels.values())


def kill(pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Terminate the ``ngrok`` processes, if running, for the given config's ``ngrok_path``. This method will not
    block, it will just issue a kill request.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    process.kill_process(pyngrok_config.ngrok_path)

    _current_tunnels.clear()


def get_version(pyngrok_config: Optional[PyngrokConfig] = None) -> Tuple[str, str]:
    """
    Get a tuple with the ``ngrok`` and ``pyngrok`` versions.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    :return: A tuple of ``(ngrok_version, pyngrok_version)``.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    ngrok_version = process.capture_run_process(pyngrok_config.ngrok_path, ["--version"]).split("version ")[1]

    return ngrok_version, __version__


def update(pyngrok_config: Optional[PyngrokConfig] = None) -> str:
    """
    Update ``ngrok`` for the given config's ``ngrok_path``, if an update is available.

    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    :return: The result from the ``ngrok`` update.
    """
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    return process.capture_run_process(pyngrok_config.ngrok_path, ["update"])


def api_request(url: str,
                method: str = "GET",
                data: Optional[Dict[str, Any]] = None,
                params: Optional[Dict[str, Any]] = None,
                timeout: float = 4,
                auth: Optional[str] = None) -> Dict[str, Any]:
    """
    Invoke an API request to the given URL, returning JSON data from the response.

    One use for this method is making requests to ``ngrok`` tunnels:

    .. code-block:: python

        from pyngrok import ngrok

        public_url = ngrok.connect()
        response = ngrok.api_request(f"{public_url}/some-route",
                                     method="POST", data={"foo": "bar"})

    Another is making requests to the ``ngrok`` API itself:

    .. code-block:: python

        from pyngrok import ngrok

        api_url = ngrok.get_ngrok_process().api_url
        response = ngrok.api_request(f"{api_url}/api/requests/http",
                                     params={"tunnel_name": "foo"})

    :param url: The request URL.
    :param method: The HTTP method.
    :param data: The request body.
    :param params: The URL parameters.
    :param timeout: The request timeout, in seconds.
    :param auth: Set as Bearer for an Authorization header.
    :return: The response from the request.
    :raises: :class:`~pyngrok.exception.PyngrokSecurityError`: When the ``url`` is not supported.
    :raises: :class:`~pyngrok.exception.PyngrokNgrokHTTPError`: When the request returns an error response.
    :raises: :class:`~pyngrok.exception.PyngrokNgrokURLError`: When the request times out.
    """
    if params is None:
        params = {}

    if not url.lower().startswith("http"):
        raise PyngrokSecurityError(f"URL must start with \"http\": {url}")

    encoded_data = json.dumps(data).encode("utf-8") if data else None

    if params:
        url += f"?{urlencode([(x, params[x]) for x in params])}"

    request = Request(url, method=method.upper())
    request.add_header("Content-Type", "application/json")
    if auth:
        request.add_header("Ngrok-Version", "2")
        request.add_header("Authorization", f"Bearer {auth}")

    logger.debug(f"Making {method} request to {url} with data: {data}")

    try:
        response = urlopen(request, encoded_data, timeout)
        response_data = response.read().decode("utf-8")

        status_code = response.getcode()
        logger.debug(f"Response {status_code}: {response_data.strip()}")

        if str(status_code)[0] != "2":
            raise PyngrokNgrokHTTPError(f"ngrok client API returned {status_code}: {response_data}", url,
                                        status_code, None, request.headers, response_data)
        elif status_code == HTTPStatus.NO_CONTENT:
            return {}

        return json.loads(response_data)  # type: ignore
    except socket.timeout:
        raise PyngrokNgrokURLError("ngrok client exception, URLError: timed out", "timed out")
    except HTTPError as e:
        response_data = e.read().decode("utf-8")

        status_code = e.getcode()
        logger.debug(f"Response {status_code}: {response_data.strip()}")

        raise PyngrokNgrokHTTPError(f"ngrok client exception, API returned {status_code}: {response_data}",
                                    e.url,
                                    status_code, e.reason, e.headers, response_data)
    except URLError as e:
        raise PyngrokNgrokURLError(f"ngrok client exception, URLError: {e.reason}", e.reason)


def run(args: Optional[List[str]] = None,
        pyngrok_config: Optional[PyngrokConfig] = None) -> None:
    """
    Ensure ``ngrok`` is installed at the default path, then call :func:`~pyngrok.process.run_process`.

    This method is meant for interacting with ``ngrok`` from the command line and is not necessarily
    compatible with non-blocking API methods. For that, use :mod:`~pyngrok.ngrok`'s interface methods (like
    :func:`~pyngrok.ngrok.connect`), or use :func:`~pyngrok.process.get_process`.

    :param args: Arguments to be passed to the ``ngrok`` process.
    :param pyngrok_config: A ``pyngrok`` configuration to use when interacting with the ``ngrok`` binary,
        overriding :func:`~pyngrok.conf.get_default()`.
    """
    if args is None:
        args = []
    if pyngrok_config is None:
        pyngrok_config = conf.get_default()

    install_ngrok(pyngrok_config)

    process.run_process(pyngrok_config.ngrok_path, args)


def main() -> None:
    """
    Entry point for the package's ``console_scripts``. This initializes a call from the command
    line and invokes :func:`~pyngrok.ngrok.run`.

    This method is meant for interacting with ``ngrok`` from the command line and is not necessarily
    compatible with non-blocking API methods. For that, use :mod:`~pyngrok.ngrok`'s interface methods (like
    :func:`~pyngrok.ngrok.connect`), or use :func:`~pyngrok.process.get_process`.
    """
    run(sys.argv[1:])

    if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1].lstrip("-").lstrip("-") == "help":
        print(f"\nPYNGROK VERSION:\n   {__version__}")
    elif len(sys.argv) == 2 and sys.argv[1].lstrip("-").lstrip("-") in ["v", "version"]:
        print(f"pyngrok version {__version__}")


if __name__ == "__main__":
    main()
