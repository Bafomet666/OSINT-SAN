# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bit fields data store type."""

from typing import Dict, List, Optional, Set, Tuple, Type, TypeVar, Union

from .._getbytes import getbytes
from ..data import Data
from ..dump import Record
from ..enum import EnumX
from ..exceptions import InsufficientMemoryError
from .bitfield import BitField, bitfield
from .meta import BitFieldsMeta, ByteOrderHint

BitField.__module__ = "plum.bitfields"
bitfield.__module__ = "plum.bitfields"
BitFieldsMeta.__module__ = "plum.bitfields"

CLS = TypeVar("CLS", bound="BitFields")


class BitFields(
    Data, metaclass=BitFieldsMeta, nbytes=4, byteorder="little", default=0, ignore=0
):

    """Bit fields data store type."""

    # filled in by metaclass
    __byteorder__: ByteOrderHint = "little"
    __compare_mask__: int = 0xFFFFFFFF
    __fields__: Dict = dict()
    __default__: int = 0
    __fields_with_defaults__: Set = set()
    __ignore__: int = 0
    __max__: int = 0xFFFFFFFF
    __nbytes__: int = 4

    def __init__(self):
        self.__value__ = self.__default__

    @classmethod
    def from_int(cls: Type[CLS], value: int) -> CLS:
        """Create instance populated from integer value."""
        instance = object.__new__(cls)

        if not 0 <= value <= cls.__max__:
            raise ValueError(
                f"{cls.__name__}.from_int() requires 0 <= value <= {cls.__max__}"
            )

        instance.__value__ = int(value)

        return instance

    @classmethod
    def __pack__(
        cls,
        value: Union["BitFields", int],
        pieces: List[bytes],
        dump: Optional[Record] = None,
    ) -> None:
        if isinstance(value, dict):
            value = cls(**value)

        if dump is None:
            pieces.append(
                int(value).to_bytes(cls.__nbytes__, cls.__byteorder__, signed=False)
            )
        else:
            dump.value = str(value)  # in case something goes wrong

            int_value = int(value)
            chunk = int_value.to_bytes(cls.__nbytes__, cls.__byteorder__, signed=False)

            pieces.append(chunk)

            dump.value = str(int_value)
            dump.memory = chunk
            cls.__add_bitfields_to_dump__(int_value, dump)

    @classmethod
    def __unpack__(
        cls, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple["BitFields", int]:
        if dump is None:
            end = offset + cls.__nbytes__

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            int_value = int.from_bytes(
                buffer[offset:end], cls.__byteorder__, signed=False
            )

            return cls.from_int(int_value), end

        chunk, offset = getbytes(buffer, offset, dump, cls.__nbytes__)

        int_value = int.from_bytes(chunk, cls.__byteorder__, signed=False)

        bitfields = cls.from_int(int_value)

        dump.value = bitfields.__value__
        cls.__add_bitfields_to_dump__(bitfields, dump)

        return bitfields, offset

    @classmethod
    def __add_bitfields_to_dump__(cls, bitfields, dump, bitoffset=0):
        if not isinstance(bitfields, cls):
            bitfields = cls.from_int(int(bitfields))

        for name, accessor in cls.__fields__.items():
            bitfield_typ = accessor.typ

            if not isinstance(bitfield_typ, EnumX) and issubclass(
                bitfield_typ, BitFields
            ):
                row = dump.add_record(access=name, fmt=bitfield_typ)
                bitfield_typ.__add_bitfields_to_dump__(
                    getattr(cls, name).__get__(bitfields, cls),
                    row,
                    bitoffset + accessor.lsb,
                )

            else:
                dump.add_record(
                    access=name,
                    bits=(bitoffset + accessor.lsb, accessor.size),
                    value=getattr(cls, name).__get__(bitfields, cls),
                    fmt=bitfield_typ,
                )

    @classmethod
    def _normalize_for_compare(cls, value, other):
        if isinstance(other, dict):
            other = cls(**other)

        if isinstance(other, cls):
            other = other.__value__ & cls.__compare_mask__
            value = value & cls.__compare_mask__
        else:
            try:
                other = int(other)
            except ValueError:
                pass

        return value, other

    def __lt__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__lt__(value, other)

    def __le__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__le__(value, other)

    def __eq__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__eq__(value, other)

    def __ne__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__ne__(value, other)

    def __gt__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__gt__(value, other)

    def __ge__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__ge__(value, other)

    def __hash__(self):
        return int.__hash__(self.__value__ & type(self).__compare_mask__)

    def __bool__(self):
        return int.__bool__(self.__value__ & type(self).__compare_mask__)

    def __add__(self, other):
        return int.__add__(self.__value__, other)

    def __sub__(self, other):
        return int.__sub__(self.__value__, other)

    def __mul__(self, other):
        return int.__mul__(self.__value__, other)

    def __truediv__(self, other):
        return int.__truediv__(self.__value__, other)

    def __floordiv__(self, other):
        return int.__floordiv__(self.__value__, other)

    def __mod__(self, other):
        return int.__mod__(self.__value__, other)

    def __divmod__(self, other):
        return int.__divmod__(self.__value__, other)

    def __pow__(self, other, *args):
        return int.__pow__(self.__value__, other, *args)

    def __lshift__(self, other):
        return int.__lshift__(self.__value__, other)

    def __rshift__(self, other):
        return int.__rshift__(self.__value__, other)

    def __and__(self, other):
        return int.__and__(self.__value__, other)

    def __xor__(self, other):
        return int.__xor__(self.__value__, other)

    def __or__(self, other):
        return int.__or__(self.__value__, other)

    def __radd__(self, other):
        return int.__radd__(self.__value__, other)

    def __rsub__(self, other):
        return int.__rsub__(self.__value__, other)

    def __rmul__(self, other):
        return int.__rmul__(self.__value__, other)

    def __rtruediv__(self, other):
        return int.__rtruediv__(self.__value__, other)

    def __rfloordiv__(self, other):
        return int.__rfloordiv__(self.__value__, other)

    def __rmod__(self, other):
        return int.__rmod__(self.__value__, other)

    def __rdivmod__(self, other):
        return int.__rdivmod__(self.__value__, other)

    def __rpow__(self, other, *args):
        return int.__rpow__(self.__value__, other, *args)

    def __rlshift__(self, other):
        return int.__rlshift__(self.__value__, other)

    def __rrshift__(self, other):
        return int.__rrshift__(self.__value__, other)

    def __rand__(self, other):
        return int.__rand__(self.__value__, other)

    def __rxor__(self, other):
        return int.__rxor__(self.__value__, other)

    def __ror__(self, other):
        return int.__ror__(self.__value__, other)

    def __iadd__(self, other):
        return self.__value__ + other

    def __isub__(self, other):
        return self.__value__ - other

    def __imul__(self, other):
        return self.__value__ * other

    def __itruediv__(self, other):
        return self.__value__ / other

    def __ifloordiv__(self, other):
        return self.__value__ // other

    def __imod__(self, other):
        return self.__value__ % other

    def __ilshift__(self, other):
        return self.__value__ << other

    def __irshift__(self, other):
        return self.__value__ >> other

    def __iand__(self, other):
        return self.__value__ & other

    def __ixor__(self, other):
        return self.__value__ ^ other

    def __ior__(self, other):
        return self.__value__ | other

    def __neg__(self):
        return -self.__value__

    def __pos__(self):
        return self.__value__

    def __abs__(self):
        return self.__value__

    def __invert__(self):
        return ~self.__value__

    def __int__(self):
        return self.__value__

    def __float__(self):
        return int.__float__(self.__value__)

    def __index__(self):
        return int.__index__(self.__value__)

    def __round__(self, *args):
        return int.__round__(self.__value__, *args)

    def asdict(self):
        """Return bit field values in dictionary form.

        :returns: bit field names/values
        :rtype: dict

        """
        return {name: getattr(self, name) for name in self.__fields__}

    def __setattr__(self, key, value):
        if key.startswith("__") or key in self.__fields__:
            super().__setattr__(key, value)
        else:
            raise AttributeError(f"{type(self).__name__!r} has no attribute {key!r}")

    def __getitem__(self, index):
        nbits = self.__nbytes__ * 8
        mask = 1
        bits = []
        value = int(self)
        while nbits:
            bits.append(bool(value & mask))
            mask <<= 1
            nbits -= 1
        return bits[index]

    def __setitem__(self, index, value):
        bits = self[:]
        nbits = len(bits)
        bits[index] = value
        if len(bits) != nbits:
            raise ValueError("slice and value not same length")
        i = 0
        mask = 1
        for bit in bits:
            if bit:
                i |= mask
            mask <<= 1
        self.__value__ = i
