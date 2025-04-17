# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Enumeration to bytes and bytes to enumeration transform."""

from enum import IntEnum
from typing import List, Optional, Tuple, Type

from ._getbytes import getbytes
from ._typing import ByteOrderHint
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform


class EnumX(Transform):

    """Enumeration to bytes and bytes to enumeration transform."""

    __nbytes__: int
    __bdnss__: Tuple[ByteOrderHint, Type[IntEnum], int, bool, bool]

    def __init__(
        self,
        enum: Type[IntEnum],
        nbytes: int = 1,
        byteorder: ByteOrderHint = "little",
        *,
        signed: bool = False,
        strict: bool = True,
        name: Optional[str] = None,
    ) -> None:
        if name is None:
            base_names = ", ".join([b.__name__ for b in enum.__bases__])
            name = f"{enum.__name__} ({base_names})"

        super().__init__(name, hint=enum.__name__)

        assert nbytes > 0
        assert byteorder in {"big", "little"}

        self.__nbytes__ = nbytes
        self.__benss__ = byteorder, enum, nbytes, bool(signed), bool(strict)

    @property
    def byteorder(self) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        byteorder, _enum, _nbytes, _signed, _strict = self.__benss__
        return byteorder

    @property
    def enum(self) -> Type[IntEnum]:
        """Enumeration."""
        _byteorder, enum, _nbytes, _signed, _strict = self.__benss__
        return enum

    @property
    def signed(self) -> bool:
        """Signed integer."""
        _byteorder, _enum, _nbytes, signed, _strict = self.__benss__
        return signed

    @property
    def strict(self) -> bool:
        """Values to pack/unpack must be an enumeration member."""
        _byteorder, _enum, _nbytes, _signed, strict = self.__benss__
        return strict

    def __pack__(
        self, value: int, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        byteorder, enum, nbytes, signed, strict = self.__benss__

        try:
            try:
                value = enum(value)
            except ValueError:
                if strict:
                    raise

            piece = int.to_bytes(value, nbytes, byteorder, signed=signed)
        except Exception:
            if dump is not None:
                # use repr in case str or something that otherwise looks like an int
                dump.value = repr(value)
            raise

        if dump is not None:
            dump.value = value
            dump.memory = piece

        pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[int, int]:
        byteorder, enum, nbytes, signed, strict = self.__benss__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            value = int.from_bytes(buffer[offset:end], byteorder, signed=signed)

            try:
                return enum(value), end
            except ValueError:
                if strict:
                    raise
        else:
            piece, end = getbytes(buffer, offset, dump, nbytes)

            value = int.from_bytes(piece, byteorder, signed=signed)

            try:
                value = enum(value)
            except ValueError:
                if strict:
                    raise
            finally:  # pragma: no cover (coverage tool anomaly)
                dump.value = value

        return value, end

    def __call__(self, value: int) -> int:
        _byteorder, enum, _nbytes, _signed, strict = self.__benss__

        if strict:
            return enum(value)

        try:
            return enum(value)
        except ValueError:
            return value
