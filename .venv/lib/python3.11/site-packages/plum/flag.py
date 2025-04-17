# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Integer flag to bytes and bytes to integer flag transform."""

from enum import IntFlag
from typing import List, Optional, Tuple, Type

from ._getbytes import getbytes
from ._typing import ByteOrderHint
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform


class FlagX(Transform):

    """Flag Enumeration to bytes and bytes to flag enumeration transform."""

    __ben__: Tuple[ByteOrderHint, Type[IntFlag], int]

    def __init__(
        self,
        enum: Type[IntFlag],
        nbytes: int,
        byteorder: ByteOrderHint = "little",
        name: Optional[str] = None,
    ) -> None:
        if name is None:
            base_names = ", ".join([b.__name__ for b in enum.__bases__])
            name = f"{enum.__name__} ({base_names})"

        super().__init__(name, hint=enum.__name__)

        assert nbytes > 0
        assert byteorder in {"big", "little"}

        self.__nbytes__ = nbytes
        self.__ben__ = byteorder, enum, nbytes

    @property
    def byteorder(self) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        byteorder, _enum, _nbytes = self.__ben__
        return byteorder

    @property
    def enum(self) -> Type[IntFlag]:
        """Integer flag enumeration."""
        _byteorder, enum, _nbytes = self.__ben__
        return enum

    def __pack__(
        self, value: int, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        byteorder, _enum, nbytes = self.__ben__

        if dump is None:
            pieces.append(int.to_bytes(value, nbytes, byteorder, signed=False))
        else:
            try:
                int_value = int(value)
                piece = int.to_bytes(int_value, nbytes, byteorder, signed=False)

                dump.memory = piece

                self._add_flags_to_dump(int_value, dump)

            except Exception:
                # use repr in case str or something that otherwise looks like an int
                dump.value = repr(value)
                raise

            pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[IntFlag, int]:
        byteorder, enum, nbytes = self.__ben__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            return (
                enum(int.from_bytes(buffer[offset:end], byteorder, signed=False)),
                end,
            )

        piece, offset = getbytes(buffer, offset, dump, nbytes)

        int_value = int.from_bytes(piece, byteorder, signed=False)

        value = enum(int_value)

        dump.value = value

        self._add_flags_to_dump(int_value, dump)

        return value, offset

    def _add_flags_to_dump(self, value: int, dump: Record) -> None:
        _byteorder, enum, _nbytes = self.__ben__

        dump.value = value

        for member in enum:
            member_name = member.name or "unlikely"  # mypy thinks it might be None
            dump.add_record(
                access=member_name,
                bits=(int(member.bit_length() - 1), 1),
                value=bool(value & member),
                fmt="bool",
            )
