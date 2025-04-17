# import sys
import os
import logging

from typing import (
    Optional,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class DummyCache:
    def __init__(
        self,
        verbose: bool = False,
    ) -> None:
        self.verbose = verbose

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        return None

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        return data
