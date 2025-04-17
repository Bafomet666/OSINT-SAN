# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Classes and utilities for packing/unpacking bytes."""

import inspect
import os
from typing import Any, List, Optional, Tuple, Type, TypeVar, Union

from . import dump as _dump
from . import exceptions


class DataMeta(type):

    """Meta class for plum types."""

    __nbytes__: Union[int, None] = None
    __implementation__: Union[str, Tuple[str, int, Tuple[str, ...]]]
    __format_name__: Optional[str] = None

    @property
    def __hint__(cls) -> str:
        """Type hint."""
        return cls.__name__

    @property
    def name(cls) -> str:
        """Transform format name (for dump "Format" column)."""
        name = cls.__format_name__

        if name is None:
            name = cls.__name__

        return name

    @property
    def nbytes(cls) -> int:
        """Transform format size in bytes."""
        nbytes = cls.__nbytes__

        if nbytes is None:
            raise exceptions.SizeError(f"{cls.__name__!r} instance sizes vary")

        return nbytes

    @property
    def implementation(cls) -> str:
        """Generated implementation code."""
        code = cls.__implementation__

        if isinstance(code, tuple):  # pragma: no cover
            code = ""

        return code

    @implementation.setter
    def implementation(cls, value: str) -> None:  # pragma: no cover
        # pylint: disable=no-self-use
        frame = list(inspect.stack())[1].frame
        namespace = frame.f_locals
        path = os.path.abspath(frame.f_code.co_filename)
        selections = (
            () if value == "all" else tuple(v.strip() for v in value.split(","))
        )
        namespace["__implementation__"] = (path, frame.f_lineno, selections)

    def __pack__(
        cls, value: Any, pieces: List[bytes], dump: Optional[_dump.Record] = None
    ) -> None:
        raise TypeError(f"{cls.__name__!r} does not support pack")  # pragma: no cover

    def __unpack__(
        cls, buffer: bytes, offset: int, dump: Optional[_dump.Record] = None
    ) -> Tuple[Any, int]:
        raise TypeError(f"{cls.__name__!r} does not support unpack")  # pragma: no cover

    def __str__(cls) -> str:
        return f"<transform class {cls.name!r}>"

    def __repr__(cls) -> str:
        return f"<transform class {cls.name!r}>"


CLS = TypeVar("CLS", bound="Data")


class Data(metaclass=DataMeta):

    """Packable/Unpacked bytes base class."""

    __nbytes__: Union[int, None] = None
    __format_name__: str

    @property
    def nbytes(self) -> int:
        """Transform format size in bytes."""
        nbytes = self.__nbytes__

        if nbytes is None:
            nbytes = len(self.ipack())

        return nbytes

    @classmethod
    def __pack__(
        cls: Type[CLS],
        value: Any,
        pieces: List[bytes],
        dump: Optional[_dump.Record] = None,
    ) -> None:
        raise TypeError(f"{cls.__name__!r} does not support pack")  # pragma: no cover

    @classmethod
    def __unpack__(
        cls: Type[CLS], buffer: bytes, offset: int, dump: Optional[_dump.Record] = None
    ) -> Tuple[CLS, int]:
        # pylint: disable=unused-argument
        raise TypeError(f"{cls.__name__!r} does not support unpack")  # pragma: no cover

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create view of bytes buffer."""
        raise TypeError(f"{cls.__name__!r} does not support view()")

    @property
    def dump(self) -> _dump.Dump:
        """Summary containing details of bytes and layout."""
        _buffer, dump = self.ipack_and_dump()
        return dump

    @classmethod
    def pack(cls, value: Any) -> bytes:
        """Pack value as formatted bytes.

        :raises: ``PackError`` if type error, value error, etc.

        """
        pieces: List[bytes] = []
        try:
            # None -> dump
            cls.__pack__(value, pieces, None)
        except Exception as exc:
            # do it over to include dump in exception message
            cls.pack_and_dump(value)

            raise exceptions.ImplementationError() from exc  # pragma: no cover

        return b"".join(pieces)

    def ipack(self) -> bytes:
        """Pack instance as bytes.

        :raises: ``PackError`` if type error, value error, etc.

        """
        pieces: List[bytes] = []
        try:
            # None -> dump
            self.__pack__(self, pieces, None)
        except Exception as exc:
            # do it over to include dump in exception message
            self.ipack_and_dump()

            raise exceptions.ImplementationError() from exc  # pragma: no cover

        return b"".join(pieces)

    @classmethod
    def pack_and_dump(cls, value: Any) -> Tuple[bytes, _dump.Dump]:
        """Pack value as formatted bytes and produce bytes summary.

        :raises: ``PackError`` if type error, value error, etc.

        """
        dump = _dump.Dump()
        pieces: List[bytes] = []
        try:
            cls.__pack__(value, pieces, dump.add_record(fmt=cls.name))
        except Exception as exc:
            raise exceptions.PackError(dump=dump, exception=exc) from exc

        return b"".join(pieces), dump

    def ipack_and_dump(self) -> Tuple[bytes, _dump.Dump]:
        """Pack instance as bytes and produce bytes summary.

        :raises: ``PackError`` if type error, value error, etc.

        """
        dmp = _dump.Dump()
        pieces: List[bytes] = []
        try:
            self.__pack__(self, pieces, dmp.add_record(fmt=type(self).name))
        except Exception as exc:
            raise exceptions.PackError(dump=dmp, exception=exc) from exc

        return b"".join(pieces), dmp

    @classmethod
    def unpack(cls, buffer: bytes) -> Any:
        """Unpack value from formatted bytes.

        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        """
        try:
            # None -> dump
            item, offset = cls.__unpack__(buffer, 0, None)
            if buffer[offset:]:
                raise exceptions.ExcessMemoryError()
            return item

        except Exception as exc:
            # do it over to include dump in exception message
            cls.unpack_and_dump(buffer)
            raise exceptions.ImplementationError() from exc  # pragma: no cover

    @classmethod
    def unpack_and_dump(cls, buffer: bytes) -> Tuple[Any, _dump.Dump]:
        r"""Unpack value from bytes and produce packed bytes summary.

        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        """
        dmp = _dump.Dump()
        try:
            item, offset = cls.__unpack__(buffer, 0, dmp.add_record(fmt=cls.name))

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

    @classmethod
    def view(cls, buffer: bytearray, offset: int = 0) -> Any:
        """Create view of bytes buffer."""
        return cls.__view__(buffer, offset)


# for easy injection of boost versions of utilities into this namespace
plum_namespace = globals()
packmethod_doc = Data.ipack.__doc__  # pylint: disable=no-member
unpackmethod_doc = Data.unpack.__doc__  # pylint: disable=no-member
