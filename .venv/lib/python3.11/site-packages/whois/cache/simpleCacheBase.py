#! /usr/bin/env python3

import time

# import sys
import os
import logging

from typing import (
    Dict,
    Optional,
    Tuple,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class SimpleCacheBase:
    def __init__(
        self,
        verbose: bool = False,
        cacheMaxAge: int = (60 * 60 * 48),
    ) -> None:
        self.verbose = verbose
        self.memCache: Dict[str, Tuple[float, str]] = {}
        self.cacheMaxAge: int = cacheMaxAge

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        # store the currentTime and data tuple (time, data)
        self.memCache[keyString] = (
            int(time.time()),
            data,
        )
        return data

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        cData = self.memCache.get(keyString)
        if cData is None:
            return None

        t = time.time()
        hasExpired = cData[0] < (t - self.cacheMaxAge)
        if hasExpired is True:
            return None

        return cData[1]


if __name__ == "__main__":
    pass
