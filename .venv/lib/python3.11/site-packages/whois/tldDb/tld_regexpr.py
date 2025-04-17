# pylint: disable=C0302
import os
import logging

from typing import (
    Dict,
    Any,
    # Callable,
)

from .finders import (
    newLineSplit,
    R,
    findFromToAndLookFor,
    findFromToAndLookForWithFindFirst,
    findInSplitedLookForHavingFindFirst,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


# 2023-09-03 mboot, all _items are inherited, confirmed
# only _<domains> as meta domains do net end up in the database

# ======================================
# Interesting for future enhancements:
# https://github.com/rfc1036/whois/blob/next/tld_serv_list
# https://github.com/rfc1036/whois/blob/next/new_gtlds_list
# seems the most up to date and maintained


def xStr(what: str, times: int = 1, firstMandatory: bool = True) -> str:
    # =================================================================
    # Often we want to repeat regex patterns,
    #   ( typically with nameservers or status fields )
    #   that becomes unreadable very fast.
    # Allow for a simplification that expands on usage and
    #   allow forcing the first to be mandatory as default,
    #   but overridable when needed

    if times < 1:
        return ""

    if firstMandatory and what[-1] == "?":
        return what[:-1] + (what * (times - 1))

    return what * times


# =================================================================
# The database
# When we finally apply the regexes we use IGNORE CASE allways on all matches

ZZ: Dict[str, Any] = {}

# ======================================
# meta registrars start with _ are only used a s a common toll to define others
# NOTE: _server is not inherited down stream, currently

ZZ["_privateReg"] = {"_privateRegistry": True}

ZZ["_teleinfo"] = {"extend": "com", "_server": "whois.teleinfo.cn"}  # updated all downstream

ZZ["_uniregistry"] = {"extend": "com", "_server": "whois.uniregistry.net"}  # updated all downstream

ZZ["_donuts"] = {
    "extend": "com",
    "_server": "whois.donuts.co",
    "registrant": R(r"Registrant Organization:\s?(.+)"),
    "status": R(r"Domain Status:\s?(.+)"),
}  # updated all downstream

ZZ["_centralnic"] = {
    "extend": "com",
    "_server": "whois.centralnic.com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Domain Status:\s?(.+)"),
}  # updated all downstream

ZZ["_gtldKnet"] = {
    "extend": "com",
    "_server": "whois.gtld.knet.cn",
    "admin": R(r"Admin\s*Name:\s+(.+)"),
    "_test": None,
}  # updated all downstream

# ======================================
# start of regular entries, simple domains are at the end

ZZ["com"] = {
    "domain_name": R(r"Domain Name\s*:\s*(.+)"),
    "registrar": R(r"Registrar:\s?(.+)"),
    "registrant": R(r"Registrant\s*Organi(?:s|z)ation:([^\n]*)"),
    "registrant_country": R(r"Registrant Country:\s?(.+)"),
    "creation_date": R(r"Creation Date:[ \t]*([^\n]*)"),
    "expiration_date": R(r"(?:Expiry|Expiration) Date:[ \t]*([^\n]*)"),
    "updated_date": R(r"Updated Date:[\t ]*([^\n]*)"),
    "name_servers": R(r"Name Server:\s*(.+)\s*"),
    "status": R(r"Status:\s?(.+)"),
    "emails": R(r"([\w\.-]+@[\w\.-]+\.[\w]{2,4})"),
    "_test": "google.com",
}

ZZ["uk"] = {
    "extend": "com",
    "_server": "whois.nic.uk",
    "registrant": R(r"Registrant:\n\s*(.+)"),
    "creation_date": R(r"Registered on:\s*(.+)"),
    "expiration_date": R(r"Expiry date:\s*(.+)"),
    "updated_date": R(r"Last updated:\s*(.+)"),
    "name_servers": R(r"Name servers:%s\n\n" % xStr(r"(?:\n[ \t]+(\S+).*)?", 10)),  # capture up to 10
    "status": R(r"Registration status:\n\s*(.+)"),
}

ZZ["ac.uk"] = {
    "extend": "uk",
    "_server": "whois.nic.ac.uk",
    "domain_name": R(r"Domain:\n([^\n]*)"),
    "owner": R(r"Domain Owner:\n\s?(.+)"),
    "registrar": R(r"Registered By:\n\s?(.+)"),
    "registrant": R(r"Registrant Contact:\n([^\n]*)"),
    "name_servers": R(r"Servers:%s\n\n" % xStr(r"(?:\n[ \t]+(\S+).*)?", 10)),
    "expiration_date": R(r"Renewal date:\n\s*(.+)"),
    "updated_date": R(r"Entry updated:\n\s*(.+)"),
    "creation_date": R(r"Entry created:\n\s?(.+)"),
    "_test": "imperial.ac.uk",
}

