# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bit fields data store type."""

from typing import Dict, Optional
from .._typing import ByteOrderHint
from ..data import DataMeta
from .._code_injector import CodeInjector
from .bitfield import BitField
from .code_maker import CodeMaker


class BlendedDefault:

    """Fake BitFields type for calculating default value."""

    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    def add(self, bitfield: BitField) -> None:
        """Add bitfield default value."""
        if bitfield.default is not None:
            mask = bitfield.mask
            lsb = bitfield.lsb
            self.value = (self.value & ~(mask << lsb)) | (
                (bitfield.default & mask) << lsb
            )


class BitFieldsMeta(DataMeta):

    """Bit fields data store type metaclass."""

    __nested__: bool
    __ignore__: int
    __byteorder__: ByteOrderHint
    __default__: bool

    def __new__(
        mcs,
        name,
        bases,
        namespace,
        nbytes: Optional[int] = None,
        byteorder: ByteOrderHint = "little",
        default: int = 0,
        ignore: int = 0,
        nested: bool = False,
        fieldorder: str = "most_to_least",
    ):
        # pylint: disable=too-many-arguments,too-many-locals
        # pylint: disable=too-many-branches,too-many-statements
        if byteorder not in {"big", "little"}:
            raise ValueError('byteorder must be either "big" or "little"')

        if fieldorder not in {"least_to_most", "most_to_least"}:
            raise ValueError(
                'fieldorder must be either "least_to_most" or "most_to_least"'
            )

        # validate bit field class attributes

        fields = {}
        for fieldname, bitfield in namespace.items():
            if not isinstance(bitfield, BitField):
                continue

            bitfield.finish_initialization(fieldname)

            fields[fieldname] = bitfield

        # fill in unassigned 'pos' in all bit field properties

        lsb = 0
        field_properties = (
            fields.values()
            if fieldorder == "least_to_most"
            else reversed(list(fields.values()))
        )
        for field in field_properties:
            if field._lsb is None:
                field._lsb = lsb
            lsb = field.lsb + field.size

        # check for overlap

        claimed_bits: Dict[int, str] = {}
        for fieldname, field in fields.items():
            for i in range(field.lsb, field.lsb + field.size):
                if i in claimed_bits:
                    raise TypeError(
                        f"bit field {fieldname!r} overlaps with {claimed_bits[i]!r}"
                    )

                claimed_bits[i] = fieldname

        # default/validate 'nbytes'

        if fields:
            numbits = max(field.lsb + field.size for field in fields.values())
            nbytes_needed = (numbits + 7) // 8
        else:
            nbytes_needed = 1

        if nbytes is None:
            nbytes = nbytes_needed
        else:
            nbytes = int(nbytes)
            if nbytes < nbytes_needed:
                raise TypeError(
                    f"nbytes must be at least {nbytes_needed} for bitfields specified"
                )

        max_ = (1 << (nbytes * 8)) - 1

        # validate 'default' and blend in defaults from individual fields

        default = int(default)

        if not 0 <= default <= max_:
            raise ValueError(f"default must be: 0 <= number <= 0x{max_:x}")

        blended_default = BlendedDefault(default)
        for field in fields.values():
            blended_default.add(field)

        # validate 'ignore' and blend in ignores from individual fields

        ignore = int(ignore)

        if not 0 <= ignore <= max_:
            raise ValueError(f"ignore must be: 0 <= number <= 0x{max_:x}")

        for field in fields.values():
            if field.ignore:
                ignore |= field.mask << field.lsb
            elif isinstance(field.typ, BitFieldsMeta):
                ignore |= field.typ.__ignore__ << field.lsb

        namespace["__format_name__"] = (
            "BitFields" if name == "BitFields" else f"{name} (BitFields)"
        )
        namespace["__byteorder__"] = byteorder
        namespace["__compare_mask__"] = (max_ ^ ignore) & max_
        namespace["__fields__"] = fields
        namespace["__default__"] = blended_default.value
        namespace["__fields_with_defaults__"] = {
            name for name, field in fields.items() if field.default is not None
        }
        namespace["__ignore__"] = ignore
        namespace["__max__"] = max_
        namespace["__nbytes__"] = nbytes
        namespace["__nested__"] = bool(nested)

        code_injector = CodeInjector(namespace)

        code_maker = CodeMaker(fields.values())
        lines = list(code_maker.iter_lines(namespace, blended_default.value, nested))

        code_injector.update_script(lines)
        code_injector.execute_lines(lines)
        namespace["__implementation__"] = "\n".join(lines)

        # pylint: disable=too-many-arguments,unused-argument
        return super().__new__(mcs, name, bases, namespace)

    @property
    def byteorder(cls) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        return cls.__byteorder__

    @property
    def default(cls) -> int:
        """Default integer basis."""
        return cls.__default__

    @property
    def ignore(cls) -> int:
        """Mask for bits to ignore (e.g. 2 ignores bit 1)."""
        return cls.__ignore__

    @property
    def nested(cls) -> bool:
        """Supports being nested in another bitfields."""
        return cls.__nested__
