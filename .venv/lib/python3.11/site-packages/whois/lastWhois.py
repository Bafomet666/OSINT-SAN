"""
This module keeps track of the original whois string for the last query request

it should be rewritten to use a static class or singleton
it is re-initialized on each new request

public access is only needed fow: get_last_raw_whois_data()

"""
import os
import logging

from typing import (
    List,
    Dict,
    Any,
)

from .context.parameterContext import ParameterContext

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

LastWhois: Dict[str, Any] = {}


def updateLastWhois(
    dList: List[str],
    whoisStr: str,
    pc: ParameterContext,
) -> None:
    global LastWhois
    LastWhois["Try"].append(
        {
            "Domain": ".".join(dList),
            "rawData": whoisStr,
            "server": pc.server,
        }
    )


def initLastWhois() -> None:
    global LastWhois
    LastWhois = {}
    LastWhois["Try"] = []  # init on start of query


def get_last_raw_whois_data() -> Dict[str, Any]:
    global LastWhois
    return LastWhois
