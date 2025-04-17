# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Data view base class."""

from typing import Any, Tuple, Type, Union

from math import ceil, floor

from .data import Data, DataMeta
from .transform import Transform
from .dump import Dump
from .exceptions import ImplementationError, UnpackError


class PlumView:

    """Data view base class.

    :param DataMeta fmt: associated plum type
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
    :param int offset: byte offset

    """

    # instance attributes (set as class attributes for pylint)
    __type__: Type[Data] = Data
    __offset__ = 0
    __buffer__ = bytearray()
    __fob__: Tuple[Type[Data], int, bytearray] = (__type__, __offset__, __buffer__)

    def __init__(self, fmt: Union[Type[Data], Transform], buffer, offset):
        if not isinstance(fmt, (DataMeta, Transform)):
            raise TypeError("invalid plumtype")

        object.__setattr__(self, "__type__", fmt)
        object.__setattr__(self, "__buffer__", buffer)
        object.__setattr__(self, "__offset__", offset)
        object.__setattr__(self, "__fob__", (fmt, offset, buffer))

    def __repr__(self):
        try:
            value = self.unpack()
        except Exception:  # pylint: disable=broad-except
            value = f"<view at 0x{self.__offset__:x}>"
        else:
            value = f"<view at 0x{self.__offset__:x}: {value!r}>"
        return value

    def __str__(self):
        try:
            value = str(self.unpack())
        except Exception:  # pylint: disable=broad-except
            value = f"<view at 0x{self.__offset__:x}>"
        return value

    def cast(self, cls: Type[Data]):
        """Create a new view of item's buffer bytes.

        :param DataMeta cls: view type
        :returns: new view
        :rtype: cls
        """
        return cls.view(self.__buffer__, self.__offset__)

    @property
    def dump(self):
        """Packed bytes summary.

        :returns: summary table of view detailing bytes and layout
        :rtype: str

        """
        return self.unpack_and_dump()[1]

    def unpack(self) -> Any:
        """Unpack item from buffer bytes."""
        fmt, offset, buffer = self.__fob__
        try:
            # None -> dump
            return fmt.__unpack__(buffer, offset, None)[0]

        except Exception as exc:
            self.unpack_and_dump()
            raise ImplementationError() from exc  # pragma: no cover

    def unpack_and_dump(self) -> Tuple[Data, Dump]:
        r"""Unpack item from bytes and produce packed bytes summary.

        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        """
        fmt, offset, buffer = self.__fob__

        dump = Dump(offset=self.__offset__)
        try:
            item, _offset = fmt.__unpack__(
                buffer, offset, dump.add_record(fmt=fmt.name)
            )

        except Exception as exc:
            raise UnpackError(dump, exc) from exc

        return item, dump

    @property
    def nbytes(self) -> int:
        """Bytes buffer view size in bytes."""
        nbytes = self.__type__.__nbytes__

        # FUTURE - remove cover comment when views support variable sized types
        if nbytes is None:  # pragma: no cover
            fmt, offset, buffer = self.__fob__
            try:
                # None -> dump
                _item, end = fmt.__unpack__(buffer, offset, None)

            except Exception as exc:
                self.unpack_and_dump()
                raise ImplementationError() from exc  # pragma: no cover

            nbytes = end - offset

        return nbytes

    def pack(self) -> bytes:
        """Pack as formatted bytes.

        :raises: ``PackError`` if type error, value error, etc.

        """
        fmt, offset, buffer = self.__fob__

        nbytes = fmt.__nbytes__

        # FUTURE - remove cover comment when views support variable sized types
        if nbytes is None:  # pragma: no cover
            try:
                # None -> dump
                _item, end = fmt.__unpack__(buffer, offset, None)

            except Exception as exc:
                self.unpack_and_dump()
                raise ImplementationError() from exc  # pragma: no cover

            bindata = bytes(buffer[offset:end])
        else:
            bindata = bytes(buffer[offset : offset + nbytes])

        if len(bindata) != nbytes:
            self.pack_and_dump()
            raise ImplementationError()  # pragma: no cover

        return bindata

    ipack = pack

    def pack_and_dump(self):
        """Pack value as formatted bytes and produce bytes summary.

        :returns: bytes buffer, packed bytes summary
        :rtype: bytearray, Dump

        """
        fmt, offset, buffer = self.__fob__

        dump = Dump(offset=self.__offset__)
        try:
            _item, end = fmt.__unpack__(buffer, offset, dump.add_record(fmt=fmt))

        except Exception as exc:
            raise UnpackError(dump, exc) from exc

        return bytes(buffer[offset:end]), dump

    ipack_and_dump = pack_and_dump

    def set(self, value):
        """Pack value into bytes buffer.

        :param object value: new value

        """
        fob, offset, buffer = self.__fob__

        membytes = fob.pack(value)

        buffer[offset : offset + len(membytes)] = membytes


