# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Object to bytes and bytes to Object transform."""

from typing import Any, Callable, List, Optional, Tuple

from ._getbytes import getbytes
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform


PackType = Callable[[Any], bytes]
UnpackType = Callable[[bytes], Any]


class ObjectX(Transform):

    """Object to bytes and bytes to object transform."""

    __nbytes__: int
    __npu__: Tuple[int, PackType, UnpackType]

    def __init__(
        self,
        pack: PackType,
        unpack: UnpackType,
        nbytes: int,
        name: str = "object",
        hint: str = "Any",
    ) -> None:
        super().__init__(name, hint)

        assert nbytes >= 0

        self.__nbytes__ = nbytes
        self.__npu__ = nbytes, pack, unpack

    def __pack__(
        self, value: int, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        _nbytes, pack, _unpack = self.__npu__

        if dump is None:
            pieces.append(pack(value))
        else:
            dump.value = repr(value)

            piece = dump.memory = pack(value)

            pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[int, int]:
        nbytes, _pack, unpack = self.__npu__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            return unpack(buffer[offset:end]), end

        chunk, end = getbytes(buffer, offset, dump, nbytes)

        value = unpack(chunk)

        dump.value = repr(value)

        return value, end
