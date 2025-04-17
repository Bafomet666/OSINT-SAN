# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Base class for bytes to values (and vice versa) transforms."""

from typing import Any, List, Optional, Tuple, Union

from . import exceptions
from .dump import Dump, Record


class TransformMeta(type):

    """Meta class for plum types."""

    # FUTURE - remove, this metaclass not needed functionally, just for mypy

    __nbytes__: Union[None, int]


class Transform(metaclass=TransformMeta):

    """Packable/Unpacked bytes base class."""

    __nbytes__: Union[int, None] = None

    __format_name__: str
    __hint__: str

    def __init__(self, name: str, hint: str = "Any") -> None:
        self.__format_name__ = name
        self.__hint__ = hint

    @property
    def name(self) -> str:
        """Transform format name (for repr and dump "Format" column)."""
        return self.__format_name__

    @property
    def nbytes(self) -> int:
        """Transform format size in bytes."""
        nbytes = self.__nbytes__

        if nbytes is None:
            raise exceptions.SizeError(f"{self!r} sizes vary")

        return nbytes

    def __pack__(
        self, value: Any, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        raise TypeError(f"{self!r} does not support pack")  # pragma: no cover

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[Any, int]:
        raise TypeError(f"{self!r} does not support unpack")  # pragma: no cover

    def __view__(self, buffer, offset=0):
        """Create view of bytes buffer."""
        raise TypeError(f"{self!r} does not support view()")

    def pack(self, value: Any) -> bytes:
        """Pack value as formatted bytes.

        :raises: ``PackError`` if type error, value error, etc.

        """
        pieces: List[bytes] = []
        try:
            # None -> dump
            self.__pack__(value, pieces, None)
        except Exception as exc:
            # do it over to include dump in exception message
            self.pack_and_dump(value)

            raise exceptions.ImplementationError() from exc  # pragma: no cover

        return b"".join(pieces)

    def pack_and_dump(self, value: Any) -> Tuple[bytes, Dump]:
        """Pack value as formatted bytes and produce bytes summary.

        :raises: ``PackError`` if type error, value error, etc.

        """
        dump = Dump()
        pieces: List[bytes] = []
        try:
            self.__pack__(value, pieces, dump.add_record(fmt=self.__format_name__))
        except Exception as exc:
            raise exceptions.PackError(dump=dump, exception=exc) from exc

        return b"".join(pieces), dump

    def unpack(self, buffer: bytes) -> Any:
        """Unpack value from formatted bytes.

        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        """
        try:
            # None -> dump
            item, offset = self.__unpack__(buffer, 0, None)
            if buffer[offset:]:
                raise exceptions.ExcessMemoryError()
            return item

        except Exception as exc:
            # do it over to include dump in exception message
            self.unpack_and_dump(buffer)
            raise exceptions.ImplementationError() from exc  # pragma: no cover

    def unpack_and_dump(self, buffer: bytes) -> Tuple[Any, Dump]:
        """Unpack value from bytes and produce packed bytes summary.

        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        """
        dmp = Dump()
        try:
            item, offset = self.__unpack__(
                buffer, 0, dmp.add_record(fmt=self.__format_name__)
            )

            extra_bytes = buffer[offset:]

            if extra_bytes:
                for i in range(0, len(extra_bytes), 16):
                    record = dmp.add_record(memory=extra_bytes[i : i + 16])
                    if not i:
                        record.separate = True
                        record.value = "<excess bytes>"

                raise exceptions.ExcessMemoryError(extra_bytes)

        except Exception as exc:
            raise exceptions.UnpackError(dmp, exc) from exc

        return item, dmp

    def view(self, buffer: bytearray, offset: int = 0) -> Any:
        """Create view of bytes buffer."""
        return self.__view__(buffer, offset)

    def __repr__(self) -> str:
        return f"<transform {self.__format_name__!r}>"
