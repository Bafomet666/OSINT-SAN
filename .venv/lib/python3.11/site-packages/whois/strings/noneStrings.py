import os
import logging

from typing import (
    List,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


NONESTRINGS: List[str] = [
    "the domain has not been registered",
    "no match found for",
    "no matching record",
    "no match",
    "not found",
    "no data found",
    "no entries found",
    # "status: free", # we should not interprete the result if there is a result
    "no such domain",
    "the queried object does not exist",
    "domain you requested is not known",
    # "status: available", # we should not interprete the result if there is a result
    "no whois server is known for this kind of object",
    "nameserver not found",
    "malformed request",  # this means this domain is not in whois as it is on top of a registered domain
    "registration of this domain is restricted",
    "restricted",
    "this domain is currently available",
    "el dominio no se encuentra registrado",
    "generic",
]


def NoneStrings() -> List[str]:
    return NONESTRINGS


def NoneStringsAdd(aString: str) -> None:
    if aString and isinstance(aString, str) and len(aString) > 0:
        NONESTRINGS.append(aString)