class NumberView(PlumView):

    """Numeric view class."""

    def __abs__(self):
        return abs(self.unpack())

    def __add__(self, other):
        return self.unpack() + other

    def __divmod__(self, other):
        return divmod(self.unpack(), other)

    def __float__(self):
        return float(self.unpack())

    def __eq__(self, other):
        return self.unpack() == other

    def __ge__(self, other):
        return self.unpack() >= other

    def __gt__(self, other):
        return self.unpack() > other

    def __iadd__(self, other):
        self.set(self.unpack() + other)
        return self

    def __imod__(self, other):
        self.set(self.unpack() % other)
        return self

    def __imul__(self, other):
        self.set(self.unpack() * other)
        return self

    def __int__(self):
        return int(self.unpack())

    def __ipow__(self, other, modulus=None):
        self.set(self.unpack().__pow__(other, modulus))  # pylint: disable=no-member
        return self

    def __isub__(self, other):
        self.set(self.unpack() - other)
        return self

    def __le__(self, other):
        return self.unpack() <= other

    def __lt__(self, other):
        return self.unpack() < other

    def __mod__(self, other):
        return self.unpack() % other

    def __mul__(self, other):
        return self.unpack() * other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        return -self.unpack()  # pylint: disable=invalid-unary-operand-type

    def __pos__(self):
        return +self.unpack()  # pylint: disable=invalid-unary-operand-type

    def __pow__(self, exponent, modulus=None):
        return self.unpack().__pow__(exponent, modulus)  # pylint: disable=no-member

    def __radd__(self, other):
        return other + self.unpack()

    def __rdivmod__(self, other):
        return divmod(other, self.unpack())

    def __repr__(self):
        try:
            value = self.unpack()
        except Exception:  # pylint: disable=broad-except
            rep = f"<view at 0x{self.__offset__:x}>"
        else:
            rep = f"<{self.__type__.name} view at 0x{self.__offset__:x}: {value}>"
        return rep

    def __rmod__(self, other):
        return other % self.unpack()

    def __rmul__(self, other):
        return other * self.unpack()

    def __rpow__(self, other):
        return other ** self.unpack()

    def __rsub__(self, other):
        return other - self.unpack()

    def __rtruediv__(self, other):
        return other / self.unpack()

    def __sub__(self, other):
        return self.unpack() - other

    def __truediv__(self, other):
        return self.unpack() / other

    def __ceil__(self):
        return ceil(self.unpack())

    def __floor__(self):
        return floor(self.unpack())

    def __floordiv__(self, other):
        return self.unpack().__floordiv__(other)  # pylint: disable=no-member

    def __rfloordiv__(self, other):
        return self.unpack().__rfloordiv__(other)  # pylint: disable=no-member

    def __round__(self, ndigits=None):
        return self.unpack().__round__(ndigits)  # pylint: disable=no-member

    def __trunc__(self):
        return self.unpack().__trunc__()  # pylint: disable=no-member

    def __hash__(self):
        raise TypeError(f"unhashable type: {type(self).__name__}")
