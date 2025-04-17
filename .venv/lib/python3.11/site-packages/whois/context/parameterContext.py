#! /usr/bin/env python3

import os
import logging
import json

from typing import (
    List,
    Dict,
    Any,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

ParamsStringJson: str = """
{
  "ignore_returncode": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "if the whois command fails with code 1 still process the data returned as normal."
  },
  "force": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "Don't use cache."
  },
  "verbose": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "print relevant information on steps taken to standard error"
  },
  "with_cleanup_results": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "cleanup lines starting with % and REDACTED FOR PRIVACY"
  },
  "internationalized": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "if true convert with internationalizedDomainNameToPunyCode()."
  },
  "include_raw_whois_text": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "if reqested the full response is also returned."
  },
  "return_raw_text_for_unsupported_tld": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": ""
  },
  "parse_partial_response": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "try to parse partial response when cmd timed out (stdbuf should be in PATH for best results)"
  },
  "simplistic": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "when simplistic is true we return null for most exceptions and dont pass info why we have no data."
  },
  "withRedacted": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "show redacted output default no redacted data is shown"
  },
  "cmd": {
    "type": "str",
    "optional": true,
    "default": "whois",
    "help": "specify the path to the cli whois you want to use."
  },
  "cache_file": {
    "type": "str",
    "optional": true,
    "default": null,
    "help": "Use file to store cache not only memory."
  },
  "server": {
    "type": "str",
    "optional": true,
    "default": null,
    "help": "use this whois server for making this query: Linux/Mac: 'whois -h <server> <domain>' Windows: 'whois.exe <domain> <server>'"
  },
  "cache_age": {
    "type": "int",
    "optional": true,
    "default": 172800,
    "help": "Cache expiration time for given domain in seconds 60*60*48 (48 hours)"
  },
  "slow_down": {
    "type": "int",
    "optional": true,
    "default": 0,
    "help": "Time [s] it will wait after you query WHOIS database."
  },
  "timeout": {
    "type": "float",
    "optional": true,
    "default": 30.0,
    "help": "timeout in seconds for the whois command to return a result."
  },
  "tryInstallMissingWhoisOnWindows": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "allow auto install of sysinternals whois on windows if no whois found"
  },
  "shortResponseLen": {
    "type": "int",
    "optional": true,
    "default": 5,
    "help": "The number of lines we consider a short response."
  },
  "withPublicSuffix": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "if lib 'tld' is installed add tld info based on get_tld(); fake the tld if needed"
  },
  "extractServers": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "try to extract the whois servers from the whois output (uses --verbose)"
  },
  "stripHttpStatus": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "strip https://icann.org/epp# from status response"
  },
  "noIgnoreWww": {
    "type": "bool",
    "default": false,
    "optional": true,
    "help": "if set to true we skip the strip www action"
  }
}
"""


class ParameterContext:
    params: Dict[str, Any]
    value: Dict[str, Any]

    KT: Dict[str, Any] = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
    }

    def loadDefaults(self) -> List[str]:
        mandatory: List[str] = []
        for i, k in self.params.items():
            if "default" in k:
                self.value[i] = k["default"]
            else:
                mandatory.append(i)  # params with no default become mandatory
                self.value[i] = None
        return mandatory

    def addArgs(
        self,
        mandatory: List[str],
        **kwargs: Dict[str, Any],
    ) -> None:
        for name, value in kwargs.items():
            if name not in self.params:
                msg = f"ignore parameter '{name}':you specified a parameter we do not currently know"
                raise TypeError(msg)

            t = self.params[name].get("type")
            if t is None:
                msg = f"unknown type: {t} for {name}"
                raise TypeError(msg)

            # we have a type and we still exist
            if value is not None:
                if not isinstance(value, self.KT[t]):
                    msg = f"unknown type: {t} for {name}, {value}"
                    raise TypeError(msg)

                self.value[name] = value
                if name in mandatory:
                    del mandatory[mandatory.index(name)]

    def validateAllMandatoryNowKnown(
        self,
        mandatory: List[str],
    ) -> None:
        if len(mandatory) != 0:
            msg = f"missing mandatory parametrs: {sorted(mandatory)}"
            raise ValueError(msg)

    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        self.params = json.loads(ParamsStringJson)
        self.value = {}

        mandatory: List[str] = self.loadDefaults()
        self.addArgs(mandatory, **kwargs)
        self.validateAllMandatoryNowKnown(mandatory)

    def __getattr__(self, name: str) -> Any:
        if name in ["params", "value"]:
            return self.name
        return self.get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ["params", "value"]:
            object.__setattr__(self, name, value)
        else:
            self.set(name, value)

    def get(self, name: str) -> Any:
        if name in self.value:
            return self.value[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def set(self, name: str, value: Any) -> None:
        if name not in self.params:
            msg = f"ignore parameter '{name}':you specified a parameter we do not currently know"
            raise TypeError(msg)

        if name in self.params:
            t = self.params[name].get("type")
            if t is None:
                msg = f"unknown type: {t} for {name}"
                raise TypeError(msg)

            if value is not None:
                if not isinstance(value, self.KT[t]):
                    msg = f"unknown type: {t} for {name}, {value}"
                    raise TypeError(msg)
                self.value[name] = value
            # leave the default


if __name__ == "__main__":
    domain: str = "haha.ha"
    pc = ParameterContext(domain=domain)
    print(pc.value)
