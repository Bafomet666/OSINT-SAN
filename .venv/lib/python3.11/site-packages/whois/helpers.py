import os
import logging

from typing import (
    Optional,
    List,
    Dict,
    Any,
)

from .exceptions import WhoisQuotaExceeded

from .tldInfo import TldInfo
from .version import VERSION
from .tldDb.tld_regexpr import ZZ
from .context.parameterContext import ParameterContext

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def filterTldToSupportedPattern(
    domain: str,
    dList: List[str],
    verbose: bool = False,
) -> Optional[str]:
    global tldInfo
    return tldInfo.filterTldToSupportedPattern(domain, dList, verbose=verbose)


def mergeExternalDictWithRegex(
    aDict: Optional[Dict[str, Any]] = None,
) -> None:
    global tldInfo
    if aDict is None:
        return
    if len(aDict) == 0:
        return

    tldInfo.mergeExternalDictWithRegex(aDict)


def validTlds() -> List[str]:
    global tldInfo
    return tldInfo.validTlds()


def get_TLD_RE() -> Dict[str, Any]:
    global tldInfo
    return tldInfo.TLD_RE()


def getVersion() -> str:
    return VERSION


def getTestHint(tldString: str) -> Optional[str]:
    k: str = "_test"
    if tldString in ZZ and k in ZZ[tldString] and ZZ[tldString][k]:
        return str(ZZ[tldString][k])

    return None


def cleanupWhoisResponse(
    whoisStr: str,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
) -> str:
    tmp2: List[str] = []

    if pc is None:
        pc = ParameterContext(
            verbose=verbose,
            withRedacted=withRedacted,
            with_cleanup_results=with_cleanup_results,
        )

    tmp: List[str] = whoisStr.split("\n")
    for line in tmp:
        # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
        if "quota exceeded" in line.lower():
            raise WhoisQuotaExceeded(whoisStr)

        if pc.with_cleanup_results is True and line.startswith("%"):  # only remove if requested
            continue

        if pc.withRedacted is False:
            if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                continue

        if "Please query the RDDS service of the Registrar of Record" in line:  # these lines contibute nothing so ignore
            continue

        if line.startswith("Terms of Use:"):  # these lines contibute nothing so ignore
            continue

        tmp2.append(line.strip("\r").rstrip())

    return "\n".join(tmp2)


VERBOSE: bool = False

# Here we focre load on import the processing of the ZZ database
tldInfo = TldInfo(ZZ, VERBOSE)
tldInfo.init()  # must run on import
