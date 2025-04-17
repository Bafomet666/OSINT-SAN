# import re
import os
import logging

from typing import (
    Dict,
    List,
    Any,
    Optional,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class TldInfo:
    def __init__(
        self,
        zzDict: Dict[str, Any],
        verbose: bool = False,
    ) -> None:
        self.verbose = verbose
        if verbose:
            logging.basicConfig(level="DEBUG")

        # a reference to the external ZZ database of all TLD info
        self.zzDictRef = zzDict

        # do we want to store the processed data or will be do all on the fly
        self.withStore: bool = True

        # the database of processed tld entries (if withStoe is True)
        self.tldRegexDb: Dict[str, Dict[str, Any]] = {}

    def _initOne(
        self,
        tld: str,
        override: bool = False,
    ) -> None:
        # meta domains start with _: examples _centralnic and _donuts
        if tld[0] == "_":  # skip meta domain patterns , these are not domains just handles we reuse
            return

        if override is False:
            if tld in self.tldRegexDb:
                return

        what = self.flattenMasterTldEntry(tld, override=override)
        if self.withStore:
            self.tldRegexDb[tld] = what

        # test if the string is identical after idna conversion
        d = tld.split(".")
        j = [k.encode("idna").decode() or k for k in d]

        tld2 = ".".join(j)
        if tld == tld2:
            return

        if self.withStore:
            self.tldRegexDb[tld2] = what

    def _cleanupResultDict(self, resultDict: Dict[str, Any]) -> Dict[str, Any]:
        # we dont want to propagate the extend data
        if "extend" in resultDict:
            del resultDict["extend"]
        if "_extend" in resultDict:
            del resultDict["_extend"]

        # we inhert all except extend or _extend
        cleanResultDict: Dict[str, Any] = {}
        for key, val in resultDict.items():
            cleanResultDict[key] = val

        return cleanResultDict

    # public

    def flattenMasterTldEntry(
        self,
        tldString: str,
        override: bool = False,
    ) -> Dict[str, Any]:
        tldDict = self.zzDictRef[tldString]
        hasExtend: Optional[str] = tldDict.get("extend") or tldDict.get("_extend")
        if hasExtend:
            eDict = self.flattenMasterTldEntry(hasExtend)  # call recursive
            tmpDict = eDict.copy()
            # entries in the current tldDict take precedence
            # over the origin data of the extend entry
            tmpDict.update(tldDict)
            return self._cleanupResultDict(tmpDict)

        return self._cleanupResultDict(tldDict)

    def init(self) -> None:
        # build the database of all tld
        for tld in self.zzDictRef.keys():
            self._initOne(tld, override=False)

    def filterTldToSupportedPattern(
        self,
        domain: str,
        dList: List[str],
        verbose: bool = False,
    ) -> Optional[str]:
        # we have max 2 levels so first check if the last 2 are in our list
        tld = f"{dList[-2]}.{dList[-1]}"
        if tld in self.zzDictRef:
            return tld

        # if not check if the last item  we have
        tld = f"{dList[-1]}"
        if tld in self.zzDictRef:
            return tld

        return None

    def mergeExternalDictWithRegex(
        self,
        aDict: Optional[Dict[str, Any]] = None,
    ) -> None:
        if aDict is None:
            return

        if len(aDict) == 0:
            return

        # merge in ZZ, this extends ZZ with new tld's and overrides existing tld's
        for tld in aDict.keys():
            self.zzDictRef[tld] = aDict[tld]

        # reprocess the regexes we newly defined or overrode
        override = True
        for tld in aDict.keys():
            self._initOne(tld, override)

    def validTlds(self) -> List[str]:
        return sorted(self.tldRegexDb.keys())

    def TLD_RE(self) -> Dict[str, Dict[str, Any]]:
        # this returns the currenly prepared list of all tlds ane theyr compiled regexes
        return self.tldRegexDb
