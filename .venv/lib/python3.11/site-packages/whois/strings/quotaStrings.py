import os
import logging

from typing import (
    List,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

QUOTASTRINGS: List[str] = [
    "limit exceeded",
    "quota exceeded",
    "try again later",
    "please try again",
    "exceeded the maximum allowable number",
    "can temporarily not be answered",
    "please try again.",
    "queried interval is too short",
    "number of allowed queries exceeded",
]


def QuotaStrings() -> List[str]:
    return QUOTASTRINGS


def QuotaStringsAdd(aString: str) -> None:
    if aString and isinstance(aString, str) and len(aString) > 0:
        QUOTASTRINGS.append(aString)