ZZ["co.uk"] = {
    "extend": "uk",
    "_server": "whois.nic.uk",
    "domain_name": R(r"Domain name:\s+(.+)"),
    "owner": R(r"Domain Owner:\s+(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "registrant": R(r"Registrant:\n\s+(.+)"),
    "status": R(r"Registration status:\s*(.+)"),
    "creation_date": R(r"Registered on:(.+)"),
    "expiration_date": R(r"Expiry date:(.+)"),
    "updated_date": R(r"Last updated:(.+)"),
    "_test": "livedns.co.uk",
}

ZZ["gov.uk"] = {
    "extend": "ac.uk",
    "_server": "whois.gov.uk",
    "_test": "service.gov.uk",
}

ZZ["org.uk"] = {
    "extend": "co.uk",
    "_test": "greenpeace.org.uk",
}

# ltd.uk: no example to test with

ZZ["me.uk"] = {
    "extend": "co.uk",
    "_server": "whois.nic.uk",
    "_test": "xxx.me.uk",
}

ZZ["net.uk"] = {
    "extend": "co.uk",
    "_server": "whois.nic.uk",
    "_test": "nic.net.uk",  # is actually a expired record it seems
}

# nhs.uk: may not have a whois server example is scot.nhs.uk or digital.nhs.uk
# plc.uk: no example to test with
# police.uk: no example to test; may not actually have a public whois server

# Armenia
ZZ["am"] = {
    "domain_name": R(r"Domain name:\s+(.+)"),
    "_server": "whois.amnic.net",
    "status": R(r"Status:\s(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "registrant": R(r"Registrant:\s+(.+)"),
    "registrant_country": R(r"Registrant:\n.+\n.+\n.+\n\s+(.+)"),
    "creation_date": R(r"Registered:\s+(.+)"),
    "expiration_date": R(r"Expires:\s+(.+)"),
    "updated_date": R(r"Last modified:\s+(.+)"),
    "name_servers": R(r"DNS servers.*:\n%s" % xStr(r"(?:\s+(\S+)\n)?", 4)),
    "_test": "amnic.net",
}

# Amsterdam
ZZ["amsterdam"] = {
    "extend": "com",
    "_server": "whois.nic.amsterdam",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Domain Status:\s?(.+)"),
    "_test": "nic.amsterdam",
}

# Argentina
ZZ["ar"] = {
    "extend": "com",
    "_server": "whois.nic.ar",
    "domain_name": R(r"domain\s*:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    "creation_date": R(r"registered:\s?(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"changed\s*:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "_test": "nic.ar",
}

# Austria
ZZ["at"] = {
    "extend": "com",
    "_server": "whois.nic.at",
    "domain_name": R(r"domain:\s?(.+)"),
    "updated_date": R(r"changed:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    # "registrant": R(r"registrant:\s?(.+)"),
    "registrant": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"nic-hdl:\s*{}\n",
        extract=r"organization:\s*([^\n]*)\n",
    ),
    "registrant_country": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"nic-hdl:\s*{}\n",
        extract=r"country:\s*([^\n]*)\n",
    ),
    "_test": "nic.at",
    "_split": newLineSplit(),
}

ZZ["ax"] = {
    "extend": "com",
    "_server": "whois.ax",
    "domain_name": R(r"domain\.+:\s*(\S+)"),
    "registrar": R(r"registrar\.+:\s*(.+)"),
    "creation_date": R(r"created\.+:\s*(\S+)"),
    "expiration_date": R(r"expires\.+:\s*(\S+)"),
    "updated_date": R(r"modified\.+:\s?(\S+)"),
    "name_servers": R(r"nserver\.+:\s*(\S+)"),
    "status": R(r"status\.+:\s*(\S+)"),
    "registrant": R(r"Holder\s+name\.+:\s*(.+)\r?\n"),  # not always present see meta.ax and google.ax
    "registrant_country": R(r"country\.+:\s*(.+)\r?\n"),  # not always present see meta.ax and google.ax
}

ZZ["bank"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
}

ZZ["be"] = {
    "extend": "pl",
    "domain_name": R(r"\nDomain:\s*(.+)"),
    "registrar": R(r"Company Name:\n?(.+)"),
    "creation_date": R(r"Registered:\s*(.+)\n"),
    "status": R(r"Status:\s?(.+)"),
    "name_servers": R(r"Nameservers:(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?\n\n"),
}

ZZ["biz"] = {
    "extend": "com",
    "registrar": R(r"Registrar:\s?(.+)"),
    "registrant": R(r"Registrant Organization:\s?(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": None,
}

ZZ["br"] = {
    "extend": "com",
    "_server": "whois.registro.br",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R("nic.br"),
    "registrant": None,
    "owner": R(r"owner:\s?(.+)"),
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"expires:\s?(.+)"),
    "updated_date": R(r"changed:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"status:\s?(.+)"),
    "_test": "registro.br",
}

ZZ["by"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s*(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "registrant": R(r"Org:\s*(.+)"),
    "registrant_country": R(r"Country:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s*(.+)"),
    "expiration_date": R(r"Expiration Date:\s*(.+)"),
    "updated_date": R(r"Updated Date:\s*(.+)"),
    "name_servers": R(r"Name Server:\s+(\S+)\n"),
}

# Brittany (French Territory)
ZZ["bzh"] = {
    "extend": "fr",
    "_server": "whois.nic.bzh",
    "domain_name": R(r"Domain Name:\s*(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "registrant": R(r"Registrant Organization:\s*(.+)"),
    "registrant_country": R(r"Registrant Country:\s*(.*)"),
    "creation_date": R(r"Creation Date:\s*(.*)"),
    "expiration_date": R(r"Registry Expiry Date:\s*(.*)"),
    "updated_date": R(r"Updated Date:\s*(.*)"),
    "name_servers": R(r"Name Server:\s*(.*)"),
    "status": R(r"Domain Status:\s*(.*)"),
    "_test": "pik.bzh",
}

ZZ["cc"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
}

ZZ["cl"] = {
    "extend": "com",
    "registrar": R("nic.cl"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "name_servers": R(r"Name Server:\s*(.+)\s*"),
}

ZZ["cn"] = {
    "extend": "com",
    "registrar": R(r"Sponsoring Registrar:\s?(.+)"),
    "registrant": R(r"Registrant:\s?(.+)"),
    "creation_date": R(r"Registration Time:\s?(.+)"),
    "expiration_date": R(r"Expiration Time:\s?(.+)"),
}

ZZ["com.tr"] = {
    "extend": "com",
    "_server": "whois.trabis.gov.tr",
    "domain_name": R(r"\*\* Domain Name:\s?(.+)"),
    "registrar": R(r"Organization Name\s+:\s?(.+)"),
    "registrant": R(r"\*\* Registrant:\s+?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"Created on\.+:\s?(.+)."),
    "expiration_date": R(r"Expires on\.+:\s?(.+)."),  # note the trailing . on both dates fields
    "updated_date": None,
    "name_servers": R(r"\*\* Domain Servers:\n(?:(\S+).*\n)?(?:(\S+).*\n)?(?:(\S+).*\n)?(?:(\S+).*\n)?"),  # allow for ip addresses after the name server
    "status": None,
    "_test": "google.com.tr",
}

ZZ["co.il"] = {
    "extend": "com",
    "domain_name": R(r"domain:\s*(.+)"),
    "registrar": R(r"registrar name:\s*(.+)"),
    "registrant": None,
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": R(r"validity:\s*(.+)"),
    "updated_date": None,
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"status:\s*(.+)"),
}

ZZ["co.cz"] = {"extend": "cz"}
ZZ["cz"] = {
    "extend": "com",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    # "registrant": R(r"registrant:\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"registered:\s?(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"changed:\s?(.+)"),
    "name_servers": R(r"nserver:\s+(\S+)"),
    "status": R(r"status:\s*(.+)"),
    "registrant": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"contact:\s*{}\n",
        extract=r"org:\s*([^\n]*)\n",
    ),
    "_split": newLineSplit(),
}

ZZ["de"] = {
    "extend": "com",
    "domain_name": R(r"\ndomain:\s*(.+)"),
    "updated_date": R(r"\nChanged:\s?(.+)"),
    "name_servers": R(r"Nserver:\s*(.+)"),
}

# Denmark
ZZ["dk"] = {
    "domain_name": R(r"Domain:\s?(.+)"),
    "registrar": None,
    "registrant": R(r"Registrant\s*Handle:\s*\w*\s*Name:\s?(.+)"),
    "registrant_country": R(r"Country:\s?(.+)"),
    "creation_date": R(r"Registered:\s?(.+)"),
    "expiration_date": R(r"Expires:\s?(.+)"),
    "updated_date": None,
    "name_servers": R(r"Hostname:\s*(.+)\s*"),
    "status": R(r"Status:\s?(.+)"),
    "emails": None,
}

ZZ["edu"] = {
    "extend": "com",
    "registrant": R(r"Registrant:\s*(.+)"),
    "creation_date": R(r"Domain record activated:\s?(.+)"),
    "updated_date": R(r"Domain record last updated:\s?(.+)"),
    "expiration_date": R(r"Domain expires:\s?(.+)"),
    "name_servers": R(r"Name Servers:\s?%s" % xStr(r"(?:\t(.+)\n)?", 10)),
    "_test": "rutgers.edu",
}

# estonian
ZZ["ee"] = {
    "extend": "com",
    "domain_name": R(r"Domain:\nname:\s+(.+\.ee)\n"),
    "registrar": R(r"Registrar:\nname:\s+(.+)\n"),
    "registrant": R(r"Registrant:\nname:\s+(.+)\n"),
    "registrant_country": R(r"Registrant:(?:\n+.+\n*)*country:\s+(.+)\n"),
    "creation_date": R(r"Domain:(?:\n+.+\n*)*registered:\s+(.+)\n"),
    "expiration_date": R(r"Domain:(?:\n+.+\n*)*expire:\s+(.+)\n"),
    "updated_date": R(r"Domain:(?:\n+.+\n*)*changed:\s+(.+)\n"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"Domain:(?:\n+.+\n*)*status:\s+(.+)\n"),
}

ZZ["eu"] = {
    "extend": "com",
    "_server": "whois.eu",
    "registrar": R(r"Name:\s?(.+)"),
    "domain_name": R(r"\nDomain:\s*(.+)"),
    "name_servers": R(r"Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?"),
}

ZZ["fi"] = {
    "domain_name": R(r"domain\.+:\s?(.+)"),
    "registrar": R(r"registrar\.+:\s?(.+)"),
    "creation_date": R(r"created\.+:\s?(.+)"),
    "expiration_date": R(r"expires\.+:\s?(.+)"),
    "updated_date": R(r"modified\.+:\s?(.+)"),
    "name_servers": R(r"nserver\.+:\s*(.+)"),
    "status": R(r"status\.+:\s?(.+)"),
    "registrant": R(r"Holder\s*\n\s*name\.*:\s*([^\n]*)\n"),
    "registrant_country": R(r"\ncountry\.*:\s*([^\n]*)\n"),
}

ZZ["fr"] = {
    "extend": "com",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s*(.+)"),
    # "registrant": R(r"contact:\s?(.+)"),
    # "registrant_organization": R(r"type:\s+ORGANIZATION\scontact:\s+(.*)"),
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"Expiry Date:\s?(.+)"),
    "updated_date": R(r"last-update:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"status:\s?(.+)"),
    # "registrant_country": R(r"Country:\s?(.+)"),
    "_test": "sfr.fr",
    "registrant": findFromToAndLookForWithFindFirst(
        findFirst=r"holder-c:\s*([^\n]*)\n",
        fromStr=r"nic-hdl:\s*{}\n",
        toStr=r"\n\n",
        lookForStr=r"contact:\s*([^\n]*)\n",
    ),
    "registrant_country": findFromToAndLookForWithFindFirst(
        findFirst=r"holder-c:\s*([^\n]*)\n",
        fromStr=r"nic-hdl:\s*{}\n",
        toStr=r"\n\n",
        lookForStr=r"country:\s*([^\n]*)\n",
    ),
}

# Hong Kong
ZZ["hk"] = {
    "extend": "com",
    "_server": "whois.hkirc.hk",
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "registrar": R(r"Registrar Name:\s?(.+)"),
    "registrant": R(r"Company English Name.*:\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"Domain Name Commencement Date:\s?(.+)"),
    "expiration_date": R(r"Expiry Date:\s?(.+)"),
    "updated_date": None,
    #  name servers have trailing whitespace, lines are \n only
    "name_servers": R(r"Name Servers Information:\s*(?:(\S+)[ \t]*\n)(?:(\S+)[ \t]*\n)?(?:(\S+)[ \t]*\n)?(?:(\S+)[ \t]*\n)?"),
    "status": None,
    "_test": "hkirc.hk",
}

ZZ["id"] = {
    "extend": "com",
    "registrar": R(r"Sponsoring Registrar Organization:\s?(.+)"),
    "creation_date": R(r"Created On:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "updated_date": R(r"Last Updated On:\s?(.+)$"),
}

ZZ["im"] = {
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "status": None,
    "registrar": None,
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": R(r"Expiry Date:\s?(.+)"),
    "updated_date": None,
    "name_servers": R(r"Name Server:(.+)"),
    "registrant": R(r"Domain Owners / Registrant\s*\n\s*Name:\s*([^\n]*)\n"),
}

ZZ["ir"] = {
    "_server": "whois.nic.ir",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R("nic.ir"),
    "registrant_country": None,
    "creation_date": None,
    "status": None,
    "expiration_date": R(r"expire-date:\s?(.+)"),
    "updated_date": R(r"last-updated:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "_test": "nic.ir",
}

ZZ["is"] = {
    "extend": "com",
    "_server": "whois.isnic.is",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": None,
    # "registrant": R(r"registrant:\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"expires:\s?(.+)"),
    "updated_date": None,
    "name_servers": R(r"nserver:\s?(.+)"),
    "status": None,
    "registrant": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"nic-hdl:\s*{}\n",
        extract=r"role:\s*([^\n]*)\n",
    ),
    "_split": newLineSplit(),
    "_test": "isnic.is",
}

ZZ["it"] = {
    "extend": "com",
    "domain_name": R(r"Domain:\s?(.+)"),
    "registrar": R(r"Registrar\s*Organization:\s*(.+)"),
    "registrant": R(r"Registrant\s*Organization:\s*(.+)"),
    "creation_date": R(r"Created:\s?(.+)"),
    "expiration_date": R(r"Expire Date:\s?(.+)"),
    "updated_date": R(r"Last Update:\s?(.+)"),
    "name_servers": R(r"Nameservers(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?"),
    "status": R(r"Status:\s?(.+)"),
}

# The Japanese whois servers always return English unless a Japanese locale is specified in the user's LANG environmental variable.
# See: https://www.computerhope.com/unix/uwhois.htm
# Additionally, whois qeuries can explicitly request english:
#   To suppress Japanese output, add'/e' at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.
#
ZZ["jp"] = {
    "domain_name": R(r"\[Domain Name\]\s?(.+)"),
    "registrar": R(r"\[ (.+) database provides information on network administration. Its use is    \]"),
    "registrant": R(r"\[Registrant\]\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"\[Created on\]\s?(.+)"),
    "expiration_date": R(r"\[Expires on\]\s?(.+)"),
    "updated_date": R(r"\[Last Updated\]\s?(.+)"),
    "name_servers": R(r"\[Name Server\]\s*(.+)"),
    "status": R(r"\[Status\]\s?(.+)"),
    "emails": R(r"([\w\.-]+@[\w\.-]+\.[\w]{2,4})"),
}

ZZ["co.jp"] = {
    "extend": "jp",
    "creation_date": R(r"\[Registered Date\]([^\n]*)\n"),  # possibly use Connected date
    "expiration_date": None,
    "updated_date": R(r"\[Last Update\]([^\n]*)\n"),
    "status": R(r"\[State\]\s?(.+)"),
}

ZZ["kg"] = {
    "domain_name": R(r"Domain\s+(\S+)"),
    "registrar": R(r"Billing\sContact:\n.*\n\s+Name:\s(.+)\n"),
    "registrant_country": None,
    "expiration_date": R(r"Record expires on:\s+(.+)"),
    "creation_date": R(r"Record created:\s+(.+)"),
    "updated_date": R(r"Record last updated on:\s+(.+)"),
    "name_servers": R(r"Name servers in the listed order:\n\n(?:(\S+)[ \t]*\S*\n)(?:(\S+)[ \t]*\S*\n)?(?:(\S+)[ \t]*\S*\n)?\n"),
    "status": R(r"Domain\s+\S+\s+\((\S+)\)"),
    "registrant": R(r"Administrative\sContact:\n.*\n\s+Name:\s(.+)\n"),
}

ZZ["kr"] = {
    "extend": "com",
    "_server": "whois.kr",
    "domain_name": R(r"Domain Name\s*:\s?(.+)"),
    "registrar": R(r"Authorized Agency\s*:\s*(.+)"),
    "registrant": R(r"Registrant\s*:\s*(.+)"),
    "creation_date": R(r"Registered Date\s*:\s?(.+)"),
    "expiration_date": R(r"Expiration Date\s*:\s?(.+)"),
    "updated_date": R(r"Last Updated Date\s*:\s?(.+)"),
    "status": R(r"status\s*:\s?(.+)"),
    "name_servers": R(r"Host Name\s+:\s+(\S+)\n"),
}

ZZ["kz"] = {
    "domain_name": R(r"Domain name\.+:\s(.+)"),
    "registrar": R(r"Current Registar:\s(.+)"),
    "registrant_country": R(r"Country\.+:\s?(.+)"),
    "expiration_date": None,
    "creation_date": R(r"Domain created:\s(.+)"),
    "updated_date": R(r"Last modified :\s(.+)"),
    "name_servers": R(r"ary server\.+:\s+(\S+)"),
    "status": R(r"Domain status :(?:\s+([^\n]+)\n)"),
    "registrant": R(r"Organization Using Domain Name\s*\n.*\n\s*Organization Name\.*:\s*([^\n]*)\n"),
}

ZZ["lt"] = {
    "extend": "com",
    "domain_name": R(r"Domain:\s?(.+)"),
    "creation_date": R(r"Registered:\s?(.+)"),
    "expiration_date": R(r"Expires:\s?(.+)"),
    "name_servers": R(r"Nameserver:\s*(.+)\s*"),
    "status": R(r"\nStatus:\s?(.+)"),
}

ZZ["lv"] = {
    "extend": "com",
    "_server": "whois.nic.lv",
    "domain_name": R(r"domain:\s*(.+)"),
    "creation_date": R(r"Registered:\s*(.+)\n"),  # actually there seem to be no dates
    "updated_date": R(r"Changed:\s*(.+)\n"),
    "expiration_date": R(r"paid-till:\s*(.+)"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"Status:\s?(.+)"),
    "_test": "nic.lv",
}

ZZ["me"] = {
    "extend": "biz",
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Expiry Date:\s?(.+)"),
    "updated_date": None,  # some entries have no date string but not always
    "name_servers": R(r"Name Server:\s*(\S+)\r?\n"),
    "status": R(r"Domain Status:\s?(.+)"),
}

ZZ["ml"] = {
    "extend": "com",
    "domain_name": R(r"Domain name:\s*([^(i|\n)]+)"),
    "registrar": R(r"(?<=Owner contact:\s)[\s\S]*?Organization:(.*)"),
    "registrant_country": R(r"(?<=Owner contact:\s)[\s\S]*?Country:(.*)"),
    "registrant": R(r"(?<=Owner contact:\s)[\s\S]*?Name:(.*)"),
    "creation_date": R(r"Domain registered: *(.+)"),
    "expiration_date": R(r"Record will expire on: *(.+)"),
    "name_servers": R(r"Domain Nameservers:\s*(.+)\n\s*(.+)\n"),
}

ZZ["mx"] = {
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "creation_date": R(r"Created On:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "updated_date": R(r"Last Updated On:\s?(.+)"),
    "registrar": R(r"Registrar:\s?(.+)"),
    "name_servers": R(r"\sDNS:\s*(.+)"),
    "registrant_country": R(r"\n\s*Country:\s*([^\n]*)\n"),
    "status": None,
    "registrant": R(r"\nRegistrant:\s*\n\s*Name:\s([^\n]*)\n"),
}
ZZ["com.mx"] = {"extend": "mx"}

# New-Caledonia (French Territory)
ZZ["nc"] = {
    "extend": "fr",
    "domain_name": R(r"Domain\s*:\s(.+)"),
    "registrar": R(r"Registrar\s*:\s(.+)"),
    "registrant": R(r"Registrant name\s*:\s(.+)"),
    "registrant_country": None,
    "creation_date": R(r"Created on\s*:\s(.*)"),
    "expiration_date": R(r"Expires on\s*:\s(.*)"),
    "updated_date": R(r"Last updated on\s*:\s(.*)"),
    "name_servers": R(r"Domain server [0-9]{1,}\s*:\s(.*)"),
    "status": None,
}

ZZ["nl"] = {
    "extend": "com",
    "expiration_date": None,
    "registrant_country": None,
    "domain_name": R(r"Domain name:\s?(.+)"),
    "name_servers": R(r"Domain nameservers.*:\n%s" % xStr(r"(?:\s+(\S+)\n)?", 10)),
    "reseller": R(r"Reseller:\s?(.+)"),
    "abuse_contact": R(r"Abuse Contact:\s?(.+)"),
    "_test": "google.nl",
    "_slowdown": 5,
}

# Norway
ZZ["no"] = {
    "domain_name": R(r"Domain Name\.+:\s?(.+)"),
    "registrar": R(r"Registrar Handle\.+:\s?(.+)"),
    "registrant": None,
    "registrant_country": None,
    "creation_date": R(r"Created:\s?(.+)"),
    "expiration_date": None,
    "updated_date": R(r"Last Updated:\s?(.+)"),
    "name_servers": R(r"Name Server Handle\.+:\s*(.+)\s*"),
    "status": None,
    "emails": None,
}

ZZ["nyc"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
}

ZZ["nz"] = {
    "domain_name": R(r"domain_name:\s?(.+)"),
    "registrar": R(r"registrar_name:\s?(.+)"),
    "registrant": R(r"registrant_contact_name:\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"domain_dateregistered:\s?(.+)"),
    "expiration_date": R(r"domain_datebilleduntil:\s?(.+)"),
    "updated_date": R(r"domain_datelastmodified:\s?(.+)"),
    "name_servers": R(r"ns_name_[0-9]{2}:\s?(.+)"),
    "status": R(r"query_status:\s?(.+)"),
    "emails": R(r"([\w\.-]+@[\w\.-]+\.[\w]{2,4})"),
}

ZZ["co.nz"] = {"extend": "com"}

ZZ["org"] = {
    "extend": "com",
    "expiration_date": R(r"\nRegistry Expiry Date:\s?(.+)"),
    "updated_date": R(r"\nLast Updated On:\s?(.+)"),
    "name_servers": R(r"Name Server:\s?(.+)\s*"),
}

ZZ["pharmacy"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"status:\s?(.+)"),
}

ZZ["pl"] = {
    "extend": "uk",
    "registrar": R(r"\nREGISTRAR:\s*(.+)\n"),
    "creation_date": R(r"\ncreated:\s*(.+)\n"),
    "updated_date": R(r"\nlast modified:\s*(.+)\n"),
    # "expiration_date": R(r"\noption expiration date:\s*(.+)\n"),
    # If no "option expiration date:" is present, use "renewal date:", but only
    # if it's not not followed by "option expiration date:". google.pl is the test case here
    "expiration_date": R(r"(?:\noption expiration date:|renewal date:(?!(?:.|\n)*\noption expiration date:))\s*(.+)\n"),
    "name_servers": R(r"nameservers:%s" % xStr(r"(?:\s+(\S+)[^\n]*\n)?", 4)),
    "status": R(r"\nStatus:\n\s*(.+)"),
    "_test": "google.pl",
}

ZZ["pt"] = {
    "_server": "whois.dns.pt",
    "extend": "com",
    "domain_name": R(r"Domain:\s?(.+)"),
    "registrar": None,
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "updated_date": None,
    "name_servers": R(r"Name Server:%s" % xStr(r"(?:\s*(\S+)[^\n]*\n)?", 2)),
    "status": R(r"Domain Status:\s?(.+)"),
    "_test": None,  # portugal never answeres, timout is all we get
}

ZZ["pw"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
}

ZZ["ru"] = {
    "extend": "com",
    "_server": "whois.tcinet.ru",
    "domain_name": R(r"domain:\s*(.+)"),
    "creation_date": R(r"created:\s*(.+)"),
    "expiration_date": R(r"paid-till:\s*(.+)"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"state:\s*(.+)"),
    "_test": "tcinet.ru",
}

ZZ["sa"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s*(.+\.sa)\s"),
    "registrant": R(r"Registrant:\n*(.+)\n"),
    "name_servers": R(r"Name Servers:\s*(.+)\s*(.+)?"),
    "registrant_country": None,
    "registrar": None,
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
    "status": None,
    "emails": None,
}

ZZ["sh"] = {
    "extend": "com",
    "registrant": R(r"\nRegistrant Organization:\s?(.+)"),
    "expiration_date": R(r"\nRegistry Expiry Date:\s*(.+)"),
    "status": R(r"\nDomain Status:\s?(.+)"),
}

ZZ["se"] = {
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    "registrant_country": None,
    "creation_date": R(r"created:\s+(\d{4}-\d{2}-\d{2})"),
    "expiration_date": R(r"expires:\s+(\d{4}-\d{2}-\d{2})"),
    "updated_date": R(r"modified:\s+(\d{4}-\d{2}-\d{2})"),
    "name_servers": R(r"nserver:\s*(.+)"),
    "status": R(r"status:\s?(.+)"),
    "registrant": R(r"holder:\s*([^\n]*)\n"),
}

# Singapore - Commercial sub-domain
ZZ["com.sg"] = {
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s?(.+)"),
    "registrant": R(r"Registrant:\r?\n\r?\n\s*Name:\s*(.+)\r?\n"),
    "registrant_country": None,
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "updated_date": R(r"Modified Date:\s?(.+)"),
    "name_servers": R(r"Name Servers:(?:\s+(\S+))(?:\s+(\S+))?(?:\s+(\S+))?(?:\s+([\.\w]+)\s+)?"),
    "status": R(r"Domain Status:\s*(.*)\r?\n"),
    "emails": R(r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}"),
}

# Slovakia
ZZ["sk"] = {
    "extend": "com",
    "_server": "whois.sk-nic.sk",
    "domain_name": R(r"Domain:\s?(.+)"),
    "creation_date": R(r"Created:\s?(.+)"),
    "expiration_date": R(r"Valid Until:\s?(.+)"),
    "updated_date": R(r"Updated:\s?(.+)"),
    "name_servers": R(r"Nameserver:\s*(\S+)"),
    "_test": "sk-nic.sk",
    # look for Organiztion but in the proper section
    "registrant": findFromToAndLookFor(
        fromStr=r"Domain registrant:",
        toStr=r"\n\n",
        lookForStr=r"Organization:\s*([^\n]*)\n",
    ),
    # Country Code:
    "registrant_country": findFromToAndLookFor(
        fromStr=r"Domain registrant:",
        toStr=r"\n\n",
        lookForStr=r"Country Code:\s*([^\n]*)\n",
    ),
    "registrar": findFromToAndLookFor(
        fromStr=r"\nRegistrar:",
        toStr=r"\n\n",
        lookForStr=r"Organization:\s*([^\n]*)\n",
        verbose=True,
    ),
}

ZZ["tel"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"\nRegistry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
}

# Thailand - Commercial sub-domain
ZZ["co.th"] = {
    "_server": "whois.thnic.co.th",
    "extend": "com",
    "registrant": R(r"Domain Holder Organization:\s?(.+)"),
    "registrant_country": R(r"Domain Holder Country:\s?(.+)"),
    "creation_date": R(r"Created date:\s?(.+)"),
    "expiration_date": R(r"Exp date:\s?(.+)"),
    "updated_date": R(r"Updated date:\s?(.+)"),
    "_test": "thnic.co.th",
}

ZZ["tn"] = {
    "extend": "com",
    "domain_name": R(r"Domain name\.+:(.+)\s*"),
    "registrar": R(r"Registrar\.+:(.+)\s*"),
    "registrant": R(r"Owner Contact\n+Name\.+:\s?(.+)"),
    "registrant_country": R(r"Owner Contact\n(?:.+\n)+Country\.+:\s(.+)"),
    "creation_date": R(r"Creation date\.+:\s?(.+)"),
    "expiration_date": None,
    "updated_date": None,
    "name_servers": R(r"DNS servers\n%s" % xStr(r"(?:Name\.+:\s*(\S+)\n)?", 4)),
    "status": R(r"Domain status\.+:(.+)"),
}

ZZ["tv"] = {
    "extend": "com",
    "_server": "whois.nic.tv",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
    "_test": "nic.tv",
}

ZZ["tz"] = {
    "domain_name": R(r"\ndomain:\s*(.+)"),
    "registrar": R(r"\nregistrar:\s?(.+)"),
    "registrant": R(r"\nregistrant:\s*(.+)"),
    "registrant_country": None,
    "creation_date": R(r"\ncreated:\s*(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"\nchanged:\s*(.+)"),
    "status": None,
    "name_servers": R(r"\nnserver:\s*(.+)"),
}

ZZ["ua"] = {
    "extend": "com",
    "domain_name": R(r"\ndomain:\s*(.+)"),
    "registrar": R(r"\nregistrar:\s*(.+)"),
    "registrant_country": R(r"\ncountry:\s*(.+)"),
    "creation_date": R(r"\ncreated:\s+(.+)"),
    "expiration_date": R(r"\nexpires:\s*(.+)"),
    "updated_date": R(r"\nmodified:\s*(.+)"),
    "name_servers": R(r"\nnserver:\s*(.+)"),
    "status": R(r"\nstatus:\s*(.+)"),
}

ZZ["uz"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Expiration Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
    "name_servers": R(r"Domain servers in listed order:%s\n\n" % xStr(r"(?:\n\s+(\S+))?", 4)),
    # sometimes 'not.defined is returned as a nameserver (e.g. google.uz)
}

ZZ["wiki"] = {
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
}

ZZ["work"] = {
    "extend": "com",
    "_server": "whois.nic.work",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "_test": "nic.work",
}

ZZ["ac"] = {
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "status": R(r"Domain Status:\s(.+)"),
    "name_servers": R(r"Name Server:\s+(\S+)"),
    "registrant_country": R(r"Registrant Country:\s*(.*)\r?\n"),
    "updated_date": R(r"Updated Date:\s+(.+)"),
    "creation_date": R(r"Creation Date:\s+(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s+(.+)"),
    "registrant": R(r"Registrant Organization:\s*([^\n]*)\n"),
}

ZZ["ae"] = {
    "extend": "ar",
    "_server": "whois.aeda.net.ae",
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "registrar": R(r"Registrar Name:\s+(.+)"),
    "status": R(r"Status:\s(.+)"),
    "name_servers": R(r"Name Server:\s+(\S+)"),
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
    "_test": "net.ae",
}

ZZ["bg"] = {
    "_server": "whois.register.bg",
    "domain_name": R(r"DOMAIN\s+NAME:\s+(.+)"),
    "status": R(r"registration\s+status:\s(.+)"),
    "name_servers": R(r"NAME SERVER INFORMATION:\n%s" % xStr(r"(?:(.+)\n)?", 4)),
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
    "registrar": None,
    "registrant_country": None,
    "_test": "register.bg",
}

ZZ["bj"] = {
    "_server": "whois.nic.bj",
    "extend": "com",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Registrar:\s*(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "status": R(r"Status:\s?(.+)"),
    "name_servers": R(r"Name Server:\s+(\S+)\n"),
    "_test": "nic.bj",
}

ZZ["cf"] = {
    "domain_name": None,
    "name_servers": R(r"Domain Nameservers:\n(?:(.+)\n)(?:(.+)\n)?(?:(.+)\n)?(?:(.+)\n)?"),
    "registrar": R(r"Record maintained by:\s+(.+)"),
    "creation_date": R(r"Domain registered:\s?(.+)"),
    "expiration_date": R(r"Record will expire:\s?(.+)"),
    "updated_date": None,
    "registrant_country": None,
    # very restrictive, after a few queries it will refuse with try again later
    "_slowdown": 5,
}

ZZ["re"] = {
    "extend": "ac",
    "domain_name": R(r"domain:\s+(.+)"),
    "registrar": R(r"registrar:\s+(.+)"),
    "name_servers": R(r"nserver:\s+(.+)"),
    "status": R(r"status:\s(.+)"),
    "creation_date": R(r"created:\s+(.+)"),
    "expiration_date": R(r"Expiry Date:\s+(.+)"),
    "updated_date": R(r"last-update:\s+(.*)"),
    "registrant_country": None,
}

ZZ["ro"] = {
    "domain_name": R(r"\s+Domain name:\s+(.+)"),
    "registrar": R(r"\s+Registrar:\s+(.+)"),
    "creation_date": R(r"\s+Registered On:\s+(.+)"),
    "expiration_date": R(r"\s+Expires On:\s+(.+)"),
    "status": R(r"\s+Domain Status:\s(.+)"),
    "name_servers": R(r"\s+NameServer:\s+(.+)"),
    "registrant_country": None,
    "updated_date": None,
}

ZZ["rs"] = {
    "domain_name": R(r"Domain name:\s+(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "status": R(r"Domain status:\s(.+)"),
    "creation_date": R(r"Registration date:\s+(.+)"),
    "expiration_date": R(r"Expiration date:\s+(.+)"),
    "updated_date": R(r"Modification date:\s+(.+)"),
    "name_servers": R(r"DNS:\s+(.+)"),
    "registrant_country": None,
    "registrant": R(r"Registrant:\s*([^\n]*)\n"),
}

# Singapore
ZZ["sg"] = {
    "_server": "whois.sgnic.sg",
    "registrar": R(r"Registrar:\s+(.+)"),
    "domain_name": R(r"\s+Domain name:\s+(.+)"),
    "creation_date": R(r"\s+Creation Date:\s+(.+)"),
    "expiration_date": R(r"\s+Expiration Date:\s+(.+)"),
    "updated_date": R(r"\s+Modified Date:\s+(.+)"),
    "status": R(r"\s+Domain Status:\s(.+)"),
    "registrant_country": None,
    "name_servers": R(r"Name Servers:%s" % xStr(r"(?:\n[ \t]+(\S+)[^\n]*)?", 4)),
    # make sure the dnssec is not matched
    "_test": "sgnic.sg",
}

ZZ["tw"] = {
    "_server": "whois.twnic.net.tw",
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "creation_date": R(r"\s+Record created on\s+(.+)"),
    "expiration_date": R(r"\s+Record expires on\s+(.+)"),
    "status": R(r"\s+Domain Status:\s+(.+)"),
    "registrar": R(r"Registration\s+Service\s+Provider:\s+(.+)"),
    "updated_date": None,
    "registrant_country": None,
    "name_servers": R(r"Domain servers in listed order:%s" % xStr(r"(?:\s+(\S+)[ \t]*\r?\n)?", 4)),
    "_test": "net.tw",
    "registrant": R(r"\n\s*Registrant:[\s\n]*([^\n]*)\n*"),
}

ZZ["ug"] = {
    "_server": "whois.co.ug",
    "domain_name": R(r"Domain name:\s+(.+)"),
    "creation_date": R(r"Registered On:\s+(.+)"),
    "expiration_date": R(r"Expires On:\s+(.+)"),
    "status": R(r"Status:\s+(.+)"),
    "name_servers": R(r"Nameserver:\s+(.+)"),
    "registrant_country": R(r"Registrant Country:\s+(.+)"),
    "updated_date": R(r"Renewed On:\s+(.+)"),
    "registrar": None,
    "registrant": R(r"Registrant Organization:\s*([^\n]*)\n"),
    "_test": "nic.co.ug",
}

ZZ["ws"] = {
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "creation_date": R(r"Creation Date:\s+(.+)"),
    "expiration_date": R(r"Registrar Registration Expiration Date:\s+(.+)"),
    "updated_date": R(r"Updated Date:\s?(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "status": R(r"Domain Status:\s(.+)"),
    "name_servers": R(r"Name Server:\s+(.+)"),
    "registrant_country": None,
    "_server": "whois.website.ws",
    "_test": "website.ws",
}

ZZ["re"] = {
    "domain_name": R(r"domain:\s+(.+)"),
    "status": R(r"status:\s+(.+)"),
    "registrar": R(r"registrar:\s+(.+)"),
    "name_servers": R(r"nserver:\s+(.+)"),
    "creation_date": R(r"created:\s+(.+)"),
    "expiration_date": R(r"Expiry Date:\s+(.+)"),
    "updated_date": R(r"last-update:\s+(.+)"),
    "registrant_country": None,
}

ZZ["bo"] = {
    "domain_name": R(r"\s*NOMBRE DE DOMINIO:\s+(.+)"),
    "registrant_country": R(r"País:\s+(.+)"),
    "creation_date": R(r"Fecha de activación:\s+(.+)"),
    "expiration_date": R(r"Fecha de corte:\s+(.+)"),
    "registrar": None,
    "status": None,
    "name_servers": None,  # bo has no nameservers, use host -t ns <domain>
    "updated_date": None,
    "registrant": R(r"CONTACTO ADMINISTRATIVO\nRazón social:\s*([^\n]*)\n"),
}

ZZ["hr"] = {
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "name_servers": R(r"Name Server:\s+(.+)"),
    "creation_date": R(r"Creation Date:\s+(.+)"),
    "updated_date": R(r"Updated Date:\s+(.+)"),
    "status": None,
    "registrar": R(r"Registrar:\s*([^\n]*)\n"),
    "expiration_date": R(r"Registrar Registration Expiration Date:\s+(.+)"),
    "registrant_country": R(r"Registrant State/Province:\s*([^\n]*)\n"),
    "registrant": R(r"Registrant Name:\s*([^\n]*)\n"),
    "_test": "google.hr",
}

ZZ["gg"] = {
    "domain_name": R(r"Domain:\s*\n\s+(.+)"),
    "status": R(r"Domain Status:\s*\n\s+(.+)"),
    "registrar": R(r"Registrar:\s*\n\s+(.+)"),
    "name_servers": R(r"Name servers:(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?\n"),
    "creation_date": R(r"Relevant dates:\s*\n\s+Registered on(.+)"),
    "expiration_date": None,
    "updated_date": None,
    "registrant_country": None,
    "registrant": R(r"\nregistrant:\s*\n\s*([^\n]*)\n"),
}

ZZ["sn"] = {
    "_server": "whois.nic.sn",
    "domain_name": R(r"Nom de domaine:\s+(.+)"),
    "status": R(r"Statut:\s+(.+)"),
    "registrar": R(r"Registrar:\s+(.+)"),
    "name_servers": R(r"Serveur de noms:\s*(.+)"),
    "creation_date": R(r"Date de création:\s+(.+)"),
    "expiration_date": R(r"Date d'expiration:\s+(.+)"),
    "updated_date": R(r"Dernière modification:\s+(.+)"),
    "_test": "nic.sn",
    "registrant": findFromToAndLookFor(
        fromStr=r"\n\[HOLDER\]",
        toStr=r"\n\n",
        lookForStr=r"Nom:\s*([^\n]*)\n",
    ),
    "registrant_country": findFromToAndLookFor(
        fromStr=r"\n\[HOLDER\]",
        toStr=r"\n\n",
        lookForStr=r"Pays:\s*([^\n]*)\n",
    ),
}

ZZ["si"] = {
    "_server": "whois.register.si",
    "domain_name": R(r"domain:\s+(.+)"),
    "status": R(r"status:\s+(.+)"),
    "registrar": R(r"registrar:\s+(.+)"),
    "name_servers": R(r"nameserver:\s*(.+)"),
    "creation_date": R(r"created:\s+(.+)"),
    "expiration_date": R(r"expire:\s+(.+)"),
    "updated_date": None,
    "registrant_country": None,
    "_test": "register.si",
}

ZZ["st"] = {
    # .ST domains can now be registered with many different competing registrars. and hence different formats
    # >>> line appears quite early, valid info after would have been suppressed with the ^>>> cleanup rule: switched off
    "extend": "com",
    "registrant_country": R(r"registrant-country:\s+(\S+)"),
    "registrant": R(r"registrant-organi(?:s|z)ation:\s*(.+)\r?\n"),
    "expiration_date": R(r"Expiration\s+Date:\s?(.+)"),
}

ZZ["mk"] = {
    "_server": "whois.marnet.mk",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    # "registrant": R(r"registrant:\s?(.+)"),
    "registrant_country": R(r"Registrant Country:\s?(.+)"),
    "creation_date": R(r"registered:\s?(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"changed:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "status": R(r"Status:\s?(.+)"),
    "emails": R(r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}"),
    "_test": "marnet.mk",
    "registrant": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"contact:\s*{}\n",
        extract=r"org:\s*([^\n]*)\n",
    ),
    "_split": newLineSplit(),
}

ZZ["si"] = {
    "_server": "whois.register.si",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    "registrant": R(r"registrant:\s?(.+)"),
    "registrant_country": R(r"Registrant Country:\s?(.+)"),
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"changed:\s?(.+)"),
    "name_servers": R(r"nameserver:\s*(.+)\s*"),
    "status": R(r"Status:\s?(.+)"),
    "emails": R(r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}"),
    "_test": "register.si",
}

ZZ["tc"] = {
    "extend": "com",
    "_server": "whois.nic.tc",
    "domain_name": R(r"Domain Name:\s?(.+)"),
    "registrar": R(r"Sponsoring Registrar:\s?(.+)"),
    "creation_date": R(r"Creation Date:\s?(.+)"),
    "expiration_date": R(r"Registry Expiry Date:\s?(.+)"),
    "name_servers": R(r"Name Server:\s*(.+)\s*"),
    "status": R(r"Domain Status:\s?(.+)"),
    "_test": "nic.tc",
}

ZZ["wf"] = {
    "extend": "com",
    "_server": "whois.nic.wf",
    "domain_name": R(r"domain:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    "registrant": R(r"registrant:\s?(.+)"),
    "registrant_country": R(r"Registrant Country:\s?(.+)"),
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"Expiry Date:\s?(.+)"),
    "updated_date": R(r"last-update:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "status": R(r"\nstatus:\s?(.+)"),
    "_test": "nic.wf",
}

ZZ["mo"] = {
    "extend": "com",
    "_server": "whois.monic.mo",
    "name_servers": R(r"Domain name servers:\s+-+\s+(\S+)\n(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?"),
    "creation_date": R(r"Record created on (.+)"),
    "expiration_date": R(r"Record expires on (.+)"),
    "_test": "monic.mo",
}

ZZ["tm"] = {  # Turkmenistan
    "extend": "com",
    "domain_name": R(r"Domain\s*:\s*(.+)"),
    "expiration_date": R(r"Expiry\s*:\s*(\d+-\d+-\d+)"),
    "name_servers": R(r"NS\s+\d+\s+:\s*(\S+)"),
    "status": R(r"Status\s*:\s*(.+)"),
}

# venezuela
ZZ["ve"] = {
    "extend": "com",
    "_server": "whois.nic.ve",
    "domain_name": R(r"domain\s*:\s?(.+)"),
    "registrar": R(r"registrar:\s?(.+)"),
    # "registrant": R(r"registrant:\s?(.+)"),
    "creation_date": R(r"created:\s?(.+)"),
    "expiration_date": R(r"expire:\s?(.+)"),
    "updated_date": R(r"changed\s*:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "_test": "nic.ve",
    "registrant": findInSplitedLookForHavingFindFirst(
        findFirst=r"registrant:\s?(.+)",
        lookForStr=r"contact:\s*{}\n",
        extract=r"org:\s*([^\n]*)\n",
    ),
    "_split": newLineSplit(),
}

ZZ["lu"] = {
    "extend": "com",
    "_server": "whois.dns.lu",
    "domain_name": R(r"domainname\s*:\s?(.+)"),
    "registrar": R(r"registrar-name:\s?(.+)"),
    "name_servers": R(r"nserver:\s*(.+)\s*"),
    "status": R(r"domaintype\s*:\s*(.+)"),
    "registrant_country": R(r"org-country\s*:\s?(.+)"),
    "_test": "dns.lu",
}

ZZ["sm"] = {
    "extend": "rs",
    "_server": "whois.nic.sm",
    "domain_name": R(r"Domain Name:\s+(.+)"),
    "status": R(r"Status:\s(.+)"),
    "name_servers": R(r"DNS Servers:\s+(.+)"),
    "_test": "nic.sm",
}

ZZ["tg"] = {
    "extend": "com",
    "_server": "whois.nic.tg",
    "domain_name": R(r"domain:\.+\s?(.+)"),
    "registrar": R(r"registrar:\.+\s?(.+)"),
    "creation_date": R(r"Activation:\.+\s?(.+)"),
    "expiration_date": R(r"Expiration:\.+\s?(.+)"),
    "status": R(r"Status:\.+\s?(.+)"),
    "name_servers": R(r"Name Server \(DB\):\.+(.+)"),
    "_test": "nic.tg",
}

ZZ["md"] = {
    "extend": "com",
    "_server": "whois.nic.md",
    "domain_name": R(r"domain\s+name:\s?(.+)"),
    "status": R(r"domain\s+state:\s?(.+)"),
    "name_servers": R(r"Nameserver:(.+)"),
    "registrar": R(r"Registrar:\s?(.+)"),
    "creation_date": R(r"Registered\s+on:\s?(.+)"),
    "expiration_date": R(r"Expires\s+on:\s?(.+)"),
    "_test": "nic.md",
}

ZZ["tg"] = {
    "_server": "whois.nic.tg",
    "extend": "com",
    "_test": "nic.tg",
    "domain_name": R(r"domain:\.+\s?(.+)"),
    "registrar": R(r"registrar:\.+\s?(.+)"),
    "creation_date": R(r"Activation:\.+\s?(.+)"),
    "expiration_date": R(r"Expiration:\.+\s?(.+)"),
    "status": R(r"Status:\.+\s?(.+)"),
    "name_servers": R(r"Name Server \(DB\):\.+(.+)"),
}
ZZ["au"] = {
    "extend": "com",
    "registrar": R(r"Registrar Name:\s?(.+)"),
    "updated_date": R(r"Last Modified:([^\n]*)"),
    "registrant": r"Registrant:\s*([^\n]*)\n",
}

# unknown tld pf, pf, pf, pf, whois.registry.pf,
ZZ["pf"] = {
    "_server": "whois.registry.pf",
    "_test": "registry.pf",
    "status": R(r"Status\s*:(\S*)\n"),
    "creation_date": R(r"Created[^:]*:(\S*)\n"),
    "expiration_date": R(r"Expire[^:]*:(\S*)\n"),
    "updated_date": R(r"Last renewed[^:]*:(\S*)\n"),
    "name_servers": R(r"Name Server[^:]*:(\S*)\n"),
    "domain_name": R(r"Informations about\s*'([^']*)'\s*:"),
    "registrar": None,
    "registrant_country": None,
}
# Informations about 'registry.pf' :
# Status : active
# Created (JJ/MM/AAAA) : 04/02/2013
# Last renewed (JJ/MM/AAAA) : 02/02/2023
# Expire (JJ/MM/AAAA) : 02/02/2024
# Name server 1 : ns1.mana.pf
# Name server 2 : ns2.mana.pf
# ======================================
# ======================================
# ======================================

ZZ["aarp"] = {"_server": "whois.nic.aarp", "extend": "com", "_test": "nic.aarp"}
ZZ["abbott"] = {"_server": "whois.nic.abbott", "extend": "com", "_test": "nic.abbott"}
ZZ["abbvie"] = {"_server": "whois.nic.abbvie", "extend": "com", "_test": "nic.abbvie"}
ZZ["abc"] = {"_server": "whois.nic.abc", "extend": "com", "_test": "nic.abc"}
ZZ["abogado"] = {"_server": "whois.nic.abogado", "extend": "com", "_test": "nic.abogado"}
ZZ["abudhabi"] = {"_server": "whois.nic.abudhabi", "extend": "com", "_test": "nic.abudhabi"}
ZZ["academy"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ac.bd"] = {"extend": "bd"}
ZZ["accountant"] = {"extend": "com", "_server": "whois.nic.accountant", "_test": "nic.accountant"}
ZZ["accountants"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ac.jp"] = {"extend": "co.jp", "_test": "icu.ac.jp"}
ZZ["ac.ke"] = {"extend": "ke"}
ZZ["aco"] = {"_server": "whois.nic.aco", "extend": "com", "_test": "nic.aco"}
ZZ["ac.rw"] = {"extend": "rw"}
ZZ["ac.th"] = {"extend": "co.th", "_test": "chula.ac.th"}
ZZ["actor"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ac.ug"] = {"extend": "ug", "_privateRegistry": True}
ZZ["ad.jp"] = {"extend": "co.jp", "_test": "nic.ad.jp"}
ZZ["ads"] = {"_server": "whois.nic.ads", "extend": "com", "_test": "nic.ads"}
ZZ["adult"] = {"_server": "whois.nic.adult", "extend": "com", "_test": "nic.adult"}
ZZ["aeg"] = {"_server": "whois.nic.aeg", "extend": "com", "_test": "nic.aeg"}
ZZ["aero"] = {"extend": "ac", "_server": "whois.aero", "registrant_country": R(r"Registrant\s+Country:\s+(.+)")}
ZZ["af"] = {"extend": "ac"}
ZZ["com.af"] = {"extend": "af"}
ZZ["afl"] = {"_server": "whois.nic.afl", "extend": "com", "_test": "nic.afl"}
ZZ["africa"] = {"extend": "com", "_server": "whois.nic.africa", "_test": "nic.africa"}
ZZ["agakhan"] = {"_server": "whois.nic.agakhan", "extend": "com", "_test": "nic.agakhan"}
ZZ["agency"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ag"] = {"extend": "ac"}
ZZ["com.ag"] = {"extend": "ac"}

ZZ["ai"] = {"extend": "com", "_server": "whois.nic.ai"}  # Anguill, "_test": "nic.ai"}
ZZ["airbus"] = {"_server": "whois.nic.airbus", "extend": "com", "_test": "nic.airbus"}
ZZ["airforce"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["airtel"] = {"_server": "whois.nic.airtel", "extend": "com", "_test": "nic.airtel"}
ZZ["akdn"] = {"_server": "whois.afilias-srs.net", "extend": "com", "_test": "nic.akdn"}
ZZ["al"] = {"extend": "_privateReg"}
ZZ["alibaba"] = {"_server": "whois.nic.alibaba", "extend": "com", "_test": "nic.alibaba"}
ZZ["alipay"] = {"_server": "whois.nic.alipay", "extend": "com", "_test": "nic.alipay"}
ZZ["allfinanz"] = {"_server": "whois.nic.allfinanz", "extend": "com", "_test": "nic.allfinanz"}
ZZ["allstate"] = {"_server": "whois.nic.allstate", "extend": "com", "_test": "nic.allstate"}
ZZ["ally"] = {"_server": "whois.nic.ally", "extend": "com", "_test": "nic.ally"}
ZZ["alsace"] = {"_server": "whois.nic.alsace", "extend": "com", "_test": "nic.alsace"}
ZZ["alstom"] = {"_server": "whois.nic.alstom", "extend": "com", "_test": "nic.alstom"}
ZZ["amazon"] = {"_server": "whois.nic.amazon", "extend": "com", "_test": "nic.amazon"}
ZZ["americanfamily"] = {"_server": "whois.nic.americanfamily", "extend": "com", "_test": "nic.americanfamily"}
ZZ["amfam"] = {"_server": "whois.nic.amfam", "extend": "com", "_test": "nic.amfam"}
ZZ["android"] = {"_server": "whois.nic.android", "extend": "com", "_test": "nic.android"}
ZZ["anquan"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["anz"] = {"_server": "whois.nic.anz", "extend": "com", "_test": "nic.anz"}
ZZ["aol"] = {"_server": "whois.nic.aol", "extend": "com", "_test": "nic.aol"}
ZZ["apartments"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["app"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["apple"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["aquarelle"] = {"_server": "whois.nic.aquarelle", "extend": "com", "_test": "nic.aquarelle"}
ZZ["arab"] = {"_server": "whois.nic.arab", "extend": "com", "_test": "nic.arab"}
ZZ["archi"] = {"_server": "whois.nic.archi", "extend": "com", "_test": "nic.archi"}
ZZ["army"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["arte"] = {"_server": "whois.nic.arte", "extend": "com", "_test": "nic.arte"}
ZZ["art"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["asda"] = {"_server": "whois.nic.asda", "extend": "com", "_test": "nic.asda"}
ZZ["as"] = {"extend": "gg"}
ZZ["asia"] = {"extend": "com"}
ZZ["associates"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["attorney"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["auction"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["audible"] = {"_server": "whois.nic.audible", "extend": "com", "_test": "nic.audible"}
ZZ["audio"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["audi"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["auspost"] = {"_server": "whois.nic.auspost", "extend": "com", "_test": "nic.auspost"}
ZZ["author"] = {"_server": "whois.nic.author", "extend": "com", "_test": "nic.author"}
ZZ["auto"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["autos"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["avianca"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["aw"] = {"extend": "nl", "name_servers": R(r"Domain nameservers.*:\n%s" % xStr(r"(?:\s+(\S+)\n)?", 4))}
ZZ["aws"] = {"_server": "whois.nic.aws", "extend": "com", "_test": "nic.aws"}
ZZ["az"] = {"extend": "_privateReg"}
ZZ["baby"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["ba"] = {"extend": "_privateReg"}
ZZ["baidu"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": "nic.baidu"}
ZZ["band"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["barcelona"] = {"_server": "whois.nic.barcelona", "extend": "com", "_test": "nic.barcelona"}
ZZ["barclaycard"] = {"_server": "whois.nic.barclaycard", "extend": "com", "_test": "nic.barclaycard"}
ZZ["barclays"] = {"_server": "whois.nic.barclays", "extend": "com", "_test": "nic.barclays"}
ZZ["barefoot"] = {"_server": "whois.nic.barefoot", "extend": "com", "_test": "nic.barefoot"}
ZZ["bar"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["bargains"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["basketball"] = {"_server": "whois.nic.basketball", "extend": "com", "_test": "nic.basketball"}
ZZ["bauhaus"] = {"_server": "whois.nic.bauhaus", "extend": "com", "_test": "nic.bauhaus"}
ZZ["bayern"] = {"_server": "whois.nic.bayern", "extend": "com", "_test": "nic.bayern"}
ZZ["bbc"] = {"_server": "whois.nic.bbc", "extend": "com", "_test": "nic.bbc"}
ZZ["bbt"] = {"_server": "whois.nic.bbt", "extend": "com", "_test": "nic.bbt"}
ZZ["bbva"] = {"_server": "whois.nic.bbva", "extend": "com", "_test": "nic.bbva"}
ZZ["bcg"] = {"_server": "whois.nic.bcg", "extend": "com", "_test": "nic.bcg"}
ZZ["bcn"] = {"_server": "whois.nic.bcn", "extend": "com", "_test": "nic.bcn"}
ZZ["bd"] = {"extend": "_privateReg"}  # Bangladesh
ZZ["beats"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["beauty"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["beer"] = {"_server": "whois.nic.beer", "extend": "com", "_test": "nic.beer"}
ZZ["bentley"] = {"_server": "whois.nic.bentley", "extend": "com", "_test": "nic.bentley"}
ZZ["berlin"] = {"_server": "whois.nic.berlin", "extend": "com", "_test": "nic.berlin"}
ZZ["bestbuy"] = {"_server": "whois.nic.bestbuy", "extend": "com", "_test": "nic.bestbuy"}
ZZ["best"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["bet"] = {"extend": "ac", "_server": "whois.nic.bet", "_test": "nic.bet"}
ZZ["bf"] = {"extend": "com", "_server": "whois.nic.bf", "registrant": R(r"Registrant Name:\s?(.+)"), "_test": "nic.bf"}
ZZ["bible"] = {"_server": "whois.nic.bible", "extend": "com", "_test": "nic.bible"}
ZZ["bid"] = {"extend": "ac", "_server": "whois.nic.bid", "_test": "nic.bid"}
ZZ["bike"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["bingo"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["bio"] = {"_server": "whois.nic.bio", "extend": "com", "_test": "nic.bio"}
ZZ["bi"] = {"_server": "whois1.nic.bi", "extend": "com"}
ZZ["blackfriday"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["black"] = {"_server": "whois.nic.black", "extend": "com", "_test": "nic.black"}
ZZ["blockbuster"] = {"_server": "whois.nic.blockbuster", "extend": "com", "_test": "nic.blockbuster"}
ZZ["blog"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["blue"] = {"extend": "com"}
ZZ["bms"] = {"_server": "whois.nic.bms", "extend": "com", "_test": "nic.bms"}
ZZ["bmw"] = {"_server": "whois.nic.bmw", "extend": "com", "_test": "nic.bmw"}
ZZ["bnpparibas"] = {"_server": "whois.nic.bnpparibas", "extend": "com", "_test": "group.bnpparibas"}
ZZ["boats"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["boehringer"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["bofa"] = {"_server": "whois.nic.bofa", "extend": "com", "_test": "nic.bofa"}
ZZ["bom"] = {"extend": "com", "_server": "whois.gtlds.nic.br"}
ZZ["bond"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["book"] = {"_server": "whois.nic.book", "extend": "com", "_test": "nic.book"}
ZZ["boo"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["bosch"] = {"_server": "whois.nic.bosch", "extend": "com", "_test": "nic.bosch"}
ZZ["bostik"] = {"_server": "whois.nic.bostik", "extend": "com", "_test": "nic.bostik"}
ZZ["boston"] = {"_server": "whois.nic.boston", "extend": "com", "_test": "nic.boston"}
ZZ["bot"] = {"_server": "whois.nic.bot", "extend": "com", "_test": "nic.bot"}
ZZ["boutique"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["box"] = {"_server": "whois.nic.box", "extend": "com", "_test": "nic.box"}
ZZ["bradesco"] = {"_server": "whois.nic.bradesco", "extend": "com", "_test": "nic.bradesco"}
ZZ["bridgestone"] = {"_server": "whois.nic.bridgestone", "extend": "com", "_test": "nic.bridgestone"}
ZZ["broadway"] = {"_server": "whois.nic.broadway", "extend": "com", "_test": "nic.broadway"}
ZZ["broker"] = {"_server": "whois.nic.broker", "extend": "com", "_test": "nic.broker"}
ZZ["brother"] = {"_server": "whois.nic.brother", "extend": "com", "_test": "nic.brother"}
ZZ["brussels"] = {"_server": "whois.nic.brussels", "extend": "com", "_test": "nic.brussels"}
ZZ["builders"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["build"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["business"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["buy"] = {"_server": "whois.nic.buy", "extend": "com", "_test": "nic.buy"}
ZZ["buzz"] = {"extend": "amsterdam"}
ZZ["bz"] = {"extend": "_privateReg"}
ZZ["cab"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ca"] = {"extend": "com"}
ZZ["cafe"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["call"] = {"_server": "whois.nic.call", "extend": "com", "_test": "nic.call"}
ZZ["cal"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["camera"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cam"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["camp"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["canon"] = {"_server": "whois.nic.canon", "extend": "com", "_test": "nic.canon"}
ZZ["capetown"] = {"_server": "whois.nic.capetown", "extend": "com", "_test": "nic.capetown"}
ZZ["capital"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["capitalone"] = {"_server": "whois.nic.capitalone", "extend": "com", "_test": "nic.capitalone"}
ZZ["cards"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["career"] = {"_server": "whois.nic.career", "extend": "com", "_test": "nic.career"}
ZZ["careers"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["care"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["car"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["cars"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["casa"] = {"extend": "ac", "registrant_country": R(r"Registrant Country:\s+(.+)")}
ZZ["case"] = {"_server": "whois.nic.case", "extend": "com", "_test": "nic.case"}
ZZ["cash"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["casino"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["catering"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cat"] = {"extend": "com", "_server": "whois.nic.cat", "_test": "nic.cat"}
ZZ["catholic"] = {"_server": "whois.nic.catholic", "extend": "com", "_test": "nic.catholic"}
ZZ["ca.ug"] = {"extend": "ug"}
ZZ["cba"] = {"_server": "whois.nic.cba", "extend": "com", "_test": "nic.cba"}
# ZZ["cbs"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["cd"] = {"extend": "ac", "_server": "whois.nic.cd", "registrant_country": R(r"Registrant\s+Country:\s+(.+)"), "_test": "nic.cd"}
ZZ["center"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ceo"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["cern"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["cfa"] = {"_server": "whois.nic.cfa", "extend": "com", "_test": "nic.cfa"}
ZZ["cfd"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["chanel"] = {"_server": "whois.nic.chanel", "extend": "com", "_test": "nic.chanel"}
ZZ["channel"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["charity"] = {"extend": "_donuts", "_server": "whois.nic.charity", "_test": "nic.charity"}
ZZ["chat"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cheap"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ch"] = {"extend": "_privateReg"}
ZZ["chintai"] = {"_server": "whois.nic.chintai", "extend": "com", "_test": "nic.chintai"}
ZZ["christmas"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["chrome"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["church"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cipriani"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["circle"] = {"_server": "whois.nic.circle", "extend": "com", "_test": "nic.circle"}
ZZ["ci"] = {"_server": "whois.nic.ci", "extend": "com", "_test": "nic.ci"}
# ZZ["cityeats"] = {"_server": "whois.nic.cityeats", "extend": "com", "_test": "nic.cityeats"}
ZZ["city"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["claims"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cleaning"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["click"] = {"extend": "com"}
ZZ["clinic"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["clinique"] = {"_server": "whois.nic.clinique", "extend": "com", "_test": "nic.clinique"}
ZZ["clothing"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cloud"] = {"extend": "com"}
ZZ["club"] = {"extend": "com"}
ZZ["clubmed"] = {"_server": "whois.nic.clubmed", "extend": "com", "_test": "nic.clubmed"}
ZZ["cm"] = {"extend": "com"}
ZZ["coach"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["codes"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["co"] = {"extend": "biz", "status": R(r"Status:\s?(.+)")}
ZZ["coffee"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["co.ke"] = {"extend": "ke"}
ZZ["college"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["cologne"] = {"_server": "whois.ryce-rsp.com", "extend": "com"}
ZZ["com.au"] = {"extend": "au"}
ZZ["com.bd"] = {"extend": "bd"}
ZZ["com.bo"] = {"extend": "bo"}
ZZ["comcast"] = {"_server": "whois.nic.comcast", "extend": "com", "_test": "nic.comcast"}
ZZ["com.cn"] = {"extend": "cn"}
ZZ["com.do"] = {"extend": "_privateReg"}
ZZ["com.ec"] = {"extend": "ec"}
ZZ["com.eg"] = {"extend": "_privateReg"}  # Egipt
ZZ["com.ly"] = {"extend": "ly"}
ZZ["commbank"] = {"_server": "whois.nic.commbank", "extend": "com", "_test": "nic.commbank"}
ZZ["com.mo"] = {"extend": "mo"}
ZZ["community"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["com.np"] = {"extend": "np"}
ZZ["company"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["compare"] = {"_server": "whois.nic.compare", "extend": "com", "_test": "nic.compare"}
ZZ["com.ph"] = {"extend": "ph"}
ZZ["computer"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["com.py"] = {"extend": "_privateReg"}
ZZ["com.ru"] = {"extend": "ru", "_server": "whois.nic.ru", "_test": "mining.com.ru"}
ZZ["comsec"] = {"_server": "whois.nic.comsec", "extend": "com", "_test": "nic.comsec"}
ZZ["com.tm"] = {"extend": "tm", "_privateRegistry": True}
ZZ["com.tw"] = {"extend": "tw"}
ZZ["com.ua"] = {"extend": "ua"}
ZZ["com.ve"] = {"extend": "ve"}
ZZ["com.zw"] = {"extend": "zw"}
ZZ["condos"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["construction"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["consulting"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["contact"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["contractors"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cooking"] = {"_server": "whois.nic.cooking", "extend": "com", "_test": "nic.cooking"}
ZZ["cool"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["coop"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["coop.rw"] = {"extend": "rw"}
ZZ["corsica"] = {"_server": "whois.nic.corsica", "extend": "com", "_test": "nic.corsica"}
ZZ["co.rw"] = {"extend": "rw"}
ZZ["co.ug"] = {"extend": "ug"}
ZZ["country"] = {"_server": "whois.nic.country", "extend": "com", "_test": "nic.country"}
ZZ["coupons"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["courses"] = {"extend": "com"}
ZZ["co.ve"] = {"extend": "ve"}
ZZ["co.za"] = {"extend": "za", "_server": "coza-whois.registry.net.za"}
ZZ["cpa"] = {"_server": "whois.nic.cpa", "extend": "com", "_test": "nic.cpa"}
ZZ["creditcard"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["credit"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["creditunion"] = {"_server": "whois.afilias-srs.net", "extend": "com"}

ZZ["cr"] = {"extend": "cz"}
ZZ["co.cr"] = {"extend": "cr"}

ZZ["cricket"] = {"extend": "com", "_server": "whois.nic.cricket", "_test": "nic.cricket"}
ZZ["cruise"] = {"_server": "whois.nic.cruise", "extend": "com", "_test": "nic.cruise"}
ZZ["cruises"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["cuisinella"] = {"_server": "whois.nic.cuisinella", "extend": "com", "_test": "nic.cuisinella"}
ZZ["cv"] = {"extend": "_privateReg"}  # Cape Verde
ZZ["cw"] = {"extend": "_privateReg"}
ZZ["cx"] = {"extend": "com"}
ZZ["cymru"] = {"_server": "whois.nic.cymru", "extend": "com", "_test": "nic.cymru"}
ZZ["cyou"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["cy"] = {"_privateRegistry": True}
ZZ["dabur"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["dad"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["dance"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["data"] = {"_server": "whois.nic.data", "extend": "com", "_test": "nic.data"}
ZZ["date"] = {"extend": "com", "_server": "whois.nic.date", "_test": "nic.date"}
ZZ["dating"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["datsun"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["day"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["dclk"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["dds"] = {"_server": "whois.nic.dds", "extend": "com", "_test": "nic.dds"}
ZZ["dealer"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["deal"] = {"_server": "whois.nic.deal", "extend": "com", "_test": "nic.deal"}
ZZ["deals"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["degree"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["delivery"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["deloitte"] = {"_server": "whois.nic.deloitte", "extend": "com", "_test": "nic.deloitte"}
ZZ["delta"] = {"_server": "whois.nic.delta", "extend": "com", "_test": "nic.delta"}
ZZ["democrat"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["dental"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["dentist"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["desi"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["design"] = {"extend": "ac"}
ZZ["dev"] = {"extend": "com"}
ZZ["diamonds"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["diet"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["digital"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["direct"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["directory"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["discount"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["dish"] = {"_server": "whois.nic.dish", "extend": "com", "_test": "nic.dish"}
ZZ["diy"] = {"_server": "whois.nic.diy", "extend": "com", "_test": "nic.diy"}
ZZ["dm"] = {"_server": "whois.dmdomains.dm", "extend": "com"}
ZZ["dnp"] = {"_server": "whois.nic.dnp", "extend": "com", "_test": "nic.dnp"}
ZZ["docs"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["doctor"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["do"] = {"extend": "bzh", "_server": "whois.nic.do", "_test": "nic.do"}
ZZ["do"] = {"extend": "_privateReg"}
ZZ["dog"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["domains"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["dot"] = {"_server": "whois.nic.dot", "extend": "com", "_test": "nic.dot"}
ZZ["download"] = {"extend": "amsterdam", "name_servers": R(r"Name Server:[ \t]+(\S+)"), "status": R(r"Domain Status:\s*([a-zA-z]+)")}
ZZ["drive"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["dtv"] = {"_server": "whois.nic.dtv", "extend": "com", "_test": "nic.dtv"}
ZZ["dubai"] = {"_server": "whois.nic.dubai", "extend": "com", "_test": "nic.dubai"}
ZZ["duckdns.org"] = {"extend": "_privateReg"}
ZZ["dunlop"] = {"_server": "whois.nic.dunlop", "extend": "com", "_test": "nic.dunlop"}
ZZ["durban"] = {"_server": "whois.nic.durban", "extend": "com", "_test": "nic.durban"}
ZZ["dvag"] = {"_server": "whois.nic.dvag", "extend": "com", "_test": "nic.dvag"}
ZZ["dvr"] = {"_server": "whois.nic.dvr", "extend": "com", "_test": "nic.dvr"}
ZZ["dz"] = {"extend": "_privateReg"}
ZZ["earth"] = {"_server": "whois.nic.earth", "extend": "com", "_test": "nic.earth"}
ZZ["eat"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["ec"] = {"extend": "_privateReg"}
ZZ["eco"] = {"_server": "whois.nic.eco", "extend": "com", "_test": "nic.eco"}
ZZ["edeka"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ed.jp"] = {"extend": "co.jp"}
ZZ["education"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["edu.tr"] = {"extend": "com.tr", "_server": "whois.trabis.gov.tr", "_test": "anadolu.edu.tr"}
ZZ["edu.ua"] = {"extend": "ua", "creation_date": R(r"\ncreated:\s+0-UANIC\s+(.+)")}
ZZ["eg"] = {"extend": "_privateReg"}  # Egipt
ZZ["email"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["emerck"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["energy"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["engineer"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["engineering"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["enterprises"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["epson"] = {"_server": "whois.nic.epson", "extend": "com", "_test": "nic.epson"}
ZZ["equipment"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ericsson"] = {"_server": "whois.nic.ericsson", "extend": "com", "_test": "nic.ericsson"}
ZZ["erni"] = {"_server": "whois.nic.erni", "extend": "com", "_test": "nic.erni"}
ZZ["es"] = {"extend": "_privateReg"}
ZZ["esq"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["estate"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["et"] = {"extend": "com", "_server": "whois.ethiotelecom.et"}
ZZ["com.et"] = {"extend": "et", "_test": "google.com.et"}
ZZ["etisalat"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["eurovision"] = {"_server": "whois.nic.eurovision", "extend": "com", "_test": "nic.eurovision"}
ZZ["eus"] = {"extend": "ac"}
ZZ["events"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["exchange"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["expert"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["exposed"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["express"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["extraspace"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["fage"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["fail"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fairwinds"] = {"_server": "whois.nic.fairwinds", "extend": "com", "_test": "nic.fairwinds"}
ZZ["faith"] = {"extend": "com", "_server": "whois.nic.faith", "_test": "nic.faith"}
ZZ["family"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fan"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fans"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["farm"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fashion"] = {"extend": "com", "_server": "whois.nic.fashion", "_test": "nic.fashion"}
ZZ["fast"] = {"_server": "whois.nic.fast", "extend": "com", "_test": "nic.fast"}
ZZ["fedex"] = {"_server": "whois.nic.fedex", "extend": "com", "_test": "nic.fedex"}
ZZ["feedback"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["ferrari"] = {"_server": "whois.nic.ferrari", "extend": "com", "_test": "nic.ferrari"}
ZZ["fidelity"] = {"_server": "whois.nic.fidelity", "extend": "com", "_test": "nic.fidelity"}
ZZ["fido"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["film"] = {"_server": "whois.nic.film", "extend": "com", "_test": "nic.film"}
ZZ["final"] = {"_server": "whois.gtlds.nic.br", "extend": "bom"}
ZZ["finance"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["financial"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fire"] = {"_server": "whois.nic.fire", "extend": "com", "_test": "nic.fire"}
ZZ["firestone"] = {"_server": "whois.nic.firestone", "extend": "com", "_test": "nic.firestone"}
ZZ["firmdale"] = {"_server": "whois.nic.firmdale", "extend": "com", "_test": "nic.firmdale"}
ZZ["fish"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fishing"] = {"_server": "whois.nic.fishing", "extend": "com", "_test": "nic.fishing"}
ZZ["fit"] = {"extend": "com"}
ZZ["fitness"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["flights"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["florist"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["flowers"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["fly"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["fm"] = {"extend": "com"}
ZZ["fo"] = {"extend": "com", "registrant": None}
ZZ["foo"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["football"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["forex"] = {"_server": "whois.nic.forex", "extend": "com", "_test": "nic.forex"}
ZZ["forsale"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["forum"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["foundation"] = {"extend": "_donuts", "_server": "whois.nic.foundation", "_test": "nic.foundation"}
ZZ["fox"] = {"_server": "whois.nic.fox", "extend": "com", "_test": "nic.fox"}
ZZ["free"] = {"_server": "whois.nic.free", "extend": "com", "_test": "nic.free"}
ZZ["fresenius"] = {"_server": "whois.nic.fresenius", "extend": "com", "_test": "nic.fresenius"}
ZZ["frl"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["frogans"] = {"_server": "whois.nic.frogans", "extend": "com", "_test": "nic.frogans"}
# ZZ["frontdoor"] = {"_server": "whois.nic.frontdoor", "extend": "com", "_test": "nic.frontdoor"}
ZZ["fujitsu"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["fund"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fun"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["furniture"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["futbol"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["fyi"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ga"] = {"extend": "_privateReg"}
ZZ["gallery"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gallo"] = {"_server": "whois.nic.gallo", "extend": "com", "_test": "nic.gallo"}
ZZ["gallup"] = {"_server": "whois.nic.gallup", "extend": "com", "_test": "nic.gallup"}
ZZ["gal"] = {"_server": "whois.nic.gal", "extend": "com", "_test": "nic.gal"}
ZZ["game"] = {"extend": "amsterdam"}
ZZ["games"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["garden"] = {"extend": "com", "_server": "whois.nic.garden", "_test": "nic.garden"}
ZZ["gay"] = {"extend": "com", "_server": "whois.nic.gay", "_test": "nic.gay"}
ZZ["gbiz"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["gd"] = {"extend": "com"}
ZZ["gdn"] = {"_server": "whois.nic.gdn", "extend": "com", "_test": "nic.gdn"}
ZZ["gea"] = {"_server": "whois.nic.gea", "extend": "com", "_test": "nic.gea"}
ZZ["gent"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["genting"] = {"_server": "whois.nic.genting", "extend": "com", "_test": "nic.genting"}
ZZ["geo.jp"] = {"extend": "co.jp"}
ZZ["george"] = {"_server": "whois.nic.george", "extend": "com", "_test": "nic.george"}
ZZ["ge"] = {"_server": "whois.nic.ge", "extend": "ac", "updated_date": None, "_test": "nic.ge", "registrant": R(r"Registrant:\s*([^\n]*)\n")}
ZZ["gf"] = {"extend": "si", "_server": "whois.mediaserv.net"}
ZZ["ggee"] = {"_server": "whois.nic.ggee", "extend": "com", "_test": "nic.ggee"}
ZZ["gh"] = {"_privateRegistry": True}
ZZ["gift"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["gifts"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gi"] = {"_server": "whois2.afilias-grs.net", "extend": "com"}
ZZ["gives"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["giving"] = {"_server": "whois.nic.giving", "extend": "com", "_test": "nic.giving"}
ZZ["glass"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gle"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["global"] = {"extend": "amsterdam", "name_servers": R(r"Name Server: (.+)")}
ZZ["globo"] = {"_server": "whois.gtlds.nic.br", "extend": "bom"}
ZZ["gl"] = {"_server": "whois.nic.gl", "extend": "com", "_test": "nic.gl"}
ZZ["gmail"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["gmbh"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gmo"] = {"_server": "whois.nic.gmo", "extend": "com", "_test": "nic.gmo"}
ZZ["gmx"] = {"_server": "whois.nic.gmx", "extend": "com", "_test": "nic.gmx"}
ZZ["gob.ec"] = {"extend": "ec"}
ZZ["godaddy"] = {"_server": "whois.nic.godaddy", "extend": "com", "_test": "nic.godaddy"}
ZZ["go.jp"] = {"extend": "co.jp"}
ZZ["go.ke"] = {"extend": "ke"}
ZZ["gold"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["goldpoint"] = {"_server": "whois.nic.goldpoint", "extend": "com", "_test": "nic.goldpoint"}
ZZ["golf"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["goodyear"] = {"_server": "whois.nic.goodyear", "extend": "com", "_test": "nic.goodyear"}
ZZ["google"] = {"_server": "whois.nic.google", "extend": "com", "_test": "nic.google"}
ZZ["goog"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["goo"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["gop"] = {"_server": "whois.nic.gop", "extend": "com", "_test": "nic.gop"}
ZZ["go.th"] = {"extend": "co.th"}
ZZ["got"] = {"_server": "whois.nic.got", "extend": "com", "_test": "nic.got"}
ZZ["gov.bd"] = {"extend": "bd"}
ZZ["gov"] = {"extend": "com"}
ZZ["gov.rw"] = {"extend": "rw"}
ZZ["gov.tr"] = {"extend": "com.tr", "_server": "whois.trabis.gov.tr", "_test": "www.turkiye.gov.tr"}
ZZ["gq"] = {"extend": "ml", "_server": "whois.domino.gq"}
ZZ["graphics"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gratis"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["green"] = {"extend": "com"}
ZZ["gr"] = {"extend": "_privateReg"}
ZZ["gripe"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gr.jp"] = {"extend": "co.jp"}
ZZ["group"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gs"] = {"_server": "whois.nic.gs", "extend": "com", "_test": "nic.gs"}
ZZ["gt"] = {"extend": "_privateReg"}
ZZ["gucci"] = {"_server": "whois.nic.gucci", "extend": "com", "_test": "nic.gucci"}
ZZ["guge"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["guide"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["guitars"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["guru"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["gy"] = {"extend": "com"}
ZZ["hair"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["hamburg"] = {"_server": "whois.nic.hamburg", "extend": "com", "_test": "nic.hamburg"}
ZZ["hangout"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["haus"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["hdfcbank"] = {"_server": "whois.nic.hdfcbank", "extend": "com", "_test": "nic.hdfcbank"}
ZZ["hdfc"] = {"_server": "whois.nic.hdfc", "extend": "com", "_test": "nic.hdfc"}
ZZ["healthcare"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["health"] = {"extend": "com", "_server": "whois.nic.health", "_test": "nic.health"}
ZZ["help"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["helsinki"] = {"_server": "whois.nic.helsinki", "extend": "com", "_test": "nic.helsinki"}
ZZ["here"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["hermes"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["hiphop"] = {"extend": "com", "_server": "whois.nic.hiphop", "_test": "nic.hiphop"}
ZZ["hisamitsu"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["hitachi"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["hiv"] = {"_server": "whois.nic.hiv", "extend": "com", "_test": "nic.hiv"}
ZZ["hkt"] = {"_server": "whois.nic.hkt", "extend": "com", "_test": "nic.hkt"}
ZZ["hn"] = {"extend": "com"}  # Honduras
ZZ["hockey"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["holdings"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["holiday"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["homedepot"] = {"_server": "whois.nic.homedepot", "extend": "com", "_test": "nic.homedepot"}
ZZ["homes"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["honda"] = {"_server": "whois.nic.honda", "extend": "com", "_test": "nic.honda"}
ZZ["hopto.org"] = {"extend": "_privateReg"}  # dynamic dns without any whois
ZZ["horse"] = {"_server": "whois.nic.horse", "extend": "com", "_test": "nic.horse"}
ZZ["hospital"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["host"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["hosting"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["hot"] = {"_server": "whois.nic.hot", "extend": "com", "_test": "nic.hot"}
ZZ["house"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["how"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["ht"] = {"_server": "whois.nic.ht", "extend": "com", "_test": "nic.ht"}
ZZ["hu"] = {"extend": "_privateReg"}
ZZ["hughes"] = {"_server": "whois.nic.hughes", "extend": "com", "_test": "nic.hughes"}
ZZ["hyundai"] = {"_server": "whois.nic.hyundai", "extend": "com", "_test": "nic.hyundai"}
ZZ["ibm"] = {"_server": "whois.nic.ibm", "extend": "com", "_test": "nic.ibm"}
ZZ["icbc"] = {"_server": "whois.nic.icbc", "extend": "com", "_test": "nic.icbc"}
ZZ["ice"] = {"_server": "whois.nic.ice", "extend": "com", "_test": "nic.ice"}
ZZ["icu"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["ie"] = {"extend": "com"}  # Ireland
ZZ["ifm"] = {"_server": "whois.nic.ifm", "extend": "com", "_test": "nic.ifm"}
ZZ["ikano"] = {"_server": "whois.nic.ikano", "extend": "com", "_test": "nic.ikano"}
ZZ["imamat"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["imdb"] = {"_server": "whois.nic.imdb", "extend": "com", "_test": "nic.imdb"}
ZZ["immobilien"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["immo"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["inc"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["industries"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["in"] = {"extend": "com", "_server": "whois.registry.in"}
ZZ["infiniti"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["info"] = {"extend": "com"}
ZZ["info.ke"] = {"extend": "ke"}
ZZ["info.ve"] = {"extend": "ve"}
ZZ["ing"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["ink"] = {"extend": "amsterdam"}
ZZ["institute"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["insurance"] = {"_server": "whois.nic.insurance", "extend": "com", "_test": "nic.insurance"}
ZZ["insure"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["international"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["in.th"] = {"extend": "co.th"}
ZZ["investments"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["io"] = {"extend": "com", "expiration_date": R(r"\nRegistry Expiry Date:\s?(.+)")}
ZZ["irish"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ismaili"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["istanbul"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ist"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["itv"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["jaguar"] = {"_server": "whois.nic.jaguar", "extend": "com", "_test": "nic.jaguar"}
ZZ["java"] = {"_server": "whois.nic.java", "extend": "com", "_test": "nic.java"}
ZZ["jcb"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["jeep"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["je"] = {"extend": "gg"}
ZZ["jetzt"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["jewelry"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["jio"] = {"_server": "whois.nic.jio", "extend": "com", "_test": "nic.jio"}
ZZ["jll"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["jobs"] = {"_server": "whois.nic.jobs", "extend": "com", "_test": "nic.jobs"}
ZZ["joburg"] = {"_server": "whois.nic.joburg", "extend": "com", "_test": "nic.joburg"}
ZZ["jot"] = {"_server": "whois.nic.jot", "extend": "com", "_test": "nic.jot"}
ZZ["joy"] = {"_server": "whois.nic.joy", "extend": "com", "_test": "nic.joy"}
ZZ["juegos"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["juniper"] = {"_server": "whois.nic.juniper", "extend": "com", "_test": "nic.juniper"}
ZZ["kaufen"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["kddi"] = {"_server": "whois.nic.kddi", "extend": "com", "_test": "nic.kddi"}
ZZ["ke"] = {"extend": "com", "_server": "whois.kenic.or.ke"}
ZZ["kerryhotels"] = {"_server": "whois.nic.kerryhotels", "extend": "com", "_test": "nic.kerryhotels"}
ZZ["kerrylogistics"] = {"_server": "whois.nic.kerrylogistics", "extend": "com", "_test": "nic.kerrylogistics"}
ZZ["kerryproperties"] = {"_server": "whois.nic.kerryproperties", "extend": "com", "_test": "nic.kerryproperties"}
ZZ["kfh"] = {"_server": "whois.nic.kfh", "extend": "com", "_test": "nic.kfh"}
ZZ["kia"] = {"_server": "whois.nic.kia", "extend": "com", "_test": "nic.kia"}
ZZ["kids"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ki"] = {"extend": "com", "_server": "whois.nic.ki", "_test": None}  # kiribati never answeres, timout is the normal response
ZZ["kim"] = {"_server": "whois.nic.kim", "extend": "com", "_test": "nic.kim"}
ZZ["kindle"] = {"_server": "whois.nic.kindle", "extend": "com", "_test": "nic.kindle"}
ZZ["kitchen"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["kiwi"] = {"extend": "com"}
ZZ["kn"] = {"extend": "com"}  # Saint Kitts and Nevis
ZZ["koeln"] = {"_server": "whois.ryce-rsp.com", "extend": "com"}
ZZ["komatsu"] = {"_server": "whois.nic.komatsu", "extend": "com", "_test": "nic.komatsu"}
ZZ["kosher"] = {"_server": "whois.nic.kosher", "extend": "com", "_test": "nic.kosher"}
ZZ["krd"] = {"_server": "whois.nic.krd", "extend": "com", "_test": "nic.krd"}
ZZ["kred"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["kuokgroup"] = {"_server": "whois.nic.kuokgroup", "extend": "com", "_test": "nic.kuokgroup"}
ZZ["kyoto"] = {"_server": "whois.nic.kyoto", "extend": "com", "_test": "nic.kyoto"}
ZZ["ky"] = {"_server": "whois.kyregistry.ky", "extend": "com"}
ZZ["lacaixa"] = {"_server": "whois.nic.lacaixa", "extend": "com", "_test": "nic.lacaixa"}
ZZ["la"] = {"extend": "com"}
ZZ["lamborghini"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["lamer"] = {"_server": "whois.nic.lamer", "extend": "com", "_test": "nic.lamer"}
ZZ["lancaster"] = {"_server": "whois.nic.lancaster", "extend": "com", "_test": "nic.lancaster"}
ZZ["land"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["landrover"] = {"_server": "whois.nic.landrover", "extend": "com", "_test": "nic.landrover"}
ZZ["lasalle"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["lat"] = {"extend": "com"}
ZZ["latino"] = {"_server": "whois.nic.latino", "extend": "com", "_test": "nic.latino"}
ZZ["latrobe"] = {"_server": "whois.nic.latrobe", "extend": "com", "_test": "nic.latrobe"}
ZZ["law"] = {"_server": "whois.nic.law", "extend": "com", "_test": "nic.law"}
ZZ["lawyer"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["lb"] = {"_server": "whois.lbdr.org.lb", "extend": "com"}
ZZ["lc"] = {"extend": "com", "_server": "whois2.afilias-grs.net"}
ZZ["lds"] = {"_server": "whois.nic.lds", "extend": "com", "_test": "nic.lds"}
ZZ["lease"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["leclerc"] = {"_server": "whois.nic.leclerc", "extend": "com", "_test": "nic.leclerc"}
ZZ["lefrak"] = {"_server": "whois.nic.lefrak", "extend": "com", "_test": "nic.lefrak"}
ZZ["legal"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["lego"] = {"_server": "whois.nic.lego", "extend": "com", "_test": "nic.lego"}
ZZ["lexus"] = {"_server": "whois.nic.lexus", "extend": "com", "_test": "nic.lexus"}
ZZ["lgbt"] = {"_server": "whois.nic.lgbt", "extend": "com", "_test": "nic.lgbt"}
ZZ["lg.jp"] = {"extend": "co.jp"}
ZZ["lidl"] = {"_server": "whois.nic.lidl", "extend": "com", "_test": "nic.lidl"}
ZZ["li"] = {"extend": "_privateReg"}
ZZ["life"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["lifestyle"] = {"_server": "whois.nic.lifestyle", "extend": "com", "_test": "nic.lifestyle"}
ZZ["lighting"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["like"] = {"_server": "whois.nic.like", "extend": "com", "_test": "nic.like"}
ZZ["limited"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["limo"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["link"] = {"extend": "amsterdam"}
ZZ["lipsy"] = {"_server": "whois.nic.lipsy", "extend": "com", "_test": "nic.lipsy"}
ZZ["live"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["lk"] = {"extend": "_privateReg"}  # Sri Lanka
ZZ["llc"] = {"_server": "whois.nic.llc", "extend": "com", "_test": "nic.llc"}
ZZ["llp"] = {"_server": "whois.nic.llp", "extend": "com", "_test": "nic.llp"}
ZZ["loan"] = {"extend": "com", "_server": "whois.nic.loan", "_test": "nic.loan"}
ZZ["loans"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["locker"] = {"_server": "whois.nic.locker", "extend": "com", "_test": "nic.locker"}
ZZ["locus"] = {"_server": "whois.nic.locus", "extend": "com", "_test": "nic.locus"}
ZZ["lol"] = {"extend": "amsterdam"}
ZZ["london"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["lotte"] = {"_server": "whois.nic.lotte", "extend": "com", "_test": "nic.lotte"}
ZZ["lotto"] = {"_server": "whois.nic.lotto", "extend": "com", "_test": "nic.lotto"}
ZZ["love"] = {"extend": "ac", "registrant_country": R(r"Registrant\s+Country:\s+(.+)")}
ZZ["lplfinancial"] = {"_server": "whois.nic.lplfinancial", "extend": "com", "_test": "nic.lplfinancial"}
ZZ["lpl"] = {"_server": "whois.nic.lpl", "extend": "com", "_test": "nic.lpl"}
ZZ["ls"] = {"extend": "cz", "_server": "whois.nic.ls", "_test": "nic.ls"}
ZZ["ltda"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ltd"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["lundbeck"] = {"_server": "whois.nic.lundbeck", "extend": "com", "_test": "nic.lundbeck"}
ZZ["luxe"] = {"_server": "whois.nic.luxe", "extend": "com", "_test": "nic.luxe"}
ZZ["luxury"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["lviv.ua"] = {"extend": "com"}
ZZ["ly"] = {"extend": "ac", "_server": "whois.nic.ly", "registrant_country": R(r"Registrant\s+Country:\s+(.+)"), "_test": "nic.ly"}
ZZ["madrid"] = {"_server": "whois.nic.madrid", "extend": "com", "_test": "nic.madrid"}
ZZ["ma"] = {"extend": "ac", "_server": "whois.registre.ma", "registrar": R(r"Sponsoring Registrar:\s*(.+)")}
ZZ["maison"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["makeup"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["management"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["mango"] = {"_server": "whois.nic.mango", "extend": "com", "_test": "nic.mango"}
ZZ["man"] = {"_server": "whois.nic.man", "extend": "com", "_test": "nic.man"}
ZZ["map"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["market"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["marketing"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["markets"] = {"_server": "whois.nic.markets", "extend": "com", "_test": "nic.markets"}
ZZ["marriott"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["mba"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["mckinsey"] = {"_server": "whois.nic.mckinsey", "extend": "com", "_test": "nic.mckinsey"}
ZZ["media"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["med"] = {"_server": "whois.nic.med", "extend": "com", "_test": "nic.med"}
ZZ["meet"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["me.ke"] = {"extend": "ke"}
ZZ["melbourne"] = {"_server": "whois.nic.melbourne", "extend": "com", "_test": "nic.melbourne"}
ZZ["meme"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["memorial"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["men"] = {"_server": "whois.nic.men", "extend": "com", "_test": "nic.men"}
ZZ["menu"] = {"_server": "whois.nic.menu", "extend": "com", "_test": "nic.menu"}
ZZ["mg"] = {"extend": "ac", "registrant_country": R(r"Registrant\s+Country:\s+(.+)")}
ZZ["miami"] = {"_server": "whois.nic.miami", "extend": "com", "_test": "nic.miami"}
ZZ["mil.rw"] = {"extend": "rw"}
ZZ["mini"] = {"_server": "whois.nic.mini", "extend": "com", "_test": "nic.mini"}
ZZ["mit"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["mitsubishi"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["mls"] = {"_server": "whois.nic.mls", "extend": "com", "_test": "nic.mls"}
ZZ["mma"] = {"_server": "whois.nic.mma", "extend": "com", "_test": "nic.mma"}
ZZ["mn"] = {"extend": "com"}
ZZ["mn"] = {"extend": "com", "_server": "whois.nic.mn", "_test": "nic.mn"}
ZZ["mobi"] = {"extend": "com", "expiration_date": R(r"\nRegistry Expiry Date:\s?(.+)"), "updated_date": R(r"\nUpdated Date:\s?(.+)")}
ZZ["mobi.ke"] = {"extend": "ke"}
ZZ["mobile"] = {"_server": "whois.nic.mobile", "extend": "com", "_test": "nic.mobile"}
ZZ["moda"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["moe"] = {"extend": "ac", "registrant_country": R(r"Registrant\s+Country:\s+(.+)")}
ZZ["moi"] = {"_server": "whois.nic.moi", "extend": "com", "_test": "nic.moi"}
ZZ["mom"] = {"_server": "whois.nic.mom", "extend": "com", "_test": "nic.mom"}
ZZ["monash"] = {"_server": "whois.nic.monash", "extend": "com", "_test": "nic.monash"}
ZZ["money"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["monster"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["mormon"] = {"_server": "whois.nic.mormon", "extend": "com", "_test": "nic.mormon"}
ZZ["mortgage"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["moscow"] = {"_server": "whois.nic.moscow", "extend": "com", "_test": "nic.moscow"}
ZZ["motorcycles"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["mov"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["movie"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["mp"] = {"extend": "_privateReg"}
ZZ["mq"] = {"extend": "si", "_server": "whois.mediaserv.net"}
ZZ["mr"] = {"_server": "whois.nic.mr", "extend": "com", "_test": "nic.mr"}
ZZ["msk.ru"] = {"extend": "com.ru"}  # test with: mining.msk.ru
# ZZ["ms"] = {"_server": "whois.nic.ms", "extend": "com", "_test": "nic.ms"} # whois.nic.ms does not exist
ZZ["ms"] = {"extend": "_privateReg"}
ZZ["mtn"] = {"_server": "whois.nic.mtn", "extend": "com", "_test": "nic.mtn"}
ZZ["mtr"] = {"_server": "whois.nic.mtr", "extend": "com", "_test": "nic.mtr"}
ZZ["mu"] = {"extend": "bank"}
ZZ["mu"] = {"extend": "bank"}
ZZ["museum"] = {"_server": "whois.nic.museum", "extend": "com", "_test": "nic.museum"}
ZZ["music"] = {"_server": "whois.nic.music", "extend": "com", "_test": "nic.music"}
ZZ["my"] = {"extend": "_privateReg"}
ZZ["mz"] = {"_server": "whois.nic.mz", "extend": "com", "_test": "nic.mz"}
ZZ["nab"] = {"_server": "whois.nic.nab", "extend": "com", "_test": "nic.nab"}
ZZ["nagoya"] = {"_server": "whois.nic.nagoya", "extend": "com", "_test": "nic.nagoya"}
ZZ["name"] = {"extend": "com", "status": R(r"Domain Status:\s?(.+)")}
ZZ["na"] = {"_server": "whois.na-nic.com.na", "extend": "com"}
ZZ["natura"] = {"_server": "whois.gtlds.nic.br", "extend": "bom"}
ZZ["navy"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["nec"] = {"_server": "whois.nic.nec", "extend": "com", "_test": "nic.nec"}
ZZ["ne.jp"] = {"extend": "co.jp"}
ZZ["ne.ke"] = {"extend": "ke"}
ZZ["netbank"] = {"_server": "whois.nic.netbank", "extend": "com", "_test": "nic.netbank"}
ZZ["net.bd"] = {"extend": "bd"}
ZZ["net"] = {"extend": "com"}
ZZ["net.ph"] = {"extend": "ph"}
ZZ["net.rw"] = {"extend": "rw"}
ZZ["net.tr"] = {"extend": "com.tr", "_server": "whois.trabis.gov.tr", "_test": "trt.net.tr"}
ZZ["net.ua"] = {"extend": "ua"}
ZZ["net.ve"] = {"extend": "ve"}
ZZ["network"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["net.za"] = {"extend": "za", "_server": "net-whois.registry.net.za"}
ZZ["new"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["news"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["nextdirect"] = {"_server": "whois.nic.nextdirect", "extend": "com", "_test": "nic.nextdirect"}
ZZ["next"] = {"_server": "whois.nic.next", "extend": "com", "_test": "nic.next"}
ZZ["nexus"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["nf"] = {"_server": "whois.nic.nf", "extend": "com", "_test": "nic.nf"}
ZZ["ngo"] = {"_server": "whois.nic.ngo", "extend": "com", "_test": "nic.ngo"}
ZZ["ng"] = {"_server": "whois.nic.net.ng", "extend": "ac", "registrant_country": R(r"Registrant Country:\s+(.+)")}
ZZ["nhk"] = {"_server": "whois.nic.nhk", "extend": "com", "_test": "nic.nhk"}
ZZ["nico"] = {"_server": "whois.nic.nico", "extend": "com", "_test": "nic.nico"}
ZZ["nikon"] = {"_server": "whois.nic.nikon", "extend": "com", "_test": "nic.nikon"}
ZZ["ninja"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["nissan"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["nissay"] = {"_server": "whois.nic.nissay", "extend": "com", "_test": "nic.nissay"}
ZZ["noip.com"] = {"extend": "_privateReg"}
ZZ["noip.org"] = {"extend": "_privateReg"}
ZZ["nokia"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["norton"] = {"_server": "whois.nic.norton", "extend": "com", "_test": "nic.norton"}
ZZ["nowruz"] = {"_server": "whois.nic.nowruz", "extend": "com", "_test": "nic.nowruz"}
ZZ["now"] = {"_server": "whois.nic.now", "extend": "com", "_test": "nic.now"}
ZZ["nowtv"] = {"_server": "whois.nic.nowtv", "extend": "com", "_test": "nic.nowtv"}
ZZ["np"] = {"extend": "_privateReg"}
ZZ["nra"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["nrw"] = {"extend": "com"}
ZZ["nu"] = {"extend": "se"}
ZZ["obi"] = {"_server": "whois.nic.obi", "extend": "com", "_test": "nic.obi"}
ZZ["observer"] = {"extend": "com", "_server": "whois.nic.observer", "_test": "nic.observer"}
ZZ["okinawa"] = {"_server": "whois.nic.okinawa", "extend": "com", "_test": "nic.okinawa"}
ZZ["olayangroup"] = {"_server": "whois.nic.olayangroup", "extend": "com", "_test": "nic.olayangroup"}
ZZ["olayan"] = {"_server": "whois.nic.olayan", "extend": "com", "_test": "nic.olayan"}
ZZ["ollo"] = {"_server": "whois.nic.ollo", "extend": "com", "_test": "nic.ollo"}
ZZ["omega"] = {"_server": "whois.nic.omega", "extend": "com", "_test": "nic.omega"}
ZZ["om"] = {"_server": "whois.registry.om", "extend": "com", "_test": "registry.om"}
ZZ["one"] = {"extend": "com", "_server": "whois.nic.one", "_test": "nic.one"}
ZZ["ong"] = {"extend": "ac", "registrant_country": R(r"Registrant Country:\s+(.+)")}
ZZ["onl"] = {"extend": "com"}
ZZ["online"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["ooo"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["oracle"] = {"_server": "whois.nic.oracle", "extend": "com", "_test": "nic.oracle"}
ZZ["orange"] = {"_server": "whois.nic.orange", "extend": "com", "_test": "nic.orange"}
ZZ["organic"] = {"_server": "whois.nic.organic", "extend": "com", "_test": "nic.organic"}
ZZ["org.ph"] = {"extend": "ph"}
ZZ["org.rw"] = {"extend": "rw"}
ZZ["org.tr"] = {"extend": "com.tr", "_server": "whois.trabis.gov.tr", "_test": "dergipark.org.tr"}
ZZ["org.ve"] = {"extend": "ve"}
ZZ["org.za"] = {"extend": "za", "_server": "org-whois.registry.net.za"}
ZZ["org.zw"] = {"extend": "zw"}
ZZ["origins"] = {"_server": "whois.nic.origins", "extend": "com", "_test": "nic.origins"}
ZZ["or.jp"] = {"extend": "co.jp"}
ZZ["or.ke"] = {"extend": "ke"}
ZZ["osaka"] = {"_server": "whois.nic.osaka", "extend": "com", "_test": "nic.osaka"}
ZZ["otsuka"] = {"_server": "whois.nic.otsuka", "extend": "com", "_test": "nic.otsuka"}
ZZ["ott"] = {"_server": "whois.nic.ott", "extend": "com", "_test": "nic.ott"}
ZZ["ovh"] = {"extend": "com", "_server": "whois.nic.ovh", "_test": "nic.ovh"}
ZZ["page"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["panasonic"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["pa"] = {"_privateRegistry": True}
ZZ["paris"] = {"_server": "whois.nic.paris", "extend": "com", "_test": "nic.paris"}
ZZ["pars"] = {"_server": "whois.nic.pars", "extend": "com", "_test": "nic.pars"}
ZZ["partners"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["parts"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["party"] = {"extend": "com", "_server": "whois.nic.party", "_test": "nic.party"}
ZZ["pay"] = {"_server": "whois.nic.pay", "extend": "com", "_test": "nic.pay"}
ZZ["pccw"] = {"_server": "whois.nic.pccw", "extend": "com", "_test": "nic.pccw"}
ZZ["pe"] = {"extend": "com", "registrant": R(r"Registrant Name:\s?(.+)"), "admin": R(r"Admin Name:\s?(.+)")}
ZZ["pet"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["phd"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["ph"] = {"extend": "_privateReg"}
ZZ["ph"] = {"extend": "_privateReg"}
ZZ["philips"] = {"_server": "whois.nic.philips", "extend": "com", "_test": "nic.philips"}
ZZ["phone"] = {"_server": "whois.nic.phone", "extend": "com", "_test": "nic.phone"}
ZZ["photo"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["photography"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["photos"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["physio"] = {"_server": "whois.nic.physio", "extend": "com", "_test": "nic.physio"}
ZZ["pics"] = {"extend": "ac"}
ZZ["pictures"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["pid"] = {"_server": "whois.nic.pid", "extend": "com", "_test": "nic.pid"}
ZZ["pink"] = {"_server": "whois.nic.pink", "extend": "com", "_test": "nic.pink"}
ZZ["pin"] = {"_server": "whois.nic.pin", "extend": "com", "_test": "nic.pin"}
ZZ["pioneer"] = {"_server": "whois.nic.pioneer", "extend": "com", "_test": "nic.pioneer"}
ZZ["pizza"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["pk"] = {"extend": "_privateReg"}
ZZ["place"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["play"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["playstation"] = {"_server": "whois.nic.playstation", "extend": "com", "_test": "nic.playstation"}
ZZ["plumbing"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["plus"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["pm"] = {"extend": "re", "_server": "whois.nic.pm", "_test": "nic.pm"}
ZZ["pnc"] = {"_server": "whois.nic.pnc", "extend": "com", "_test": "nic.pnc"}
ZZ["pohl"] = {"_server": "whois.nic.pohl", "extend": "com", "_test": "nic.pohl"}
ZZ["poker"] = {"_server": "whois.nic.poker", "extend": "com", "_test": "nic.poker"}
ZZ["politie"] = {"_server": "whois.nic.politie", "extend": "com", "_test": "nic.politie"}
ZZ["porn"] = {"_server": "whois.nic.porn", "extend": "com", "_test": "nic.porn"}
ZZ["press"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["prime"] = {"_server": "whois.nic.prime", "extend": "com", "_test": "nic.prime"}
ZZ["prod"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["productions"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["pro"] = {"extend": "com", "_server": "whois.nic.pro", "_test": "nic.pro"}
ZZ["prof"] = {"extend": "com", "_server": "whois.nic.google"}
ZZ["progressive"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["promo"] = {"extend": "com", "_server": "whois.nic.promo", "_test": "nic.promo"}
ZZ["properties"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["property"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["protection"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["pr"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ps"] = {"_privateRegistry": True}  # no host can be contacted only http://www.nic.ps
ZZ["pub"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["pwc"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["py"] = {"extend": "_privateReg"}  # Paraguay
ZZ["qa"] = {"_server": "whois.registry.qa", "extend": "com"}
ZZ["qpon"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["quebec"] = {"_server": "whois.nic.quebec", "extend": "com", "_test": "nic.quebec"}
ZZ["quest"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["racing"] = {"extend": "com", "_server": "whois.nic.racing", "_test": "nic.racing"}
ZZ["radio"] = {"extend": "com", "_server": "whois.nic.radio", "_test": "nic.radio"}
ZZ["read"] = {"_server": "whois.nic.read", "extend": "com", "_test": "nic.read"}
ZZ["realestate"] = {"_server": "whois.nic.realestate", "extend": "com", "_test": "nic.realestate"}
ZZ["realty"] = {"_server": "whois.nic.realty", "extend": "com", "_test": "nic.realty"}
ZZ["recipes"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["red"] = {"extend": "com"}
ZZ["redstone"] = {"_server": "whois.nic.redstone", "extend": "com", "_test": "nic.redstone"}
ZZ["redumbrella"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["rehab"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["reise"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["reisen"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["reit"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["reliance"] = {"_server": "whois.nic.reliance", "extend": "com", "_test": "nic.reliance"}
ZZ["ren"] = {"extend": "com", "_server": "whois.nic.ren", "_test": "nic.ren"}
ZZ["rentals"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["rent"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["repair"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["report"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["republican"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["restaurant"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["rest"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["review"] = {"extend": "com", "_server": "whois.nic.review", "_test": "nic.review"}
ZZ["reviews"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["rexroth"] = {"_server": "whois.nic.rexroth", "extend": "com", "_test": "nic.rexroth"}
ZZ["richardli"] = {"_server": "whois.nic.richardli", "extend": "com", "_test": "nic.richardli"}
ZZ["rich"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["ricoh"] = {"_server": "whois.nic.ricoh", "extend": "com", "_test": "nic.ricoh"}
ZZ["ril"] = {"_server": "whois.nic.ril", "extend": "com", "_test": "nic.ril"}
ZZ["rio"] = {"_server": "whois.gtlds.nic.br", "extend": "bom"}
ZZ["rip"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["rocks"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["rodeo"] = {"_server": "whois.nic.rodeo", "extend": "com", "_test": "nic.rodeo"}
ZZ["rogers"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["room"] = {"_server": "whois.nic.room", "extend": "com", "_test": "nic.room"}
ZZ["rsvp"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["rugby"] = {"_server": "whois.nic.rugby", "extend": "com", "_test": "nic.rugby"}
ZZ["ruhr"] = {"_server": "whois.nic.ruhr", "extend": "com", "_test": "nic.ruhr"}
ZZ["run"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["ru.rf"] = {"extend": "ru"}
ZZ["rwe"] = {"_server": "whois.nic.rwe", "extend": "com", "_test": "nic.rwe"}
ZZ["rw"] = {"extend": "com", "_server": "whois.ricta.org.rw"}
ZZ["ryukyu"] = {"_server": "whois.nic.ryukyu", "extend": "com", "_test": "nic.ryukyu"}
ZZ["saarland"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["safe"] = {"_server": "whois.nic.safe", "extend": "com", "_test": "nic.safe"}
ZZ["safety"] = {"_server": "whois.nic.safety", "extend": "com", "_test": "nic.safety"}
ZZ["sale"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["salon"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["samsclub"] = {"_server": "whois.nic.samsclub", "extend": "com", "_test": "nic.samsclub"}
ZZ["samsung"] = {"_server": "whois.nic.samsung", "extend": "com", "_test": "nic.samsung"}
ZZ["sandvikcoromant"] = {"_server": "whois.nic.sandvikcoromant", "extend": "com", "_test": "nic.sandvikcoromant"}
ZZ["sandvik"] = {"_server": "whois.nic.sandvik", "extend": "com", "_test": "nic.sandvik"}
ZZ["sanofi"] = {"_server": "whois.nic.sanofi", "extend": "com", "_test": "nic.sanofi"}
ZZ["sap"] = {"_server": "whois.nic.sap", "extend": "com", "_test": "nic.sap"}
ZZ["sarl"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["save"] = {"_server": "whois.nic.save", "extend": "com", "_test": "nic.save"}
ZZ["saxo"] = {"_server": "whois.nic.saxo", "extend": "com", "_test": "nic.saxo"}
ZZ["sb"] = {"extend": "com", "_server": "whois.nic.net.sb"}
ZZ["sbi"] = {"_server": "whois.nic.sbi", "extend": "com", "_test": "nic.sbi"}
ZZ["sbs"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["sca"] = {"_server": "whois.nic.sca", "extend": "com", "_test": "nic.sca"}
ZZ["scb"] = {"_server": "whois.nic.scb", "extend": "com", "_test": "nic.scb"}
ZZ["schaeffler"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["schmidt"] = {"_server": "whois.nic.schmidt", "extend": "com", "_test": "nic.schmidt"}
ZZ["scholarships"] = {"_server": "whois.nic.scholarships", "extend": "com", "_test": "nic.scholarships"}
ZZ["school"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["schule"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["schwarz"] = {"_server": "whois.nic.schwarz", "extend": "com", "_test": "nic.schwarz"}
ZZ["science"] = {"extend": "com", "_server": "whois.nic.science", "_test": "nic.science"}
ZZ["sc.ke"] = {"extend": "ke"}
ZZ["scot"] = {"_server": "whois.nic.scot", "extend": "com", "_test": "nic.scot"}
ZZ["sc"] = {"_server": "whois2.afilias-grs.net", "extend": "com"}
ZZ["sd"] = {"extend": "com", "_server": "whois.sdnic.sd"}
ZZ["search"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["seat"] = {"_server": "whois.nic.seat", "extend": "com", "_test": "nic.seat"}
ZZ["secure"] = {"_server": "whois.nic.secure", "extend": "com", "_test": "nic.secure"}
ZZ["security"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["seek"] = {"_server": "whois.nic.seek", "extend": "com", "_test": "nic.seek"}
ZZ["select"] = {"_server": "whois.nic.select", "extend": "com", "_test": "nic.select"}
ZZ["한국"] = {"_server": "whois.kr", "extend": "kr"}
ZZ["삼성"] = {"_server": "whois.kr", "extend": "kr"}
ZZ["닷컴"] = {"_server": "whois.nic.xn--mk1bu44c", "extend": "xn--mk1bu44c"}
ZZ["닷넷"] = {"_server": "whois.nic.xn--t60b56a", "extend": "xn--t60b56a"}
ZZ["services"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["seven"] = {"_server": "whois.nic.seven", "extend": "com", "_test": "nic.seven"}
ZZ["sew"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["sex"] = {"_server": "whois.nic.sex", "extend": "com", "_test": "nic.sex"}
ZZ["sexy"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["sfr"] = {"_server": "whois.nic.sfr", "extend": "com", "_test": "nic.sfr"}
ZZ["shangrila"] = {"_server": "whois.nic.shangrila", "extend": "com", "_test": "nic.shangrila"}
ZZ["sharp"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["shaw"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["shell"] = {"_server": "whois.nic.shell", "extend": "com", "_test": "nic.shell"}
ZZ["shia"] = {"_server": "whois.nic.shia", "extend": "com", "_test": "nic.shia"}
ZZ["shiksha"] = {"_server": "whois.nic.shiksha", "extend": "com", "_test": "nic.shiksha"}
ZZ["shoes"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["shop"] = {"extend": "com"}
ZZ["shopping"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["shouji"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["show"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
# ZZ["showtime"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["silk"] = {"_server": "whois.nic.silk", "extend": "com", "_test": "nic.silk"}
ZZ["sina"] = {"_server": "whois.nic.sina", "extend": "com", "_test": "nic.sina"}
ZZ["singles"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["site"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["skin"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["ski"] = {"_server": "whois.nic.ski", "extend": "com", "_test": "nic.ski"}
ZZ["sky"] = {"_server": "whois.nic.sky", "extend": "com", "_test": "nic.sky"}
ZZ["sl"] = {"extend": "com", "_server": "whois.nic.sl", "_test": "nic.sl"}
ZZ["sling"] = {"_server": "whois.nic.sling", "extend": "com", "_test": "nic.sling"}
ZZ["smart"] = {"_server": "whois.nic.smart", "extend": "com", "_test": "nic.smart"}
ZZ["smile"] = {"_server": "whois.nic.smile", "extend": "com", "_test": "nic.smile"}
ZZ["sncf"] = {"_server": "whois.nic.sncf", "extend": "com", "_test": "nic.sncf"}
ZZ["soccer"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["social"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["so"] = {"extend": "com"}
ZZ["softbank"] = {"_server": "whois.nic.softbank", "extend": "com", "_test": "nic.softbank"}
ZZ["software"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["solar"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["solutions"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["sony"] = {"_server": "whois.nic.sony", "extend": "com", "_test": "nic.sony"}
ZZ["soy"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["space"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["spa"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["spb.ru"] = {"extend": "com.ru", "_test": "iac.spb.ru"}
ZZ["sport"] = {"_server": "whois.nic.sport", "extend": "com", "_test": "nic.sport"}
ZZ["spot"] = {"_server": "whois.nic.spot", "extend": "com", "_test": "nic.spot"}
ZZ["sr"] = {"extend": "_privateReg"}
ZZ["srl"] = {"_server": "whois.afilias-srs.net", "extend": "ac", "registrant_country": R(r"Registrant Country:\s+(.+)")}
ZZ["ss"] = {"_server": "whois.nic.ss", "extend": "com", "_test": "nic.ss"}
ZZ["stada"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["star"] = {"_server": "whois.nic.star", "extend": "com", "_test": "nic.star"}
ZZ["statebank"] = {"_server": "whois.nic.statebank", "extend": "com", "_test": "nic.statebank"}
ZZ["stcgroup"] = {"_server": "whois.nic.stcgroup", "extend": "com", "_test": "nic.stcgroup"}
ZZ["stc"] = {"_server": "whois.nic.stc", "extend": "com", "_test": "nic.stc"}
ZZ["stockholm"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["storage"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["store"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["stream"] = {"_server": "whois.nic.stream", "extend": "com", "_test": "nic.stream"}
ZZ["studio"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["study"] = {"extend": "com"}
ZZ["style"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["sucks"] = {"_server": "whois.nic.sucks", "extend": "com", "_test": "nic.sucks"}
ZZ["su"] = {"extend": "ru"}
ZZ["supplies"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["supply"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["support"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["surf"] = {"_server": "whois.nic.surf", "extend": "com", "_test": "nic.surf"}
ZZ["surgery"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["suzuki"] = {"_server": "whois.nic.suzuki", "extend": "com", "_test": "nic.suzuki"}
ZZ["sv"] = {"_privateRegistry": True}
ZZ["swatch"] = {"_server": "whois.nic.swatch", "extend": "com", "_test": "nic.swatch"}
ZZ["swiss"] = {"_server": "whois.nic.swiss", "extend": "com", "_test": "nic.swiss"}
ZZ["sx"] = {"extend": "com", "_server": "whois.sx"}
ZZ["sydney"] = {"_server": "whois.nic.sydney", "extend": "com", "_test": "nic.sydney"}
ZZ["sy"] = {"extend": "com", "_server": "whois.tld.sy", "_test": "tld.sy"}
ZZ["systems"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tab"] = {"_server": "whois.nic.tab", "extend": "com", "_test": "nic.tab"}
ZZ["taipei"] = {"_server": "whois.nic.taipei", "extend": "com", "_test": "nic.taipei"}
ZZ["talk"] = {"_server": "whois.nic.talk", "extend": "com", "_test": "nic.talk"}
ZZ["taobao"] = {"_server": "whois.nic.taobao", "extend": "com", "_test": "nic.taobao"}
ZZ["tatamotors"] = {"_server": "whois.nic.tatamotors", "extend": "com", "_test": "nic.tatamotors"}
ZZ["tatar"] = {"_server": "whois.nic.tatar", "extend": "com", "_test": "nic.tatar"}
ZZ["tattoo"] = {"extend": "_uniregistry", "_server": "whois.uniregistry.net"}
ZZ["tax"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["taxi"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tci"] = {"_server": "whois.nic.tci", "extend": "com", "_test": "nic.tci"}
ZZ["tdk"] = {"_server": "whois.nic.tdk", "extend": "com", "_test": "nic.tdk"}
ZZ["td"] = {"_server": "whois.nic.td", "extend": "ac", "registrant_country": R(r"Registrant Country:\s+(.+)"), "_test": "nic.td"}
ZZ["team"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tech"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["technology"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["temasek"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["tennis"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["teva"] = {"_server": "whois.nic.teva", "extend": "com", "_test": "nic.teva"}
ZZ["tf"] = {"extend": "re", "_server": "whois.nic.tf", "_test": "nic.tf"}
ZZ["thd"] = {"_server": "whois.nic.thd", "extend": "com", "_test": "nic.thd"}
ZZ["theater"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["theatre"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["th"] = {"_server": "whois.thnic.co.th", "extend": "co.th", "_test": "thnic.co.th"}
ZZ["tiaa"] = {"_server": "whois.nic.tiaa", "extend": "com", "_test": "nic.tiaa"}
ZZ["tickets"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["tienda"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tips"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tires"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tirol"] = {"_server": "whois.nic.tirol", "extend": "com", "_test": "nic.tirol"}
ZZ["tk"] = {"extend": "_privateReg"}
ZZ["tl"] = {"extend": "com"}
ZZ["tmall"] = {"_server": "whois.nic.tmall", "extend": "com", "_test": "nic.tmall"}
ZZ["today"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["to"] = {"extend": "_privateReg"}
ZZ["tokyo"] = {"extend": "com", "_server": "whois.nic.tokyo", "_test": "nic.tokyo"}
ZZ["tools"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["top"] = {"extend": "com"}
ZZ["toray"] = {"_server": "whois.nic.toray", "extend": "com", "_test": "nic.toray"}
ZZ["toshiba"] = {"_server": "whois.nic.toshiba", "extend": "com", "_test": "nic.toshiba"}
ZZ["total"] = {"_server": "whois.nic.total", "extend": "com", "_test": "nic.total"}
ZZ["tours"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["town"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["toyota"] = {"_server": "whois.nic.toyota", "extend": "com", "_test": "nic.toyota"}
ZZ["toys"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["trade"] = {"extend": "amsterdam"}
ZZ["trading"] = {"_server": "whois.nic.trading", "extend": "com", "_test": "nic.trading"}
ZZ["training"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["travelersinsurance"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["travelers"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["travel"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["tr"] = {"extend": "_privateReg"}
ZZ["trust"] = {"_server": "whois.nic.trust", "extend": "com", "_test": "nic.trust"}
ZZ["trv"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["tt"] = {"extend": "_privateReg"}
ZZ["tube"] = {"extend": "com", "_server": "whois.nic.tube", "_test": "nic.tube"}
ZZ["tui"] = {"_server": "whois.nic.tui", "extend": "com", "_test": "nic.tui"}
ZZ["tunes"] = {"_server": "whois.nic.tunes", "extend": "com", "_test": "nic.tunes"}
ZZ["tushu"] = {"_server": "whois.nic.tushu", "extend": "com", "_test": "nic.tushu"}
ZZ["tvs"] = {"_server": "whois.nic.tvs", "extend": "com", "_test": "nic.tvs"}
ZZ["ubank"] = {"_server": "whois.nic.ubank", "extend": "com", "_test": "nic.ubank"}
ZZ["ubs"] = {"_server": "whois.nic.ubs", "extend": "com", "_test": "nic.ubs"}
ZZ["unicom"] = {"_server": "whois.nic.unicom", "extend": "com", "_test": "nic.unicom"}
ZZ["university"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["uno"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["uol"] = {"_server": "whois.gtlds.nic.br", "extend": "bom"}
ZZ["ups"] = {"_server": "whois.nic.ups", "extend": "com", "_test": "nic.ups"}
ZZ["us"] = {"extend": "name"}
ZZ["uy"] = {"extend": "_privateReg"}  # Uruguay
ZZ["vacations"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["va"] = {"extend": "_privateReg"}  # This TLD has no whois server.
ZZ["vana"] = {"_server": "whois.nic.vana", "extend": "com", "_test": "nic.vana"}
ZZ["vanguard"] = {"_server": "whois.nic.vanguard", "extend": "com", "_test": "nic.vanguard"}
ZZ["vc"] = {"extend": "com"}
ZZ["vegas"] = {"_server": "whois.nic.vegas", "extend": "com", "_test": "nic.vegas"}
ZZ["ventures"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["verisign"] = {"_server": "whois.nic.verisign", "extend": "com", "_test": "nic.verisign"}
ZZ["vermögensberater"] = {"_server": "whois.nic.xn--vermgensberater-ctb", "extend": "xn--vermgensberater-ctb"}
ZZ["vermögensberatung"] = {"_server": "whois.nic.xn--vermgensberatung-pwb", "extend": "xn--vermgensberatung-pwb"}
ZZ["versicherung"] = {"_server": "whois.nic.versicherung", "extend": "com", "_test": "nic.versicherung"}
ZZ["vet"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["vg"] = {"_server": "whois.nic.vg", "extend": "com", "_test": "nic.vg"}
ZZ["viajes"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["video"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["vig"] = {"extend": "com", "_server": "whois.afilias-srs.net"}
ZZ["vig"] = {"_server": "whois.nic.vig", "extend": "com", "_test": "nic.vig"}
ZZ["viking"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["villas"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["vin"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["vip"] = {"_server": "whois.nic.vip", "extend": "com", "updated_date": None, "_test": "nic.vip"}
ZZ["virgin"] = {"_server": "whois.nic.virgin", "extend": "com", "_test": "nic.virgin"}
ZZ["visa"] = {"_server": "whois.nic.visa", "extend": "com", "_test": "nic.visa"}
ZZ["vision"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["viva"] = {"_server": "whois.nic.viva", "extend": "com", "_test": "nic.viva"}
ZZ["vlaanderen"] = {"_server": "whois.nic.vlaanderen", "extend": "com", "_test": "nic.vlaanderen"}
ZZ["vn"] = {"extend": "_privateReg"}
ZZ["vodka"] = {"_server": "whois.nic.vodka", "extend": "com", "_test": "nic.vodka"}
ZZ["volkswagen"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["volvo"] = {"_server": "whois.nic.volvo", "extend": "com", "_test": "nic.volvo"}
ZZ["vote"] = {"_server": "whois.nic.vote", "extend": "com", "_test": "nic.vote"}
ZZ["voting"] = {"_server": "whois.nic.voting", "extend": "com", "_test": "nic.voting"}
ZZ["voto"] = {"_server": "whois.nic.voto", "extend": "com", "_test": "nic.voto"}
ZZ["voyage"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["vu"] = {"extend": "_privateReg"}  # all dates 1970 , no furter relevant info
ZZ["wales"] = {"_server": "whois.nic.wales", "extend": "com", "_test": "nic.wales"}
ZZ["walmart"] = {"_server": "whois.nic.walmart", "extend": "com", "_test": "nic.walmart"}
ZZ["walter"] = {"_server": "whois.nic.walter", "extend": "com", "_test": "nic.walter"}
ZZ["wang"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": "nic.wang"}
ZZ["wanggou"] = {"_server": "whois.nic.wanggou", "extend": "com", "_test": "nic.wanggou"}
ZZ["watches"] = {"_server": "whois.nic.watches", "extend": "com", "_test": "nic.watches"}
ZZ["watch"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["webcam"] = {"extend": "com", "_server": "whois.nic.webcam", "_test": "nic.webcam"}
ZZ["weber"] = {"_server": "whois.nic.weber", "extend": "com", "_test": "nic.weber"}
ZZ["website"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["web.ve"] = {"extend": "ve"}
ZZ["web.za"] = {"extend": "za", "_server": "web-whois.registry.net.za"}
ZZ["wedding"] = {"_server": "whois.nic.wedding", "extend": "com", "_test": "nic.wedding"}
ZZ["wed"] = {"_server": "whois.nic.wed", "extend": "com", "_test": "nic.wed"}
ZZ["weibo"] = {"_server": "whois.nic.weibo", "extend": "com", "_test": "nic.weibo"}
ZZ["whoswho"] = {"_server": "whois.nic.whoswho", "extend": "com", "_test": "nic.whoswho"}
ZZ["wien"] = {"_server": "whois.nic.wien", "extend": "com", "_test": "nic.wien"}
ZZ["wine"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["win"] = {"extend": "com"}
ZZ["wme"] = {"_server": "whois.nic.wme", "extend": "com", "_test": "nic.wme"}
ZZ["wolterskluwer"] = {"_server": "whois.nic.wolterskluwer", "extend": "com", "_test": "nic.wolterskluwer"}
ZZ["woodside"] = {"_server": "whois.nic.woodside", "extend": "com", "_test": "nic.woodside"}
ZZ["works"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["world"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["wow"] = {"_server": "whois.nic.wow", "extend": "com", "_test": "nic.wow"}
ZZ["wtc"] = {"_server": "whois.nic.wtc", "extend": "com", "_test": "nic.wtc"}
ZZ["wtf"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["xerox"] = {"_server": "whois.nic.xerox", "extend": "com", "_test": "nic.xerox"}
ZZ["xfinity"] = {"_server": "whois.nic.xfinity", "extend": "com", "_test": "nic.xfinity"}
ZZ["xihuan"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["xin"] = {"extend": "com", "_server": "whois.nic.xin", "_test": "nic.xin"}
ZZ["xn--11b4c3d"] = {"_server": "whois.nic.xn--11b4c3d", "extend": "com", "_test": "nic.xn--11b4c3d"}
ZZ["xn--1qqw23a"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--2scrj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--30rr7y"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["xn--3bst00m"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["xn--3ds443g"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["xn--3e0b707e"] = {"_server": "whois.kr", "extend": "kr"}
ZZ["xn--3hcrj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--3pxu8k"] = {"_server": "whois.nic.xn--3pxu8k", "extend": "com", "_test": "nic.xn--3pxu8k"}
ZZ["xn--42c2d9a"] = {"_server": "whois.nic.xn--42c2d9a", "extend": "com", "_test": "nic.xn--42c2d9a"}
ZZ["xn--45br5cyl"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--45brj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--45q11c"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["xn--4gbrim"] = {"_server": "whois.nic.xn--4gbrim", "extend": "com", "_test": "nic.xn--4gbrim"}
ZZ["xn--55qx5d"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--5su34j936bgsg"] = {"_server": "whois.nic.xn--5su34j936bgsg", "extend": "com", "_test": "nic.xn--5su34j936bgsg"}
ZZ["xn--5tzm5g"] = {"_server": "whois.nic.xn--5tzm5g", "extend": "com", "_test": "nic.xn--5tzm5g"}
ZZ["xn--6frz82g"] = {"_server": "whois.nic.xn--6frz82g", "extend": "com", "_test": "nic.xn--6frz82g"}
ZZ["xn--6qq986b3xl"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["xn--80adxhks"] = {"_server": "whois.nic.xn--80adxhks", "extend": "com", "_test": "nic.xn--80adxhks"}
ZZ["xn--80aqecdr1a"] = {"_server": "whois.nic.xn--80aqecdr1a", "extend": "com", "_test": "nic.xn--80aqecdr1a"}
ZZ["xn--80asehdb"] = {"extend": "com"}
ZZ["xn--80asehdb"] = {"_server": "whois.nic.xn--80asehdb", "extend": "com", "_test": "nic.xn--80asehdb"}
ZZ["xn--80aswg"] = {"_server": "whois.nic.xn--80aswg", "extend": "com", "_test": "nic.xn--80aswg"}
ZZ["xn--8y0a063a"] = {"_server": "whois.nic.xn--8y0a063a", "extend": "com", "_test": "nic.xn--8y0a063a"}
ZZ["xn--9dbq2a"] = {"_server": "whois.nic.xn--9dbq2a", "extend": "com", "_test": "nic.xn--9dbq2a"}
ZZ["xn--9et52u"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["xn--9krt00a"] = {"_server": "whois.nic.xn--9krt00a", "extend": "com", "_test": "nic.xn--9krt00a"}
ZZ["xn--b4w605ferd"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["xn--c1avg"] = {"_server": "whois.nic.xn--c1avg", "extend": "com", "_test": "nic.xn--c1avg"}
ZZ["xn--c2br7g"] = {"_server": "whois.nic.xn--c2br7g", "extend": "com", "_test": "nic.xn--c2br7g"}
ZZ["xn--cckwcxetd"] = {"_server": "whois.nic.xn--cckwcxetd", "extend": "com", "_test": "nic.xn--cckwcxetd"}
ZZ["xn--cg4bki"] = {"_server": "whois.kr", "extend": "kr"}
ZZ["xn--clchc0ea0b2g2a9gcd"] = {"_server": "whois.sgnic.sg", "extend": "sg"}
ZZ["xn--czrs0t"] = {"_server": "whois.nic.xn--czrs0t", "extend": "com", "_test": "nic.xn--czrs0t"}
ZZ["xn--czru2d"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["xn--d1alf"] = {"_server": "whois.marnet.mk", "extend": "mk"}
ZZ["xn--e1a4c"] = {"_server": "whois.eu", "extend": "eu"}
ZZ["xn--efvy88h"] = {"_server": "whois.nic.xn--efvy88h", "extend": "com", "_test": "nic.xn--efvy88h"}
ZZ["xn--fhbei"] = {"_server": "whois.nic.xn--fhbei", "extend": "com", "_test": "nic.xn--fhbei"}
ZZ["xn--fiq228c5hs"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["xn--fiq64b"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["xn--fiqs8s"] = {"_server": "whois.cnnic.cn", "extend": "com"}
ZZ["xn--fiqz9s"] = {"_server": "whois.cnnic.cn", "extend": "com"}
ZZ["xn--fjq720a"] = {"_server": "whois.nic.xn--fjq720a", "extend": "com", "_test": "nic.xn--fjq720a"}
ZZ["xn--flw351e"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["xn--fpcrj9c3d"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--fzys8d69uvgm"] = {"_server": "whois.nic.xn--fzys8d69uvgm", "extend": "com", "_test": "nic.xn--fzys8d69uvgm"}
ZZ["xn--gecrj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--h2breg3eve"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--h2brj9c8c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--h2brj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--hxt814e"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["xn--i1b6b1a6a2e"] = {"_server": "whois.nic.xn--i1b6b1a6a2e", "extend": "com", "_test": "nic.xn--i1b6b1a6a2e"}
ZZ["xn--io0a7i"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--j1aef"] = {"_server": "whois.nic.xn--j1aef", "extend": "com", "_test": "nic.xn--j1aef"}
ZZ["xn--j6w193g"] = {"_server": "whois.hkirc.hk", "extend": "hk", "_test": "hkirc.hk"}
ZZ["xn--jlq480n2rg"] = {"_server": "whois.nic.xn--jlq480n2rg", "extend": "com", "_test": "nic.xn--jlq480n2rg"}
ZZ["xn--kcrx77d1x4a"] = {"_server": "whois.nic.xn--kcrx77d1x4a", "extend": "com", "_test": "nic.xn--kcrx77d1x4a"}
ZZ["xn--kprw13d"] = {"extend": "tw", "_test": "google.xn--kprw13d"}
ZZ["xn--kpry57d"] = {"extend": "tw", "_test": "google.xn--kpry57d"}
ZZ["xn--kput3i"] = {"_server": "whois.nic.xn--kput3i", "extend": "com", "_test": "nic.xn--kput3i"}
ZZ["xn--mgb9awbf"] = {"_server": "whois.registry.om", "extend": "om"}
ZZ["xn--mgba7c0bbn0a"] = {"_server": "whois.nic.xn--mgba7c0bbn0a", "extend": "com", "_test": "nic.xn--mgba7c0bbn0a"}
ZZ["xn--mgbaakc7dvf"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["xn--mgbab2bd"] = {"_server": "whois.nic.xn--mgbab2bd", "extend": "com", "_test": "nic.xn--mgbab2bd"}
ZZ["xn--mgbah1a3hjkrd"] = {"_server": "whois.nic.mr", "extend": "mr"}
ZZ["xn--mgbbh1a71e"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--mgbbh1a"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--mgbca7dzdo"] = {"_server": "whois.nic.xn--mgbca7dzdo", "extend": "com", "_test": "nic.xn--mgbca7dzdo"}
ZZ["xn--mgbgu82a"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--mgbi4ecexp"] = {"_server": "whois.nic.xn--mgbi4ecexp", "extend": "com", "_test": "nic.xn--mgbi4ecexp"}
ZZ["xn--mgbt3dhd"] = {"_server": "whois.nic.xn--mgbt3dhd", "extend": "com", "_test": "nic.xn--mgbt3dhd"}
ZZ["xn--mix891f"] = {"_server": "whois.monic.mo", "extend": "mo"}
ZZ["xn--mk1bu44c"] = {"_server": "whois.nic.xn--mk1bu44c", "extend": "com", "_test": "nic.xn--mk1bu44c"}
ZZ["xn--mxtq1m"] = {"_server": "whois.nic.xn--mxtq1m", "extend": "com", "_test": "nic.xn--mxtq1m"}
ZZ["xn--ngbc5azd"] = {"_server": "whois.nic.xn--ngbc5azd", "extend": "com", "_test": "nic.xn--ngbc5azd"}
ZZ["xn--ngbe9e0a"] = {"_server": "whois.nic.xn--ngbe9e0a", "extend": "com", "_test": "nic.xn--ngbe9e0a"}
ZZ["xn--ngbrx"] = {"_server": "whois.nic.xn--ngbrx", "extend": "com", "_test": "nic.xn--ngbrx"}
ZZ["xn--nqv7fs00ema"] = {"_server": "whois.nic.xn--nqv7fs00ema", "extend": "com", "_test": "nic.xn--nqv7fs00ema"}
ZZ["xn--nqv7f"] = {"_server": "whois.nic.xn--nqv7f", "extend": "com", "_test": "nic.xn--nqv7f"}
ZZ["xn--o3cw4h"] = {"_server": "whois.thnic.co.th", "extend": "co.th"}
ZZ["xn--ogbpf8fl"] = {"_server": "whois.tld.sy", "extend": "sy", "_test": "tld.sy"}
ZZ["xn--p1acf"] = {"extend": "com"}
ZZ["xn--p1ai"] = {"extend": "ru"}
ZZ["xn--pssy2u"] = {"_server": "whois.nic.xn--pssy2u", "extend": "com", "_test": "nic.xn--pssy2u"}
ZZ["xn--q9jyb4c"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["xn--qcka1pmc"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["xn--qxa6a"] = {"_server": "whois.eu", "extend": "eu"}
ZZ["xn--rvc1e0am3e"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--s9brj9c"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--ses554g"] = {"_server": "whois.nic.xn--ses554g", "extend": "com", "_test": "nic.xn--ses554g"}
ZZ["xn--t60b56a"] = {"_server": "whois.nic.xn--t60b56a", "extend": "com", "_test": "nic.xn--t60b56a"}
ZZ["xn--tckwe"] = {"_server": "whois.nic.xn--tckwe", "extend": "com", "_test": "nic.xn--tckwe"}
ZZ["xn--tiq49xqyj"] = {"_server": "whois.nic.xn--tiq49xqyj", "extend": "com", "_test": "nic.xn--tiq49xqyj"}
ZZ["xn--unup4y"] = {"_server": "whois.nic.xn--unup4y", "extend": "com", "_test": "nic.xn--unup4y"}
ZZ["xn--vermgensberater-ctb"] = {"_server": "whois.nic.xn--vermgensberater-ctb", "extend": "com", "_test": "nic.xn--vermgensberater-ctb"}
ZZ["xn--vermgensberatung-pwb"] = {"_server": "whois.nic.xn--vermgensberatung-pwb", "extend": "com", "_test": "nic.xn--vermgensberatung-pwb"}
ZZ["xn--vhquv"] = {"_server": "whois.nic.xn--vhquv", "extend": "com", "_test": "nic.xn--vhquv"}
ZZ["xn--vuq861b"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["xn--w4r85el8fhu5dnra"] = {"_server": "whois.nic.xn--w4r85el8fhu5dnra", "extend": "com", "_test": "nic.xn--w4r85el8fhu5dnra"}
ZZ["xn--w4rs40l"] = {"_server": "whois.nic.xn--w4rs40l", "extend": "com", "_test": "nic.xn--w4rs40l"}
ZZ["xn--wgbl6a"] = {"_server": "whois.registry.qa", "extend": "qa", "_test": "registry.qa"}
ZZ["xn--xhq521b"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--xkc2dl3a5ee0h"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["xn--yfro4i67o"] = {"_server": "whois.sgnic.sg", "extend": "sg"}
ZZ["xxx"] = {"_server": "whois.nic.xxx", "extend": "com", "_test": "nic.xxx"}
ZZ["xyz"] = {"extend": "_centralnic", "_server": "whois.nic.xyz", "_test": "nic.xyz"}
ZZ["yachts"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["yamaxun"] = {"_server": "whois.nic.yamaxun", "extend": "com", "_test": "nic.yamaxun"}
ZZ["ye"] = {"extend": "com", "_server": "whois.y.net.ye", "_test": "net.ye"}
ZZ["yodobashi"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["yoga"] = {"_server": "whois.nic.yoga", "extend": "com", "_test": "nic.yoga"}
ZZ["yokohama"] = {"_server": "whois.nic.yokohama", "extend": "com", "_test": "nic.yokohama"}
ZZ["you"] = {"_server": "whois.nic.you", "extend": "com", "_test": "nic.you"}
ZZ["youtube"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["yt"] = {"extend": "re", "_server": "whois.nic.yt", "_test": "nic.yt"}
ZZ["yun"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["za"] = {"extend": "com"}
ZZ["zappos"] = {"_server": "whois.nic.zappos", "extend": "com", "_test": "nic.zappos"}
ZZ["zara"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["zip"] = {"extend": "com", "_server": "whois.nic.zip", "_test": "nic.zip"}
ZZ["zm"] = {"extend": "com"}
ZZ["zone"] = {"extend": "_donuts", "_server": "whois.donuts.co"}
ZZ["zuerich"] = {"extend": "_centralnic", "_server": "whois.centralnic.com"}
ZZ["zw"] = {"extend": "_privateReg"}  # Zimbabwe
ZZ["ευ"] = {"_server": "whois.eu", "extend": "eu"}
ZZ["ею"] = {"_server": "whois.eu", "extend": "eu"}
ZZ["католик"] = {"_server": "whois.nic.xn--80aqecdr1a", "extend": "xn--80aqecdr1a"}
ZZ["ком"] = {"_server": "whois.nic.xn--j1aef", "extend": "xn--j1aef"}
ZZ["мкд"] = {"_server": "whois.marnet.mk", "extend": "mk"}
ZZ["москва"] = {"_server": "whois.nic.xn--80adxhks", "extend": "xn--80adxhks"}
ZZ["онлайн"] = {"extend": "com"}
ZZ["орг"] = {"_server": "whois.nic.xn--c1avg", "extend": "xn--c1avg"}
ZZ["рус"] = {"extend": "com"}
ZZ["рф"] = {"extend": "ru"}
ZZ["сайт"] = {"_server": "whois.nic.xn--80aswg", "extend": "xn--80aswg"}
ZZ["קום"] = {"_server": "whois.nic.xn--9dbq2a", "extend": "xn--9dbq2a"}
ZZ["ابوظبي"] = {"_server": "whois.nic.xn--mgbca7dzdo", "extend": "xn--mgbca7dzdo"}
ZZ["اتصالات"] = {"_server": "whois.centralnic.com", "extend": "_centralnic"}
ZZ["العليان"] = {"_server": "whois.nic.xn--mgba7c0bbn0a", "extend": "xn--mgba7c0bbn0a"}
ZZ["بارت"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["بازار"] = {"_server": "whois.nic.xn--mgbab2bd", "extend": "xn--mgbab2bd"}
ZZ["بھارت"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["بيتك"] = {"_server": "whois.nic.xn--ngbe9e0a", "extend": "xn--ngbe9e0a"}
ZZ["ڀارت"] = {"_server": "whois.registry.in", "extend": "com"}
ZZ["سورية"] = {"_server": "whois.tld.sy", "extend": "sy"}
ZZ["شبكة"] = {"_server": "whois.nic.xn--ngbc5azd", "extend": "xn--ngbc5azd"}
ZZ["عرب"] = {"_server": "whois.nic.xn--ngbrx", "extend": "xn--ngbrx"}
ZZ["عمان"] = {"_server": "whois.registry.om", "extend": "om"}
ZZ["قطر"] = {"_server": "whois.registry.qa", "extend": "qa"}
ZZ["كاثوليك"] = {"_server": "whois.nic.xn--mgbi4ecexp", "extend": "xn--mgbi4ecexp"}
ZZ["كوم"] = {"_server": "whois.nic.xn--fhbei", "extend": "xn--fhbei"}
ZZ["موريتانيا"] = {"_server": "whois.nic.mr", "extend": "mr"}
ZZ["موقع"] = {"_server": "whois.nic.xn--4gbrim", "extend": "xn--4gbrim"}
ZZ["همراه"] = {"_server": "whois.nic.xn--mgbt3dhd", "extend": "xn--mgbt3dhd"}
ZZ["कम"] = {"_server": "whois.nic.xn--11b4c3d", "extend": "xn--11b4c3d"}
ZZ["नट"] = {"_server": "whois.nic.xn--c2br7g", "extend": "xn--c2br7g"}
ZZ["भरत"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["भरत"] = {"_server": "whois.registry.in", "extend": "in"}
# ZZ["भरतम"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["सगठन"] = {"_server": "whois.nic.xn--i1b6b1a6a2e", "extend": "xn--i1b6b1a6a2e"}
ZZ["ভরত"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ভৰত"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ਭਰਤ"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ભરત"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ଭରତ"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["இநதய"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["சஙகபபர"] = {"_server": "whois.sgnic.sg", "extend": "sg"}
ZZ["భరత"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ಭರತ"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["ഭരത"] = {"_server": "whois.registry.in", "extend": "in"}
ZZ["คอม"] = {"_server": "whois.nic.xn--42c2d9a", "extend": "xn--42c2d9a"}  #
ZZ["ไทย"] = {"_server": "whois.thnic.co.th", "extend": "co.th"}
ZZ["アマゾン"] = {"_server": "whois.nic.xn--cckwcxetd", "extend": "xn--cckwcxetd"}
ZZ["グーグル"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["コム"] = {"_server": "whois.nic.xn--tckwe", "extend": "xn--tckwe"}
ZZ["みんな"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["中信"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["中国"] = {"_server": "whois.cnnic.cn", "extend": "xn--fiqs8s"}
ZZ["中國"] = {"_server": "whois.cnnic.cn", "extend": "xn--fiqs8s"}
ZZ["中文网"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["亚马逊"] = {"_server": "whois.nic.xn--jlq480n2rg", "extend": "xn--jlq480n2rg"}
ZZ["企业"] = {"_server": "whois.nic.xn--vhquv", "extend": "xn--vhquv"}
ZZ["佛山"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["信息"] = {"_server": "whois.teleinfo.cn", "extend": "_teleinfo"}
ZZ["八卦"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["公司"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["台湾"] = {"_server": "whois.twnic.net.tw", "extend": "tw", "_test": "google.台湾"}
ZZ["台灣"] = {"_server": "whois.twnic.net.tw", "extend": "tw", "_test": "google.台灣"}
ZZ["商城"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["商店"] = {"_server": "whois.nic.xn--czrs0t", "extend": "xn--czrs0t"}
ZZ["嘉里"] = {"_server": "whois.nic.xn--w4rs40l", "extend": "xn--w4rs40l"}
ZZ["嘉里大酒店"] = {"_server": "whois.nic.xn--w4r85el8fhu5dnra", "extend": "xn--w4r85el8fhu5dnra"}
ZZ["在线"] = {"extend": "_teleinfo", "_server": "whois.teleinfo.cn"}
ZZ["大拿"] = {"_server": "whois.nic.xn--pssy2u", "extend": "xn--pssy2u"}
ZZ["天主教"] = {"_server": "whois.nic.xn--tiq49xqyj", "extend": "xn--tiq49xqyj"}
ZZ["娱乐"] = {"_server": "whois.nic.xn--fjq720a", "extend": "xn--fjq720a"}
ZZ["广东"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["微博"] = {"_server": "whois.nic.xn--9krt00a", "extend": "xn--9krt00a"}
ZZ["慈善"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["我爱你"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["手机"] = {"_server": "whois.nic.xn--kput3i", "extend": "xn--kput3i"}
ZZ["政府"] = {"_server": "whois.nic.xn--mxtq1m", "extend": "xn--mxtq1m"}
ZZ["新加坡"] = {"_server": "whois.sgnic.sg", "extend": "sg"}
ZZ["新闻"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["时尚"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["机构"] = {"_server": "whois.nic.xn--nqv7f", "extend": "xn--nqv7f"}
ZZ["淡马锡"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["游戏"] = {"_server": "whois.nic.xn--unup4y", "extend": "xn--unup4y"}
ZZ["澳門"] = {"_server": "whois.monic.mo", "extend": "mo"}
ZZ["点看"] = {"_server": "whois.nic.xn--3pxu8k", "extend": "xn--3pxu8k"}
ZZ["移动"] = {"_server": "whois.nic.xn--6frz82g", "extend": "xn--6frz82g"}
ZZ["组织机构"] = {"_server": "whois.nic.xn--nqv7fs00ema", "extend": "xn--nqv7fs00ema"}
ZZ["网址"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["网店"] = {"extend": "_gtldKnet", "_server": "whois.gtld.knet.cn", "_test": None}
ZZ["网站"] = {"_server": "whois.nic.xn--5tzm5g", "extend": "xn--5tzm5g"}
ZZ["网络"] = {"_server": "whois.ngtld.cn", "extend": "com", "_test": "ngtld.cn"}
ZZ["联通"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["谷歌"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["集团"] = {"_server": "whois.gtld.knet.cn", "extend": "com", "_test": None}
ZZ["電訊盈科"] = {"_server": "whois.nic.xn--fzys8d69uvgm", "extend": "xn--fzys8d69uvgm"}
ZZ["飞利浦"] = {"_server": "whois.nic.xn--kcrx77d1x4a", "extend": "xn--kcrx77d1x4a"}
ZZ["香格里拉"] = {"_server": "whois.nic.xn--5su34j936bgsg", "extend": "xn--5su34j936bgsg", "_test": "nic.xn--5su34j936bgsg"}
ZZ["香港"] = {"_server": "whois.hkirc.hk", "extend": "hk", "_test": "hkirc.hk"}

# भारतम् xn--h2breg3eve ; still issues with some utf8 strings 2023-08-28 mboot

ZZ["aaa"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["able"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["accenture"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ad"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["aetna"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["aig"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["americanexpress"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["amex"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["amica"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["analytics"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ao"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["aq"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["aramco"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["athleta"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["axa"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["azure"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["banamex"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bananarepublic"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["baseball"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bb"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bh"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bharti"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bing"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bloomberg"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bm"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["booking"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bs"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bt"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["bv"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["calvinklein"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["caravan"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["cbn"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["cbre"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["cg"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["chase"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["cisco"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["citadel"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["citi"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["citic"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ck"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["coupon"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["cu"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["dell"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["dhl"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["discover"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["dj"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["dupont"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["er"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["farmers"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ferrero"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["fk"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["flickr"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["flir"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["food"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ford"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["frontier"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ftr"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gap"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gb"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gm"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gn"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["grainger"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["grocery"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gu"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["guardian"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["gw"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["hbo"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["homegoods"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["homesense"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["hotels"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["hotmail"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["hsbc"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["hyatt"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ieee"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["intuit"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ipiranga"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["itau"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jm"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jmp"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jnj"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jo"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jpmorgan"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["jprs"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["kh"] = {"_privateRegistry": True}  # no whois server found in iana
# ZZ["kinder"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["km"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["kp"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["kpmg"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["kpn"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["kw"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["lanxess"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["lifeinsurance"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["lilly"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["lincoln"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["living"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["lr"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["maif"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["marshalls"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mattel"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mc"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["merckmsd"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mh"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["microsoft"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mil"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mint"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mlb"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["moto"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["msd"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mt"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["mv"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["nba"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ne"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["netflix"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["neustar"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["nfl"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ni"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["nike"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["nr"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ntt"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["office"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["oldnavy"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["open"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pfizer"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pg"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pictet"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["ping"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pn"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pramerica"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["praxi"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["pru"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["prudential"] = {"_privateRegistry": True}  # no whois server found in iana
# ZZ["rocher"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sakura"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sas"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sener"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sj"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["skype"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sohu"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["song"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["staples"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["statefarm"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["sz"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["target"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["tj"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["tjmaxx"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["tjx"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["tkmaxx"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["vi"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["vivo"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["weather"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["weatherchannel"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["williamhill"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["windows"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["winners"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xbox"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--1ck2e1b"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--54b7fta0cc"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--bck1b9a5dre4c"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--cck2b3b"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--czr694b"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--eckvdtc9d"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--fct429k"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--fzc2c9e2c"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--g2xx48c"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--gckr3f0f"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--gk3at1e"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--imr513n"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--jvr189m"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--l1acc"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgba3a3ejt"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgbai9azgqp6j"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgbayh7gpa"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgbc0a9azcg"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgbcpq6gpa1a"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--mgbpl2fh"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--nyqy26a"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--otu796d"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--qxam"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--rhqv96g"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--rovu88b"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--wgbh1c"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["xn--xkc2al3hye2a"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["yahoo"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["yandex"] = {"_privateRegistry": True}  # no whois server found in iana
ZZ["zero"] = {"_privateRegistry": True}  # no whois server found in iana

ZZ["onion"] = {"_privateRegistry": True}  # this is a special case https://tools.ietf.org/html/rfc7686

# 2023-11-14
# unknown tld abb, abb, abb, abb, whois.nic.abb,
ZZ["abb"] = {"_server": "whois.nic.abb", "_test": "nic.abb", "extend": "com"}
# unknown tld bn, bn, bn, bn, whois.bnnic.bn,
ZZ["bn"] = {"_server": "whois.bnnic.bn", "_test": "bnnic.bn", "extend": "com"}
ZZ["gov.bn"] = {"_server": "whois.bnnic.bn", "_test": "egc.gov.bn", "extend": "com"}
# unknown tld bw, bw, bw, bw, whois.nic.net.bw,
ZZ["bw"] = {"_server": "whois.nic.net.bw", "_test": "net.bw", "extend": "com"}
# unknown tld crown, crown, crown, crown, whois.nic.crown,
ZZ["crown"] = {"_server": "whois.nic.crown", "_test": "nic.crown", "extend": "com"}
# unknown tld crs, crs, crs, crs, whois.nic.crs,
ZZ["crs"] = {"_server": "whois.nic.crs", "_test": "nic.crs", "extend": "com"}
# unknown tld fj, fj, fj, fj, www.whois.fj,
ZZ["fj"] = {"_server": "whois.nic.fj", "_test": "nic.fj", "extend": "com"}  # actually not working but server exists (dns)
# unknown tld gp, gp, gp, gp, whois.nic.gp,
ZZ["gp"] = {"_server": "whois.nic.gp", "_test": "nic.gp", "extend": "com"}  # actually not working but server exists (dns)
# unknown tld hm, hm, hm, hm, whois.registry.hm,
ZZ["hm"] = {"_server": "whois.registry.hm", "_test": "registry.hm", "extend": "com"}  # actually not working but server exists (dns)
# unknown tld il, il, il, il, whois.isoc.org.il,
# unknown tld int, int, int, int, whois.iana.org,
ZZ["int"] = {"_server": "whois.iana.org", "_test": "eu.int", "extend": "cz"}

# unknown tld iq, iq, iq, iq, whois.cmc.iq
ZZ["iq"] = {"_server": "whois.cmc.iq", "_test": "cmc.iq", "extend": "com"}
# unknown tld mm, mm, mm, mm, whois.registry.gov.mm
ZZ["mm"] = {"_server": "whois.registry.gov.mm", "_test": "registry.gov.mm", "extend": "com"}
# unknown tld mw, mw, mw, mw, whois.nic.mw,
ZZ["mw"] = {"_server": "whois.nic.mw", "_test": "nic.mw", "extend": "fr"}
# unknown tld post, post, post, post, whois.dotpostregistry.net,
ZZ["post"] = {"_server": "whois.dotpostregistry.net", "_test": "us.post", "extend": "com"}
# unknown tld realtor, realtor, realtor, realtor, whois.nic.realtor,
ZZ["realtor"] = {"_server": "whois.nic.realtor", "_test": "nic.realtor", "extend": "com"}
# unknown tld weir, weir, weir, weir, whois.nic.weir,
ZZ["weir"] = {"_server": "whois.nic.weir", "_test": "nic.weir", "extend": "com"}
