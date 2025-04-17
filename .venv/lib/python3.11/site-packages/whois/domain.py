#! /usr/bin/env python3

# import sys
import os
import re
import logging

from typing import (
    Any,
    List,
    Dict,
)

from .handleDateStrings import str_to_date
from .context.parameterContext import ParameterContext
from .context.dataContext import DataContext

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class Domain:
    # The docstrings for classes should summarize its behavior
    # and list the public methods and instance variables.
    """
    A class to represent a standarized result of a whois lookup

    # Attributes
    * Attributes are created dynamically,
    not all domains have currently the same amount.

    - name: str, the domain name
    - tld: str, the detected top level domain
    - name_servers: List, a list of detected name servers
    - DNSSEC: boolean

    - status: List
    - registrar: str
    - registrant: str
    - registrant_country:
    - emails: List

    - updated_date: datetime
    - expiration_date: datetime
    - creation_date: datetime

    Methods
    -------
    def init(pc: ParameterContext,dc: DataContext) -> None:
        initialize the object with the current data from dc.data: Dict[str, Any]
        the init is separated from creating an instance as we want to use dependency injection as much as possible.
    """

    def _cleanupArray(
        self,
        data: List[str],
    ) -> List[str]:
        if "" in data:
            index = data.index("")
            data.pop(index)
        return data

    def _doNameservers(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        tmp: List[str] = []
        for x in dc.data["name_servers"]:
            if isinstance(x, str):
                tmp.append(x.strip().lower())
                continue

            # not a string but an array
            for y in x:
                tmp.append(y.strip().lower())

        self.name_servers: List[str] = []
        for x in tmp:
            x = x.strip(" .")  # remove any leading or trailing spaces and/or dots
            if x:
                if " " in x:
                    x, _ = x.split(" ", 1)
                    x = x.strip(" .")

                x = x.lower()
                if x not in self.name_servers:
                    self.name_servers.append(x)

        self.name_servers = sorted(self.name_servers)

    def cleanStatus(self, item: str) -> str:
        if "icann.org/epp#" in item:
            res = re.split(r"\s*\(?https?://(www\.)?icann\.org/epp#\s*", item)
            if res and res[0]:
                return res[0].strip()

        if "identitydigital.au/get-au/whois-status-codes#" in item:
            res = re.split(r"\s*https://identitydigital\.au/get-au/whois-status-codes#\s*", item)
            if res and res[0]:
                return res[0].strip()

        return item

    def _doStatus(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        self.status = dc.data["status"][0].strip()

        if pc.stripHttpStatus:
            self.status = self.cleanStatus(self.status)

        # sorted added to get predictable output during test
        # deduplicate results with set comprehension {}

        self.statuses = sorted(
            list({s.strip() for s in dc.data["status"]}),
        )
        if "" in self.statuses:
            self.statuses = self._cleanupArray(self.statuses)

        if pc.stripHttpStatus:
            z = []
            for item in self.statuses:
                item = self.cleanStatus(item)
                z.append(item)
            self.statuses = z

    def _doOptionalFields(
        self,
        data: Dict[str, Any],
    ) -> None:
        # optional fields

        if "owner" in data:
            self.owner = data["owner"][0].strip()

        if "abuse_contact" in data:
            self.abuse_contact = data["abuse_contact"][0].strip()

        if "reseller" in data:
            self.reseller = data["reseller"][0].strip()

        if "registrant" in data:
            if "registrant_organization" in data:
                self.registrant = data["registrant_organization"][0].strip()
            else:
                self.registrant = data["registrant"][0].strip()

        if "admin" in data:
            self.admin = data["admin"][0].strip()

        if "emails" in data:
            # sorted added to get predictable output during test
            # list(set(...))) to deduplicate results

            self.emails = sorted(
                list({s.strip() for s in data["emails"]}),
            )
            if "" in self.emails:
                self.emails = self._cleanupArray(self.emails)

    def _parseData(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        # process mandatory fields that we expect always to be present
        # even if we have None or ''
        self.registrar = dc.data["registrar"][0].strip()
        self.registrant_country = dc.data["registrant_country"][0].strip()

        # date time items
        self.creation_date = str_to_date(dc.data["creation_date"][0], self.tld)
        self.expiration_date = str_to_date(dc.data["expiration_date"][0], self.tld)
        self.last_updated = str_to_date(dc.data["updated_date"][0], self.tld)

        self.dnssec = dc.data["DNSSEC"]
        self._doStatus(pc, dc)
        self._doNameservers(pc, dc)

        # optional fields
        self._doOptionalFields(dc.data)

    def __init__(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        pass

    def init(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        if pc.include_raw_whois_text and dc.whoisStr is not None:
            self.text = dc.whoisStr

        if dc.exeptionStr is not None:
            self._exception = dc.exeptionStr
            return

        if dc.data == {}:
            return

        msg = f"{dc.data}"
        log.debug(msg)

        k = "domain_name"
        if k in dc.data:
            self.name = dc.data["domain_name"][0].strip().lower()

        k = "tld"
        if k in dc.data:
            self.tld = dc.data[k].lower()

        if pc.withPublicSuffix and dc.hasPublicSuffix:
            self.public_suffix: str = str(dc.publicSuffixStr)

        if pc.extractServers:
            self.servers = dc.servers
            self.server = ""
            if self.servers:
                self.server = self.servers[-1]

        if pc.return_raw_text_for_unsupported_tld is True:
            return

        self._parseData(pc, dc)
