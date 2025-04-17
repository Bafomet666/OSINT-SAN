__copyright__ = "Copyright (c) 2018-2024 Alex Laird"
__license__ = "MIT"

import logging
import shlex
from typing import Optional


class NgrokLog:
    """
    An object containing a parsed log from the ``ngrok`` process.
    """

    def __init__(self,
                 line: str) -> None:
        #: The raw, unparsed log line.
        self.line: str = line.strip()

        #: The log's ISO 8601 timestamp.
        self.t: Optional[str] = None
        #: The log's level.
        self.lvl: str = "NOTSET"
        #: The log's message.
        self.msg: Optional[str] = None
        #: The log's error, if applicable.
        self.err: Optional[str] = None
        #: The log's type.
        self.obj: Optional[str] = None
        #: The URL, if ``obj`` is "web".
        self.addr: Optional[str] = None

        try:
            split = shlex.split(self.line)
        except ValueError:
            split = []

        for i in split:
            if "=" not in i:
                continue

            key, value = i.split("=", 1)

            if key == "lvl":
                if not value:
                    value = self.lvl

                value = value.upper()
                if value == "CRIT":
                    value = "CRITICAL"
                elif value in ["ERR", "EROR"]:
                    value = "ERROR"
                elif value == "WARN":
                    value = "WARNING"

                if not hasattr(logging, value):
                    value = self.lvl

            setattr(self, key, value)

    def __repr__(self) -> str:
        return f"<NgrokLog: t={self.t} lvl={self.lvl} msg=\"{self.msg}\">"

    def __str__(self) -> str:  # pragma: no cover
        attrs = [attr for attr in dir(self) if not attr.startswith("_") and getattr(self, attr) is not None]
        attrs.remove("line")

        return " ".join(f"{attr}=\"{getattr(self, attr)}\"" for attr in attrs)
