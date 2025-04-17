# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Utility functions."""

from typing import Any, List, Tuple

from ._getbytes import getbytes  # pylint: disable=unused-import
from .data import Data, DataMeta
from .dump import Dump
from .exceptions import (
    ExcessMemoryError,
    ImplementationError,
    PackError,
    SizeError,
    UnpackError,
)
from .items import calcsize as _calcsize, items, ItemsFormat
from .transform import Transform

getbytes.__module__ = "plum"


def calcsize(fmt: ItemsFormat) -> int:
    """Calculate format size (raise SizeError if variably sized)."""
    if isinstance(fmt, DataMeta):
        nbytes = getattr(fmt, "__nbytes__")

    elif isinstance(fmt, (Data, Transform)):
        nbytes = fmt.nbytes

    else:
        nbytes = _calcsize(fmt)

    if nbytes is None:
        raise SizeError("size varies")

    return nbytes


def pack(value: Any, fmt: ItemsFormat = None) -> bytes:
    """Pack value as formatted bytes.

    :raises: ``PackError`` if type error, value error, etc.

    """
    pieces: List[bytes] = []
    try:
        # None -> dump
        items.__pack__(value, pieces, None, fmt)
    except Exception as exc:
        # do it over to include dump in exception message
        pack_and_dump(value, fmt)

        raise ImplementationError() from exc  # pragma: no cover

    return b"".join(pieces)


def pack_and_dump(value: Any, fmt: ItemsFormat = None) -> Tuple[bytes, Dump]:
    """Pack value as formatted bytes and produce bytes summary.

    :raises: ``PackError`` if type error, value error, etc.

    """
    dump = Dump()
    pieces: List[bytes] = []
    try:
        # empty record added so so pack always called with a Record instance
        items.__pack__(value, pieces, dump.add_record(), fmt)

    except Exception as exc:
        dump.trim_blank_record()
        raise PackError(dump=dump, exception=exc) from exc

    dump.trim_blank_record()

    return b"".join(pieces), dump


def unpack(fmt: ItemsFormat, buffer: bytes) -> Any:
    """Unpack value from formatted bytes.

    :raises: ``UnpackError`` if insufficient bytes or value error

    """
    try:
        # None -> dump
        value, offset = items.__unpack__(buffer, 0, None, fmt)
        if buffer[offset:]:
            raise ExcessMemoryError("too many bytes, retry with dump to follow")
    except Exception as exc:
        # do it over to include dump in exception message
        unpack_and_dump(fmt, buffer)
        raise ImplementationError() from exc  # pragma: no cover

    return value


def unpack_and_dump(fmt: ItemsFormat, buffer: bytes):
    """Unpack value from formatted bytes and produce a packed bytes summary.

    :raises: ``UnpackError`` if insufficient bytes or value error

    """
    dump = Dump()

    try:
        # empty record added so so pack always called with a Record instance
        dump_record = dump.add_record()

        value, offset = items.__unpack__(buffer, 0, dump_record, fmt)

        extra_bytes = buffer[offset:]

        if extra_bytes:

            for i in range(0, len(extra_bytes), 16):

                record = dump_record.add_record(memory=extra_bytes[i : i + 16])

                if not i:
                    record.separate = True

                    record.value = "<excess bytes>"

            raise ExcessMemoryError(extra_bytes)

    except Exception as exc:
        dump.trim_blank_record()
        raise UnpackError(dump, exc) from exc

    dump.trim_blank_record()

    return value, dump
