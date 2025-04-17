# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Utility functions."""

from typing import Tuple, Union

from .dump import Record
from .exceptions import InsufficientMemoryError


def getbytes(
    buffer: bytes, offset: int, dump: Record, nbytes: Union[int, None] = None
) -> Tuple[bytes, int]:
    """Get bytes from buffer (get remainder in buffer if nbytes is None)."""
    if nbytes is None:
        chunk = bytes(buffer[offset:])

        offset += len(chunk)

        dump.memory = chunk

    else:
        start = offset
        offset += nbytes
        chunk = bytes(buffer[start:offset])

        if len(chunk) < nbytes:
            dump.value = "<insufficient bytes>"
            if len(chunk) > 16:
                dump.add_extra_bytes("", chunk)
            else:
                dump.memory = chunk

            extra = f" {dump.fmt}" if dump.fmt else ""

            unpack_shortage = (
                f"{nbytes - len(chunk)} too few bytes to unpack{extra}"
                f", {nbytes} needed, only {len(chunk)} available"
            )

            raise InsufficientMemoryError(unpack_shortage)

        dump.memory = chunk

    return chunk, offset
