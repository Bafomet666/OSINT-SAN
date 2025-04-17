# pylint: disable=duplicate-code
"""
Module providing all public accessible functions and data for the whoisdomain package

## optional modules supported:

- if the tld library is installed you can use the `withPublicSuffix:bool` option

All public data is vizible via the __all__ List
"""

import sys
import os
import logging

from functools import wraps

from typing import (
    cast,
    Optional,
    List,
    Dict,
    Tuple,
    Any,
    Callable,
)

from .exceptions import (
    UnknownTld,
    FailedParsingWhoisOutput,
    UnknownDateFormat,
    WhoisCommandFailed,
    WhoisPrivateRegistry,
    WhoisQuotaExceeded,
    WhoisCommandTimeout,
)

from .tldInfo import TldInfo
from .version import VERSION
from .processWhoisDomainRequest import ProcessWhoisDomainRequest
from .doWhoisCommand import setMyCache
from .domain import Domain
from .strings.noneStrings import NoneStrings, NoneStringsAdd
from .strings.quotaStrings import QuotaStrings, QuotaStringsAdd
from .tldDb.tld_regexpr import ZZ
from .context.dataContext import DataContext
from .context.parameterContext import ParameterContext
from .cache.simpleCacheBase import SimpleCacheBase
from .cache.simpleCacheWithFile import SimpleCacheWithFile
from .cache.dummyCache import DummyCache
from .cache.dbmCache import DBMCache
from .whoisParser import WhoisParser
from .whoisCliInterface import WhoisCliInterface


from .helpers import (
    filterTldToSupportedPattern,
    mergeExternalDictWithRegex,
    validTlds,
    get_TLD_RE,
    getVersion,
    getTestHint,
    cleanupWhoisResponse,
)

from .lastWhois import (
    get_last_raw_whois_data,
    initLastWhois,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

HAS_REDIS = False
try:
    import redis

    HAS_REDIS = True
except ImportError as e:
    _ = e

if HAS_REDIS:
    from .cache.redisCache import RedisCache

WHOISDOMAIN: str = ""
if os.getenv("WHOISDOMAIN"):
    WHOISDOMAIN = str(os.getenv("WHOISDOMAIN"))

WD = WHOISDOMAIN.upper().split(":")

SIMPLISTIC = False
if "SIMPLISTIC" in WD:
    SIMPLISTIC = True

TLD_LIB_PRESENT: bool = False
try:
    import tld as libTld

    TLD_LIB_PRESENT = True
except ImportError as e:
    _ = e  # ignore any error

__all__ = [
    # from exceptions
    "UnknownTld",
    "FailedParsingWhoisOutput",
    "UnknownDateFormat",
    "WhoisCommandFailed",
    "WhoisPrivateRegistry",
    "WhoisQuotaExceeded",
    "WhoisCommandTimeout",
    # from helpers
    "validTlds",
    "mergeExternalDictWithRegex",
    "filterTldToSupportedPattern",
    "get_TLD_RE",
    "getVersion",
    "getTestHint",
    "cleanupWhoisResponse",  # we will drop this most likely
    # from version
    "VERSION",
    # from parameterContext
    "ParameterContext",
    # from this file
    "query",
    "q2",
    # from lastWhois
    "get_last_raw_whois_data",
    # from doWhoisCommand
    "setMyCache",  # to build your own caching interface
    # from doParse
    "NoneStrings",
    "NoneStringsAdd",
    "QuotaStrings",
    "QuotaStringsAdd",
    # from Cache
    "SimpleCacheBase",
    "SimpleCacheWithFile",
    "DummyCache",
    "DBMCache",
    "RedisCache",
]


def _result2dict(func: Any) -> Any:
    @wraps(func)
    def _inner(*args: str, **kw: Any) -> Dict[str, Any]:
        r = func(*args, **kw)
        return r and vars(r) or {}

    return _inner


def q2(
    domain: str,
    pc: ParameterContext,
) -> Optional[Domain]:
    initLastWhois()

    dc = DataContext(
        domain=domain,
        hasLibTld=TLD_LIB_PRESENT,
    )

    dom = Domain(
        pc=pc,
        dc=dc,
    )

    parser = WhoisParser(
        pc=pc,
        dc=dc,
    )

    wci = WhoisCliInterface(
        pc=pc,
        dc=dc,
    )

    pwdr = ProcessWhoisDomainRequest(
        pc=pc,
        dc=dc,
        dom=dom,
        wci=wci,
        parser=parser,
    )

    result = pwdr.processRequest()
    return result


def query(
    domain: str,
    force: bool = False,
    cache_file: Optional[str] = None,
    cache_age: int = 60 * 60 * 48,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    internationalized: bool = False,
    include_raw_whois_text: bool = False,
    return_raw_text_for_unsupported_tld: bool = False,
    timeout: Optional[float] = None,
    parse_partial_response: bool = False,
    cmd: str = "whois",
    simplistic: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
    tryInstallMissingWhoisOnWindows: bool = False,
    shortResponseLen: int = 5,
    withPublicSuffix: bool = False,
    extractServers: bool = False,
    stripHttpStatus: bool = False,
    noIgnoreWww: bool = False,
    # if you use pc as argument all above params (except domain are ignored)
) -> Optional[Domain]:
    # see documentation about paramaters in parameterContext.py

    assert isinstance(domain, str), Exception("`domain` - must be <str>")

    if pc is None:
        pc = ParameterContext(
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
            with_cleanup_results=with_cleanup_results,
            internationalized=internationalized,
            include_raw_whois_text=include_raw_whois_text,
            return_raw_text_for_unsupported_tld=return_raw_text_for_unsupported_tld,
            timeout=timeout,
            parse_partial_response=parse_partial_response,
            cmd=cmd,
            simplistic=simplistic,
            withRedacted=withRedacted,
            withPublicSuffix=withPublicSuffix,
            shortResponseLen=shortResponseLen,
            tryInstallMissingWhoisOnWindows=tryInstallMissingWhoisOnWindows,
            extractServers=extractServers,
            stripHttpStatus=stripHttpStatus,
            noIgnoreWww=noIgnoreWww,
        )

    msg = f"{pc}"
    log.debug(msg)

    return q2(domain=domain, pc=pc)


# Add get function to support return result in dictionary form
get = _result2dict(query)
