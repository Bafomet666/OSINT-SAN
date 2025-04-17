# import sys
import os
import logging

from typing import (
    Optional,
    List,
    Tuple,
)

from .exceptions import UnknownTld

from .context.dataContext import DataContext
from .context.parameterContext import ParameterContext

from .helpers import filterTldToSupportedPattern
from .helpers import get_TLD_RE

from .doWhoisCommand import doWhoisAndReturnString
from .whoisParser import WhoisParser
from .domain import Domain
from .lastWhois import updateLastWhois
from .whoisCliInterface import WhoisCliInterface

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

TLD_LIB_PRESENT: bool = False
try:
    import tld as libTld

    TLD_LIB_PRESENT = True
except ImportError as ee:
    _ = ee  # ignore any error


class ProcessWhoisDomainRequest:
    def __init__(
        self,
        pc: ParameterContext,
        dc: DataContext,
        dom: Domain,
        wci: WhoisCliInterface,
        parser: WhoisParser,
    ) -> None:
        self.pc = pc
        self.dc = dc
        self.dom: Optional[Domain] = dom
        self.wci = wci
        self.parser = parser
        if self.pc.verbose:
            logging.basicConfig(level="DEBUG")

    def _analyzeDomainStringAndValidate(
        self,
    ) -> None:
        def _internationalizedDomainNameToPunyCode(d: List[str]) -> List[str]:
            return [k.encode("idna").decode() or k for k in d]

        # Prep the domain ================
        self.dc.domain = self.dc.domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.
        self.dc.dList = self.dc.domain.split(".")

        # test with: www.dublin.airport.aero see make withPublicSuffix
        if self.dc.hasLibTld and self.pc.withPublicSuffix:
            res = libTld.get_tld(
                self.dc.domain,
                fail_silently=True,
                fix_protocol=True,
            )
            if res:
                self.dc.publicSuffixStr = str(res)
                self.dc.hasPublicSuffix = True
                msg = f"publicSuffixStr: {self.dc.publicSuffixStr}"
                log.debug(msg)

        if len(self.dc.dList) == 0:
            self.dc.tldString = None
            self.dc.dList = []
            return

        if self.dc.dList[0] == "www":
            if self.pc.noIgnoreWww is False:
                self.dc.dList = self.dc.dList[1:]

        if len(self.dc.dList) == 0:
            self.dc.tldString = None
            self.dc.dList = []
            return

        # we currently do not support raw tld's so we cannot lookup 'com' for example
        if len(self.dc.dList) == 1:
            self.dc.tldString = None
            self.dc.dList = []
            return

        # Is it a supported domain =======
        self.dc.tldString = filterTldToSupportedPattern(
            self.dc.domain,
            self.dc.dList,
            self.pc.verbose,
        )

        if self.dc.tldString is None:
            # if not fail
            tld = f"{self.dc.dList[-1]}"
            a = f"The TLD {tld} is currently not supported by this package."
            b = "Use validTlds() to see what toplevel domains are supported."
            msg = f"{a} {b}"
            raise UnknownTld(msg)

        # Internationalized domains: Idna translate
        if self.pc.internationalized:
            self.dc.dList = _internationalizedDomainNameToPunyCode(self.dc.dList)

    def _makeMessageForUnsupportedTld(
        self,
    ) -> Optional[str]:
        if self.pc.return_raw_text_for_unsupported_tld:
            return None

        a = f"The TLD {self.dc.tldString} is currently not supported by this package."
        b = "Use validTlds() to see what toplevel domains are supported."
        msg = f"{a} {b}"
        return msg

    def _doUnsupportedTldAnyway(
        self,
    ) -> None:
        if self.dc.dList is not None:
            # we will not hunt for possible valid first level domains as we have no actual feedback
            self.pc.include_raw_whois_text = True

            # now use the cache interface to fetch the whois str from cli whois
            self.dc.whoisStr = doWhoisAndReturnString(
                pc=self.pc,
                dc=self.dc,
                wci=self.wci,
            )

            # we will only return minimal data
            self.dc.data = {
                "tld": self.dc.tldString,
                "domain_name": [],
            }

            z: str = ".".join(self.dc.dList)
            self.dc.data["domain_name"] = [z]  # note the fields are default all array, except tld
            self.pc.return_raw_text_for_unsupported_tld = True

    def _doOneLookup(
        self,
    ) -> Tuple[Optional[Domain], bool]:
        msg = f"### lookup: tldString: {self.dc.tldString}; dList: {self.dc.dList}"
        log.debug(msg)

        if self.dc.dList is None:  # mainly to please mypy
            self.dom = None
            return self.dom, True

        try:
            # now use the cache interface to fetch the whois str from cli whois
            self.dc.whoisStr = doWhoisAndReturnString(
                pc=self.pc,
                dc=self.dc,
                wci=self.wci,
            )
        except Exception as e:
            if self.pc.simplistic is False:
                raise e

            self.dc.exeptionStr = f"{e}"
            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return self.dom, True

        self.dc.whoisStr = str(self.dc.whoisStr)

        msg = f"Raw: {self.dc.whoisStr}"
        log.debug(msg)

        self.dc.rawWhoisStr = self.dc.whoisStr  # keep the original whois string for reference before we clean
        updateLastWhois(
            dList=self.dc.dList,
            whoisStr=self.dc.rawWhoisStr,
            pc=self.pc,
        )

        self.parser.init()
        # init also calls cleanup on the text string whois cli response
        msg = f"Clean: {self.dc.whoisStr}"
        log.debug(msg)

        assert self.dom is not None
        data, finished = self.parser.parse(
            dom=self.dom,
        )

        if finished:
            self.dom = data

        return data, finished

    def _prepRequest(self) -> bool:
        try:
            self._analyzeDomainStringAndValidate()  # may raise UnknownTld
        except UnknownTld as e:
            if self.pc.simplistic is False:
                raise e

            self.dc.exeptionStr = "UnknownTld"

            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return True

        if self.dc.tldString is None:
            self.dom = None
            return True

        # force mypy to process ok
        self.dc.tldString = str(self.dc.tldString)
        if self.dc.dList == []:
            self.dom = None
            return True

        # =================================================
        myKeys: List[str] = []
        for item in get_TLD_RE():
            myKeys.append(item)

        if self.dc.tldString not in myKeys:
            msg = self._makeMessageForUnsupportedTld()
            if msg is None:
                self._doUnsupportedTldAnyway()

                assert self.dom is not None
                self.dom.init(
                    pc=self.pc,
                    dc=self.dc,
                )
                return True

            if self.pc.simplistic is False:
                raise UnknownTld(msg)

            self.dc.exeptionStr = msg  # was: self.dc.exeptionStr = "UnknownTld"
            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return True

        # find my compiled info under key: tld and use {} as the default
        # self.dc.thisTld = get_TLD_RE().get(self.dc.tldString, {})
        self.parser.getThisTld(self.dc.tldString)

        if self.parser.verifyPrivateRegistry():  # may raise WhoisPrivateRegistry
            msg = "This tld has either no whois server or responds only with minimal information"
            self.dc.exeptionStr = msg
            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return True

        self.parser.doServerHintsForThisTld()
        self.parser.doSlowdownHintForThisTld()

        return False

    def init(self) -> None:
        pass

    def processRequest(self) -> Optional[Domain]:
        finished = self._prepRequest()
        if finished is True:
            return self.dom

        # if the tld is a multi level we should not move further down than the tld itself
        # we currently allow progressive lookups until we find something:
        # so xxx.yyy.zzz will try both xxx.yyy.zzz and yyy.zzz
        # but if the tld is yyy.zzz we should only try xxx.yyy.zzz

        # self.dc.tldString is now a supported <tld> and never changes
        # self.dc.dList is the cleaned up domain query in list form:
        # so ".".join(self.dc.dList) would be like: aaa.<tld> or perhaps aaa.bbb.<tld>
        # and may change if we find no data in cli whois

        tldLevel: List[str] = []
        if self.dc.hasPublicSuffix:
            tldLevel = str(self.dc.publicSuffixStr).split(".")
        else:
            tldLevel = str(self.dc.tldString).split(".")

        while len(self.dc.dList) > len(tldLevel):
            log.debug(f"{self.dc.dList}")
            z, finished = self._doOneLookup()

            if finished:
                self.dom = z
                return self.dom

            self.dc.dList = self.dc.dList[1:]  # strip one element from the front and try again

        self.dom = None
        return self.dom
