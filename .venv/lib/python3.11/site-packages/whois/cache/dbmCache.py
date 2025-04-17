# import sys
import dbm
import os
import logging

from typing import (
    Optional,
)

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class DBMCache:
    def __init__(
        self,
        dbmFile: str,
        verbose: bool = False,
    ) -> None:
        self.verbose = verbose
        self.dbmFile = dbmFile

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        msg = f"{type(self).__name__} get: {keyString}"
        log.debug(msg)

        with dbm.open(self.dbmFile, "c") as db:
            data = db.get(keyString, None)
            if data:
                sdata: str = data.decode("utf-8")
                msg = f"{sdata}"
                log.debug(msg)
                return sdata
        return None

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        msg = f"{type(self).__name__} put: {keyString}"
        log.debug(msg)

        with dbm.open(self.dbmFile, "c") as db:
            db[keyString] = bytes(data, "utf-8")

        return data
