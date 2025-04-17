import os
import logging


from typing import (
    List,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

IGNORESTRINGS: List[str] = [
    "<data not disclosed>",
    "Contact Privacy Inc. Customer",
    "Data Protected",
    "Domain Privacy Trustee SA",
    "Domains By Proxy, LLC",
    "Data Privacy Protected",
    "Domain Privacy Service FBO Registrant",
    "Domain Privacy Service FBO Registrant.",  # may be removed
    "Domain Privacy Trustee",
    "Domain Protection Services",
    "hidden",
    "Identity Protect Limited",
    "Identity Protection Service",
    "Jewella Privacy LLC Privacy ID#",
    "MyPrivacy.net",
    "NameBrightPrivacy.com",  # this may also suppress domain info
    "NO FORMAT!",
    "None",
    "Not Disclosed",
    "Not shown, please visit www.dnsbelgium.be for webbased whois.",
    "[PRIVATE]",
    "Privacy Protection",  # generic, all Whosis Privacy Protection can be removed
    "PrivacyGuardian.org llc",
    "Privacy service provided by Withheld for Privacy ehf",
    "REDACTED FOR PRIVACY",
    "Redacted for ",  # generic , the next 3 can be removed
    "Redacted for GDPR privacy",
    "Redacted for Privacy",
    "Redacted for Privacy Purposes",
    "Statutory Masking Enabled",
    "See PrivacyGuardian.org",
    "Super domains privacy",
    "Whois Privacy",  # generic, the next 5 can be removed
    "Whois Privacy Protection Foundation",
    "Whois Privacy Protection Service",
    "Whois Privacy Protection Service by VALUE-DOMAIN",
    "Whois Privacy Protection Service by onamae.com",
    "Whois Privacy Service",
    "Whoisprotection.cc",
    "Withheld for Privacy Purposes",
]


def IgnoreStrings() -> List[str]:
    return IGNORESTRINGS


def IgnoreStringsAdd(aString: str) -> None:
    if aString and isinstance(aString, str) and len(aString) > 0:
        IGNORESTRINGS.append(aString)
