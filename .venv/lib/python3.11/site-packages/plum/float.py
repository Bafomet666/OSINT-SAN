# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Float to bytes and bytes to float transform."""

from numbers import Real
from struct import Struct
from typing import List, Optional, Tuple

from ._getbytes import getbytes
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform
from .view import NumberView


FORMAT_CODES = {2: "e", 4: "f", 8: "d"}
ENDIAN_CODES = {"big": ">", "little": "<"}
DEFAULT_NAMES = {2: "half float", 4: "single float", 8: "double float"}


class FloatView(NumberView, Real):

    """Float type view."""

    def __float__(self):
        return NumberView.unpack(self)


class FloatX(Transform):

    """Float to bytes and bytes to float transform."""

    def __init__(
        self,
        nbytes: int,
        byteorder: str = "little",
        name: Optional[str] = None,
    ) -> None:
        assert nbytes in [2, 4, 8]
        assert byteorder in {"big", "little"}

        if name is None:
            name = DEFAULT_NAMES[nbytes]

        super().__init__(name, hint="float")

        self.__nbytes__ = nbytes

        struct = Struct(ENDIAN_CODES[byteorder] + FORMAT_CODES[nbytes])

        self.__byteorder__ = byteorder
        self.__p__ = struct.pack
        self.__nu__ = nbytes, struct.unpack

    @property
    def byteorder(self) -> str:
        """Byte order ("little" or "big")."""
        return self.__byteorder__

    def __pack__(
        self, value: float, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        if dump is None:
            pieces.append(self.__p__(value))
        else:
            dump.value = value

            piece = self.__p__(value)

            dump.memory = piece

            pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[float, int]:
        nbytes, unpack = self.__nu__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            return unpack(buffer[offset:end])[0], end

        chunk, offset = getbytes(buffer, offset, dump, nbytes)

        value = dump.value = unpack(chunk)[0]

        return value, offset

    def __view__(self, buffer: bytearray, offset: int = 0) -> FloatView:
        """Create view of float in bytes buffer."""
        return FloatView(self, buffer, offset)
