# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Integer to bytes and bytes to integer transform."""

from numbers import Integral
from typing import List, Optional, Tuple, Type, Union

from ._getbytes import getbytes
from ._typing import ByteOrderHint
from .data import Data
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform
from .view import NumberView


class IntView(NumberView, Integral):  # pylint: disable=too-many-ancestors

    """Integer type view."""

    def __and__(self, other):
        return self.unpack() & other

    def __getitem__(self, item):
        dref = self.__type__.__dref__  # pylint: disable=no-member

        if dref is None:
            raise RuntimeError(
                f"{self.__type__!r} type does not support pointer dereference"
            )

        offset = self.unpack() + (item * dref.__nbytes__)

        return dref.view(self.__buffer__, offset)

    def __iand__(self, other):
        self.set(self.unpack() & other)
        return self

    def __ilshift__(self, other):
        self.set(self.unpack() << other)
        return self

    def __int__(self):
        return NumberView.unpack(self)

    def __invert__(self):
        return ~self.unpack()  # pylint: disable=invalid-unary-operand-type

    def __ior__(self, other):
        self.set(self.unpack() | other)
        return self

    def __irshift__(self, other):
        self.set(self.unpack() >> other)
        return self

    def __ixor__(self, other):
        self.set(self.unpack() ^ other)
        return self

    def __lshift__(self, other):
        return self.unpack() << other

    def __or__(self, other):
        return self.unpack() | other

    def __rand__(self, other):
        return other & self.unpack()

    def __rlshift__(self, other):
        return other << self.unpack()

    def __ror__(self, other):
        return other | self.unpack()

    def __rrshift__(self, other):
        return other >> self.unpack()

    def __rshift__(self, other):
        return self.unpack() >> other

    def __rxor__(self, other):
        return other ^ self.unpack()

    def __setitem__(self, item, value):
        dref_view = self.__getitem__(item)
        dref_view.set(value)

    def __xor__(self, other):
        return self.unpack() ^ other

    def to_bytes(self, length, byteorder, *, signed=False):
        """Return an array of bytes representing an integer.

        :param int length:
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.

        :param str byteorder:
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            ``sys.byteorder`` as the byte order value.

        :param bool signed:
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.

        :returns: array of bytes
        :rtype: bytes

        """
        # pylint: disable=no-member
        return self.unpack().to_bytes(length, byteorder, signed=signed)


DREF = Optional[Union[Type[Data], Transform]]


class IntX(Transform):

    """Integer to bytes and bytes to integer transform."""

    __dref__: DREF
    __nbytes__: int
    __bns__: Tuple[ByteOrderHint, int, bool]

    def __init__(
        self,
        nbytes: int,
        byteorder: ByteOrderHint = "little",
        *,
        signed: bool = False,
        dref: DREF = None,
        name: Optional[str] = None,
    ) -> None:
        if name is None:
            name = f"{'s' if signed else 'u'}int{nbytes * 8}"

        super().__init__(name, hint="int")

        assert nbytes > 0
        assert byteorder in {"big", "little"}

        # store byteorder, nbytes, signed separately for use later
        # to pack/unpack to be able to support any sized integer
        # (versus storing struct pack/unpack function similar to
        # float type which is restricted to common sizes).

        self.__dref__ = dref
        self.__nbytes__ = nbytes
        self.__bns__ = byteorder, nbytes, signed

    @property
    def byteorder(self) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        return self.__bns__[0]

    @property
    def signed(self) -> bool:
        """Signed integer."""
        return self.__bns__[2]

    def __pack__(
        self, value: int, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        byteorder, nbytes, signed = self.__bns__

        if dump is None:
            pieces.append(value.to_bytes(nbytes, byteorder, signed=signed))
        else:
            # use repr in case str or something that otherwise looks like an int
            dump.value = repr(value)

            try:
                piece = value.to_bytes(nbytes, byteorder, signed=signed)
            except AttributeError:
                raise TypeError(
                    f"value type {type(value)!r} not int-like "
                    f"(no to_bytes() method)"
                ) from None

            dump.value = int(value)
            dump.memory = piece

            pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[int, int]:
        byteorder, nbytes, signed = self.__bns__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            return int.from_bytes(buffer[offset:end], byteorder, signed=signed), end

        chunk, end = getbytes(buffer, offset, dump, nbytes)

        value = dump.value = int.from_bytes(chunk, byteorder, signed=signed)

        return value, end

    def __view__(self, buffer, offset=0):
        """Create integer view of bytes in buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        """
        return IntView(self, buffer, offset)
