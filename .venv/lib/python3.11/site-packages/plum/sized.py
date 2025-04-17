# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized object to bytes and bytes to sized object transform."""

from typing import Any, List, Optional, Tuple

from ._getbytes import getbytes
from ._typing import Format
from .int import IntX
from .dump import Record
from .exceptions import ExcessMemoryError, InsufficientMemoryError
from .transform import Transform


class SizedX(Transform):

    """Sized object to bytes and bytes to sized object transform.

    :param fmt: object format
    :param size_fmt: size format
    :param int ratio: number of bytes per increment of size member
    :param int offset: difference in size (in bytes)
    :param size_access: dump access description for size

    """

    __forss__: Tuple[Format, int, float, str, IntX]

    def __init__(
        self,
        fmt: Format,
        size_fmt: IntX,
        ratio: float = 1,
        offset: int = 0,
        size_access: str = "--size--",
        name: Optional[str] = None,
    ) -> None:
        # pylint: disable=too-many-arguments
        hint = fmt.__hint__

        if name is None:
            name = f"sized: {hint}"

        super().__init__(name, hint)

        self.__forss__ = fmt, offset, ratio, size_access, size_fmt

    @property
    def fmt(self) -> Format:
        """Sized object format."""
        return self.__forss__[0]

    @property
    def offset(self) -> int:
        """Difference in size (in bytes)."""
        return self.__forss__[1]

    @property
    def ratio(self) -> float:
        """Number of bytes per increment of size."""
        return self.__forss__[2]

    @property
    def size_access(self) -> str:
        """Description to list in access column for size (e.g. "--size--")."""
        return self.__forss__[3]

    @property
    def size_fmt(self) -> IntX:
        """Size format."""
        return self.__forss__[4]

    def __pack__(
        self, value: Any, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        fmt, offset, ratio, size_access, size_fmt = self.__forss__

        if dump is None:
            size_record = None
            object_record = None
        else:
            size_record = dump.add_record(access=size_access, fmt=size_fmt)
            object_record = dump.add_record(fmt=fmt)

        object_pieces: List[bytes] = []

        try:
            fmt.__pack__(value, object_pieces, object_record)
        finally:
            if dump is not None and object_record is not None:
                dump += object_record[:]
                object_record[:] = []

        size = int(len(b"".join(object_pieces)) // ratio) + offset

        size_fmt.__pack__(size, pieces, size_record)

        pieces += object_pieces

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[Any, int]:
        # pylint: disable=too-many-locals
        fmt, size_offset, ratio, size_access, size_fmt = self.__forss__

        if dump is None:
            size_record = None
            object_record = None
        else:
            size_record = dump.add_record(access=size_access, fmt=size_fmt)
            object_record = dump.add_record(fmt=fmt)

        size, offset = size_fmt.__unpack__(buffer, offset, size_record)

        nbytes = int((size - size_offset) * ratio)
        end = offset + nbytes

        object_buffer = buffer[:end]

        try:
            if len(object_buffer) < end:
                if object_record is None:
                    # cause redo with dump to use getbytes() to make dump informative
                    raise InsufficientMemoryError("not enough buffer bytes")

                getbytes(buffer, offset, object_record, nbytes)

            value, offset = fmt.__unpack__(object_buffer, offset, object_record)

            extra_bytes = object_buffer[offset:]

            if extra_bytes:
                if object_record is not None:
                    for i in range(0, len(extra_bytes), 16):
                        if i:
                            object_record.add_record(memory=extra_bytes[i : i + 16])
                        else:
                            object_record.add_record(
                                separate=True,
                                value="<excess bytes>",
                                memory=extra_bytes[i : i + 16],
                            )

                raise ExcessMemoryError(extra_bytes)

        finally:
            if dump is not None and object_record is not None:  # pragma: no cover
                dump += object_record[:]
                object_record[:] = []

        return value, offset
