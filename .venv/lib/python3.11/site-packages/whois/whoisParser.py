#! /usr/bin/env python3
# pylint: disable=duplicate-code

from typing import (
    Any,
    Dict,
    Optional,
    List,
    # Union,
    Tuple,
    # cast,
)

import re
import os
import logging

# import sys

from .exceptions import (
    FailedParsingWhoisOutput,
    WhoisQuotaExceeded,
    WhoisPrivateRegistry,
)

from .domain import Domain
from .strings.noneStrings import NoneStrings
from .strings.quotaStrings import QuotaStrings
from .strings.ignoreStrings import IgnoreStrings

from .context.parameterContext import ParameterContext
from .context.dataContext import DataContext
from .helpers import get_TLD_RE


log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class WhoisParser:
    def __init__(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        self.pc = pc
        self.dc = dc
        self.dom: Optional[Domain] = None
        self.resultDict: Dict[str, Any] = {}
        if self.pc.verbose:
            logging.basicConfig(level="DEBUG")

    def _doExtractPattensIanaFromWhoisString(
        self,
    ) -> None:
        # now handle the actual format for this whois response
        iana = {
            "domain_name": r"domain:\s?([^\n]+)",
            "registrar": r"organisation:\s?([^\n]+)",
            "creation_date": r"created:\s?([^\n]+)",
        }

        for key, val in iana.items():
            result = re.findall(val, str(self.dc.whoisStr))
            if not result:
                continue

            self.resultDict[key] = result
            msg = f"parsing iana data only for tld: {self.dc.tldString}, {result}"
            log.debug(msg)

    def _doExtractPattensFromWhoisString_old(
        self,
    ) -> None:
        empty = [""]  # Historical: we use 'empty string' as default, not None

        for key, compiledRe in self.dc.thisTld.items():
            if key.startswith("_"):
                # skip meta element like: _server or _privateRegistry
                continue

            self.resultDict[key] = empty  # set a default
            if compiledRe:
                # here we apply the regex patterns
                self.resultDict[key] = compiledRe.findall(self.dc.whoisStr) or empty
                msg = f"{key}, {self.resultDict[key]}"
                log.debug(msg)

    def _doExtractPattensFromWhoisString(
        self,
    ) -> None:
        empty = [""]  # Historical: we use 'empty string' as default, not None , or []

        sData: List[str] = []
        splitter = self.dc.thisTld.get("_split")
        if splitter:
            sData = splitter(self.dc.whoisStr, self.pc.verbose)
            if sData != []:
                for item in sData:
                    msg = f"split data: {item}"
                    log.debug(msg)

        for key, val in self.dc.thisTld.items():
            if key.startswith("_"):
                # skip meta element like: _server or _privateRegistry
                continue

            self.resultDict[key] = empty  # set a default
            if val is None:
                continue

            if callable(val):
                # vcall the curry function we created in tld_regexpr.py
                self.resultDict[key] = val(self.dc.whoisStr, sData, self.pc.verbose) or empty
                msg = f"_doExtractPattensFromWhoisString: call indirect {val} {key}, {self.resultDict[key]}"
                log.debug(msg)
                continue

            if isinstance(val, str):
                # we still support plain strings also
                self.resultDict[key] = re.findall(val, self.dc.whoisStr, flags=re.IGNORECASE) or empty
                msg = f"_doExtractPattensFromWhoisStringstr: {key}, {self.resultDict[key]}"
                log.debug(msg)
                continue

            msg = f"UNKNOWN: _doExtractPattensFromWhoisString {key}, {val}"
            log.debug(msg)

    def _doSourceIana(
        self,
    ) -> Optional[Domain]:
        self.dc.whoisStr = str(self.dc.whoisStr)

        # here we can handle the example.com and example.net permanent IANA domains
        k: str = "source:       IANA"

        msg: str = f"i have seen {k}"
        log.debug(msg)

        whois_splitted: List[str] = self.dc.whoisStr.split(k)
        z: int = len(whois_splitted)
        if z > 2:
            self.dc.whoisStr = k.join(whois_splitted[1:])
            self.dom = None
            return self.dom

        if z == 2 and whois_splitted[1].strip() != "":
            # if we see source: IANA and the part after is not only whitespace
            msg = f"after: {k} we see not only whitespace: {whois_splitted[1]}"
            log.debug(msg)

            self.dc.whoisStr = whois_splitted[1]
            self.dom = None
            return self.dom

        self._doExtractPattensFromWhoisString()  # try to parse this as a IANA domain as after is only whitespace
        self._doExtractPattensIanaFromWhoisString()  # now handle the actual format if this whois response

        self.dc.data = self.resultDict
        if self.dc.data["domain_name"][0]:
            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return self.dom

        self.dom = None
        return self.dom

    def _doIfServerNameLookForDomainName(self) -> None:
        if self.dc.whoisStr is None:
            return

        # not often available anymore
        if not re.findall(r"Server Name:\s?(.+)", self.dc.whoisStr, re.IGNORECASE):
            return

        msg = "i have seen Server Name:, looking for Domain Name:"
        log.debug(msg)

        # this changes the whoisStr, we may want to keep the original as extra
        self.dc.whoisStr = self.dc.whoisStr[self.dc.whoisStr.find("Domain Name:") :]

    def _doDnsSec(
        self,
    ) -> bool:
        if self.dc.whoisStr is None:
            return False

        whoisDnsSecList: List[str] = self.dc.whoisStr.split("DNSSEC:")
        if len(whoisDnsSecList) >= 2:
            msg = "DEGUG: i have seen dnssec: {whoisDnsSecStr}"
            log.debug(msg)

            whoisDnsSecStr: str = whoisDnsSecList[1].split("\n")[0]
            if whoisDnsSecStr.strip() == "signedDelegation" or whoisDnsSecStr.strip() == "yes":
                return True

        return False

    def _handleShortResponse(
        self,
    ) -> Optional[Domain]:
        if self.dc.whoisStr is None:
            self.dom = None
            return self.dom

        msg = f"shortResponse:: {self.dc.tldString} {self.dc.whoisStr}"
        log.debug(msg)

        # TODO: some short responses are actually valid:
        # lookfor Domain: and Status but all other fields are missing so the regexec could fail
        # this domain is taken already or reserved

        # whois syswow.64-b.it
        # [Querying whois.nic.it]
        # [whois.nic.it]
        # Domain:             syswow.64-b.it
        # Status:             UNASSIGNABLE

        # ---------------------------------
        # NOTE: from here s is lowercase only
        s = self.dc.whoisStr.strip().lower()
        noneStrings = NoneStrings()
        for i in noneStrings:
            if i in s:
                self.dom = None
                return self.dom

        # ---------------------------------
        # is there any error string in the result
        if s.count("error"):
            msg = "i see 'error' in the result, return: None"
            log.debug(msg)
            self.dom = None
            return self.dom

        # ---------------------------------
        quotaStrings = QuotaStrings()
        for i in quotaStrings:
            if i in s:
                if self.pc.simplistic:
                    msg = "WhoisQuotaExceeded"
                    self.dc.exeptionStr = msg

                    assert self.dom is not None
                    self.dom.init(
                        pc=self.pc,
                        dc=self.dc,
                    )
                    return self.dom

                raise WhoisQuotaExceeded(self.dc.whoisStr)

        if self.pc.simplistic:
            msg = "FailedParsingWhoisOutput"
            self.dc.exeptionStr = msg

            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return self.dom

        raise FailedParsingWhoisOutput(self.dc.whoisStr)

    def _extractWhoisServer(self) -> List[str]:
        # jp starts comments with [\s
        result = re.findall(r"^Using\s+server\s+([^\n]*)\n", str(self.dc.whoisStr), flags=re.IGNORECASE)
        if result:
            return result

        result = re.findall(r"\[(?=[^\s])([^\]]*)\]\r?\n", str(self.dc.whoisStr), flags=re.IGNORECASE)
        if result:
            return result

        return []

    def _cleanupWhoisResponse(
        self,
    ) -> str:
        tmp2: List[str] = []
        self.dc.whoisStr = str(self.dc.whoisStr)

        tmp: List[str] = self.dc.whoisStr.split("\n")
        for line in tmp:
            # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
            if "quota exceeded" in line.lower():
                raise WhoisQuotaExceeded(self.dc.whoisStr)

            if ":101: no entries found" in line.lower():  # google.co.cz has a response longer than 5 but no data
                break

            if self.pc.with_cleanup_results is True and line.startswith("%"):  # only remove if requested
                continue

            if self.pc.withRedacted is False:
                for item in IgnoreStrings():
                    if item in line:  # note we do not use ignorecase currently here
                        continue

                if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                    continue

            if "Please query the RDDS service of the Registrar of Record" in line:  # these lines contibute nothing so ignore
                continue

            if line.startswith("Terms of Use:"):  # these lines contibute nothing so ignore
                continue

            # we can now remove \r as all regexecs have been cleaned and strip all trailing whitespace
            tmp2.append(line.strip("\r").rstrip())

        self.dc.whoisStr = "\n".join(tmp2)
        return self.dc.whoisStr

    # public

    def verifyPrivateRegistry(
        self,
    ) -> bool:
        # may raise WhoisPrivateRegistry
        # we know the tld but it has no whois or does not respond with any information
        if not self.dc.thisTld.get("_privateRegistry"):
            return False

        if self.pc.simplistic is False:
            msg = "WhoisPrivateRegistry"
            raise WhoisPrivateRegistry(msg)

        return True

    def doServerHintsForThisTld(
        self,
    ) -> None:
        # note _server are currently passed down when using "extend", 2023-09-04 mboot
        server = self.dc.thisTld.get("_server")
        if self.pc.server is None and server:
            self.pc.server = server

    def doSlowdownHintForThisTld(
        self,
    ) -> int:
        self.pc.slow_down = self.pc.slow_down or 0

        slowDown = self.dc.thisTld.get("_slowdown")
        if slowDown:
            if self.pc.slow_down == 0 and int(slowDown) > 0:
                self.pc.slow_down = int(slowDown)

        if int(self.pc.slow_down):
            msg = f"using _slowdown hint {self.pc.slow_down} for tld: {self.dc.tldString}"
            log.debug(msg)

        return int(self.pc.slow_down)

    def getThisTld(self, tldString: str) -> None:
        self.dc.thisTld = get_TLD_RE().get(tldString, {})
        msg = f"{self.dc.thisTld}"
        log.debug(msg)

    def init(
        self,
    ) -> None:
        self.dc.whoisStr = str(self.dc.whoisStr)

        self.resultDict = {
            "tld": str(self.dc.tldString),
            "DNSSEC": self._doDnsSec(),
        }
        self.dc.servers = self._extractWhoisServer()
        self._cleanupWhoisResponse()

    def parse(
        self,
        dom: Optional[Domain],
    ) -> Tuple[Optional[Domain], bool]:
        self.dc.whoisStr = str(self.dc.whoisStr)
        self.dom = dom

        if self.dc.whoisStr.count("\n") < self.pc.shortResponseLen:
            self.dom = self._handleShortResponse()  # may raise: FailedParsingWhoisOutput, WhoisQuotaExceeded,
            return self.dom, True

        if "source:       IANA" in self.dc.whoisStr:
            # historical IANA domains
            self.dom = self._doSourceIana()
            if self.dom is not None:
                return self.dom, True

        if "Server Name" in self.dc.whoisStr:
            # old type Server Name (not very common anymore)
            self._doIfServerNameLookForDomainName()

        self._doExtractPattensFromWhoisString()

        # do we have a result and does it have a domain name
        self.dc.data = self.resultDict
        if self.dc.data["domain_name"][0]:
            assert self.dom is not None
            self.dom.init(
                pc=self.pc,
                dc=self.dc,
            )
            return self.dom, True

        return None, False
