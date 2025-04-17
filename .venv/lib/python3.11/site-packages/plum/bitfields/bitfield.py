# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bit fields data store type."""

# pylint: disable=too-many-arguments

from enum import EnumMeta
from typing import Any, Optional

from ..enum import EnumX
from ..flag import FlagX


class BitField(property):

    """Bit field definition.

    :param doc: one line description
    :param size: size in bits
    :param typ: bit field type, default uses type annotation
    :param lsb: bit offset of least significant bit
    :param default: initial value when unspecified
    :param signed: interpret as signed integer
    :param ignore: do not include field in comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """

    # pylint: disable=too-many-instance-attributes

    def __init__(
        self,
        doc: str,
        size: int,
        typ: type,
        lsb: Optional[int],
        default: Optional[int],
        signed: bool,
        ignore: bool,
        readonly: bool,
        argrepr: Optional[str],
    ):
        property.__init__(self)

        if lsb is not None:
            lsb = int(lsb)
            if lsb < 0:
                raise TypeError(
                    "bit field position must be greater than or equal to zero"
                )

        size = int(size)
        signed = bool(signed)

        if signed:
            if size < 2:
                raise ValueError("'size' must be 2 or greater for signed bit field")
            signbit = 1 << (size - 1)
        else:
            if size < 1:
                raise ValueError("'size' must be 1 or greater for unsigned bit field")
            signbit = 0

        if signbit:
            minvalue = -(1 << (size - 1))
            maxvalue = -(1 + minvalue)
        else:
            minvalue = 0
            maxvalue = (1 << size) - 1

        if default is not None:
            default = int(default)
            if not minvalue <= default <= maxvalue:
                raise ValueError(
                    f"bit field requires {minvalue} <= default <= {maxvalue}"
                )

        self._doc = doc
        self._default = default
        self._ignore = ignore
        self._mask = (1 << size) - 1
        self._minvalue = minvalue
        self._maxvalue = maxvalue
        self._name: Optional[str] = None  # filled in later by BitFieldsMeta
        self._lsb = lsb
        self._signbit = signbit
        self._size = size
        self._make_type = None
        self._readonly = readonly
        self._argrepr = argrepr
        self._set_typ(typ)

    @property
    def argrepr(self) -> str:
        """Format string to represent bit field argument in bit fields repr."""
        if isinstance(self._argrepr, str):
            repr_format = self._argrepr

        elif isinstance(self._typ, (EnumMeta, EnumX)):
            repr_format = (
                f"{self.name}={{repr(self.{self.name}).split(':')[0].lstrip('<')}}"
            )

        else:
            repr_format = f"{self.name}={{self.{self.name}!r}}"

        return repr_format

    @property
    def default(self) -> Optional[int]:
        """Initializer default value for this bitfield."""
        return self._default

    @property
    def doc(self) -> str:
        """One line bit field description."""
        return self._doc

    @property
    def ignore(self) -> bool:
        """Ignore when compared against bitfields of same type."""
        return self._ignore

    @property
    def lsb(self) -> int:
        """Bit offset of least significant bit."""
        if self._lsb is None:  # pragma: no cover, for mypy purposes
            raise RuntimeError("internal error")
        return self._lsb

    @property
    def mask(self) -> int:
        """Bit zero aligned bit mask covering the width of the bit field."""
        return self._mask

    @property
    def minvalue(self) -> int:
        """Minimum allowable bit field value."""
        return self._minvalue

    @property
    def maxvalue(self) -> int:
        """Maximum allowable bit field value."""
        return self._maxvalue

    @property
    def name(self) -> str:
        """Bit field name."""
        if self._name is None:  # pragma: no cover, for mypy purposes
            raise RuntimeError("internal error")
        return self._name

    @property
    def readonly(self) -> bool:
        """Block setting bit field attribute."""
        return self._readonly

    @property
    def signbit(self) -> int:
        """Mask when anded with bit field value reveals if value is negative."""
        return self._signbit

    @property
    def signed(self) -> bool:
        """Interpret bit field as signed integer."""
        return bool(self._signbit)

    @property
    def size(self) -> int:
        """Bit field size in bits."""
        return self._size

    @property
    def type_hint(self) -> type:
        """Type hint expression."""
        typ = self._typ

        if isinstance(typ, EnumX):
            typ = typ.enum

        return typ

    @property
    def typ(self) -> type:
        """Bit field type.

        :returns: bit field type
        :rtype: type

        """
        return self._typ

    def _set_typ(self, typ: type):
        is_int_subclass = isinstance(typ, type) and issubclass(typ, int)

        if isinstance(typ, (FlagX, EnumX)) or is_int_subclass:
            pass

        elif hasattr(typ, "nested"):  # must be BitFields
            if not getattr(typ, "nested"):
                name = f"{self.name!r} " if self._name else ""
                raise TypeError(
                    f"bit field typ {name}must be declared as nested (e.g. "
                    f"'class {typ.__name__}(BitFields, nested=True):')"
                )

        else:
            raise TypeError("bit field type must be int-like")

        self._typ = typ

    def finish_initialization(self, name: str) -> None:
        """Complete instance initialization.

        :param name: member name

        """
        if self._name is None:
            self._name = name
        else:
            raise TypeError(
                f"invalid bit field {name!r} definition, "
                f"{type(self).__name__}() instance can not be shared "
                f"between bit fields classes"
            )

    def __repr__(self):
        return f"BitField(name={self._name!r})"

    def getter(self, fget):
        property.__init__(self, fget, self.fset, self.fdel)
        return self

    def setter(self, fset):
        if self.readonly:
            raise TypeError("'setter' not allowed on read-only bit field properties")

        property.__init__(self, self.fget, fset, self.fdel)
        return self

    def deleter(self, fdel):
        raise TypeError("bit field properties do not support 'deleter'")


def bitfield(
    doc: str = "",
    *,
    size: int,
    typ: type = int,
    lsb: Optional[int] = None,
    default: Optional[int] = None,
    signed: bool = False,
    ignore: bool = False,
    readonly: bool = False,
    argrepr: Optional[str] = None,
) -> Any:
    """Define bit field.

    :param doc: one line description
    :param size: size in bits
    :param typ: bit field type
    :param lsb: bit offset of least significant bit
    :param default: initial value when unspecified
    :param signed: interpret as signed integer
    :param ignore: do not include field in comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """
    return BitField(doc, size, typ, lsb, default, signed, ignore, readonly, argrepr)
