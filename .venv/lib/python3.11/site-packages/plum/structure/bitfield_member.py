# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bit field structure member definition."""

# pylint: disable=too-many-arguments

from dataclasses import dataclass
from enum import EnumMeta
from typing import Any, Dict, Optional, Tuple

from .._code_injector import CodeInjector
from .._default import NO_DEFAULT
from .._getbytes import getbytes
from .._typing import ByteOrderHint
from ..bitfields import BitFields, BitFieldsMeta
from ..dump import Record
from ..enum import EnumX
from ..flag import FlagX
from ..exceptions import InsufficientMemoryError
from ..none import NoneX
from .member import Member


@dataclass
class BitFieldsStore:

    """Temporary information store for generating implementation code."""

    is_first: bool = False
    is_last: bool = False
    group_name: str = ""
    nbytes: Optional[int] = None
    byteorder: str = "little"


class BitFieldMember(Member):

    """Bit field structure member definition.

    :param doc: accessor documentation string
    :param size: bit field width (in bits)
    :param lsb: least significant bit position
    :param typ: field type (e.g. ``IntEnum`` subclass), default uses type annotation
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param compute: initializer defaults to compute based on another member
    :param nbytes: bytes occupied by this bit field and ones that follow (0 => calculate)
    :param argrepr: format to represent member argument in structure repr

    """

    aux_store: BitFieldsStore

    _group_name: str
    _typ: Any

    _attributes_to_copy: Tuple[str, ...] = Member._attributes_to_copy + (
        "_typ",
        "_size",
        "_lsb",
        "_signed",
        "_group_name",
    )

    def __init__(
        self,
        doc: str,
        size: int,
        lsb: Optional[int],
        typ: type,
        signed: bool,
        default: Any,
        ignore: bool,
        readonly: bool,
        compute: bool,
        nbytes: int,
        argrepr: Optional[str],
    ) -> None:
        if lsb is not None:
            lsb = int(lsb)
            if lsb < 0:
                raise TypeError(
                    "bit field position must be greater than or equal to zero"
                )

        if signed and size < 2:
            raise ValueError("'size' must be 2 or greater for signed bit field")

        if size < 1:
            raise ValueError("'size' must be 1 or greater for unsigned bit field")

        super().__init__(
            doc,
            default,
            ignore,
            readonly,
            compute,
            argrepr,
            fmt=NoneX(),
            fmt_arg=None,
        )

        self._set_typ(typ)
        self._size = size
        self._lsb = lsb
        self._nbytes = nbytes
        self._signed = signed
        self._group_name = ""

    @property
    def lsb(self) -> int:
        """Bit field bit position."""
        return -1 if self._lsb is None else self._lsb

    @property
    def nbytes(self) -> int:
        """Number of bytes allocated for this and following bit fields.

        Return zero for bit fields included in previous bit field allocation.

        """
        if self._nbytes is None:  # pragma: no cover
            raise RuntimeError("internal error")
        return self._nbytes

    @property
    def signed(self) -> bool:
        """Bit field is a signed integer."""
        return self._signed

    @property
    def size(self) -> int:
        """Bit field width (in bits)."""
        return self._size

    @property
    def typ(self) -> type:
        """Field type (e.g. ``IntEnum`` subclass), default uses type annotation."""
        return self._typ

    def _set_typ(self, typ: type):
        # FUTURE - eliminate/conditionalize this code for performance
        try:
            is_int_subclass = issubclass(typ, (int, BitFields))

        except TypeError:
            is_int_subclass = False  # must not be class

        if isinstance(typ, (FlagX, EnumX)) or is_int_subclass:
            pass

        else:
            raise TypeError("bit field type must be int-like")

        self._typ = typ

    @property
    def argrepr(self) -> str:
        """Format string to represent member argument in structure repr."""
        if isinstance(self._argrepr, str):
            repr_format = self._argrepr

        elif isinstance(self._typ, EnumMeta):
            repr_format = (
                f"{self.name}={{repr(self.{self.name}).split(':', 1)[0].lstrip('<')}}"
            )

        else:
            repr_format = f"{self.name}={{self.{self.name}!r}}"

        return repr_format

    @classmethod
    def organize(cls, members: Dict[str, Member], byteorder: str, fieldorder: str):
        """Organize bit field members into groups."""
        collection = []
        group = {}

        for name, member in members.items():
            if isinstance(member, BitFieldMember) and not member.nbytes:
                group[name] = member
                continue

            if group:
                collection.append(group)
                group = {}

            if isinstance(member, BitFieldMember):
                group[name] = member

        if group:
            collection.append(group)

        for i, group in enumerate(collection):
            nbytes = cls.position_and_size(f"fields_{i}", group, fieldorder)
            for member in group.values():
                member.aux_store = BitFieldsStore(
                    byteorder=byteorder, nbytes=nbytes, group_name=f"bitfields_{i}"
                )
            list(group.values())[0].aux_store.is_first = True
            list(group.values())[-1].aux_store.is_last = True

    @staticmethod
    def position_and_size(
        group_name: str, members: Dict[str, "BitFieldMember"], fieldorder: str
    ) -> int:
        """Fill in any unassigned positions, determine overall size."""
        # fill in missing positions (and assign group name)
        lsb = 0
        field_member_properties = (
            members.values()
            if fieldorder == "least_to_most"
            else reversed(list(members.values()))
        )
        for field_member in field_member_properties:
            # pylint: disable=protected-access
            field_member._group_name = group_name
            if field_member._lsb is None:
                field_member._lsb = lsb
            lsb = field_member.lsb + field_member.size

        # check for overlap
        claimed_bits: Dict[int, str] = {}
        for name, member in members.items():
            for i in range(member.lsb, member.lsb + member.size):
                if i in claimed_bits:
                    raise TypeError(
                        f"bit field {name!r} overlaps with {claimed_bits[i]!r}"
                    )

                claimed_bits[i] = name

        # default/validate 'nbytes'
        numbits = max(member.lsb + member.size for member in members.values())
        nbytes_needed = (numbits + 7) // 8

        first_bitfield_name, first_bitfield = list(members.items())[0]
        nbytes = first_bitfield.nbytes

        if not nbytes:
            nbytes = first_bitfield._nbytes = nbytes_needed

        elif nbytes_needed > nbytes:
            raise TypeError(
                f"'nbytes' must be at least {nbytes_needed} for bitfield "
                f"{first_bitfield_name!r} (to have sufficient room for it "
                f"and those that follow)"
            )

        return nbytes

    @staticmethod
    def __unpack__(
        buffer: bytes,
        offset: int,
        dump: Optional[Record],
        byteorder: ByteOrderHint,
        nbytes: int,
        signed: bool,
    ) -> Tuple[int, int]:
        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError(
                    "too few bytes to unpack, retry with dump to follow"
                )

            value = int.from_bytes(buffer[offset:end], byteorder, signed=signed)

            return value, end

        chunk, offset = getbytes(buffer, offset, dump, nbytes)

        value = int.from_bytes(chunk, byteorder, signed=signed)

        dump.value = value

        return value, offset

    def add_name_index(
        self,
        name: str,
        index: int,
        code_injector: CodeInjector,
    ) -> int:
        """Assign name, index number, and prepare for code generation."""
        # pylint: disable=too-many-statements, too-many-branches, too-many-locals
        index = super().add_name_index(name, index, code_injector)

        store = self.temp_store
        aux = self.aux_store

        # Erase normal member packing lines (from super)
        store.unpack = []
        store.unpack_and_dump = []
        store.pack = []
        store.pack_and_dump = []

        lo_mask = (1 << self.size) - 1
        sign_bit = 1 << (self.size - 1)

        cls_name = code_injector.get_expression(self.typ, f"cls.{self.name}.typ")

        dump_name = f"{aux.group_name}_dump"
        dump_group = [f"{dump_name} = dump.add_record()"]

        if isinstance(self.typ, BitFieldsMeta):
            dump_member = [
                # line 1
                f"dump_m_{self.name} = dump.add_record("
                f'access="{name}", value=int(m_{self.name}), fmt={cls_name})',
                # line 2
                f"{cls_name}.__add_bitfields_to_dump__("
                f"m_{self.name}, dump_m_{self.name}, bitoffset={self.lsb})",
            ]
        else:
            dump_member = [
                f"dump.add_record("
                f'access="{name}", bits={self.lsb, self.size}, '
                f"value=m_{self.name}, fmt={cls_name})"
            ]

        if aux.is_first:
            store.unpack += [
                f"{aux.group_name}, offset = "
                f"cls.{name}.__unpack__(buffer, offset, dump, "
                f'"{aux.byteorder}", nbytes={aux.nbytes}, signed={self.signed})',
                "",
            ]

            store.unpack_and_dump += dump_group + [
                f"{aux.group_name}, offset = "
                f"cls.{name}.__unpack__(buffer, offset, {dump_name}, "
                f'"{aux.byteorder}", nbytes={aux.nbytes}, signed={self.signed})',
                "",
            ]

        lines = [f"m_{name} = ({aux.group_name} >> {self.lsb}) & 0x{lo_mask:x}"]

        if self.signed:
            lines += [
                f"if m_{name} & 0x{sign_bit:x}:",
                f"    m_{name} -= 0x{1 << self.size:x}",
            ]

        if self.typ is not int:
            if isinstance(self.typ, BitFieldsMeta):
                lines.append(f"m_{name} = {cls_name}.from_int(m_{name})")
            else:
                lines.append(f"m_{name} = {cls_name}(m_{name})")

        store.unpack += lines
        store.unpack_and_dump += lines + dump_member

        if aux.is_first:
            lines = [f"{aux.group_name} = 0", ""]
            store.pack += lines
            store.pack_and_dump += dump_group + lines

        assert self.lsb is not None, "internal error"
        hi_mask = ~(lo_mask << self.lsb)
        member_name = f"m_{self.name}"
        if self.typ is bool:
            # don't let an integer > 1 be masked off and become False
            member_name = f"int(bool({member_name}))"
        op2 = f"({member_name} & 0x{lo_mask:x})"
        if self.lsb:
            op2 = f"({op2} << {self.lsb})"
        lines = [f"{aux.group_name} |= ({aux.group_name} & {hi_mask}) | {op2}"]
        store.pack += lines
        store.pack_and_dump += dump_member + lines

        if aux.is_last:
            store.pack += [
                "",
                f"pieces.append({aux.group_name}.to_bytes("
                f'{aux.nbytes}, "{aux.byteorder}", signed={self.signed}))',
            ]
            store.pack_and_dump += [
                "",
                f"pieces.append({aux.group_name}.to_bytes("
                f'{aux.nbytes}, "{aux.byteorder}", signed={self.signed}))',
                f"{dump_name}.value = str({aux.group_name})",
                f"{dump_name}.memory = pieces[-1]",
            ]

        if self.signed:
            neg_limit = -(1 << (self.size - 1))
            maxvalue = f"{-(1 + neg_limit)}"
            minvalue = f"-{-neg_limit}"
        else:
            minvalue = "0"
            maxvalue = f"{(1 << self.size) - 1}"

        if self.fset is None and not self.readonly:
            # override lines put in by super()
            if isinstance(self.typ, EnumMeta):
                store.setter = (
                    []
                )  # no need for range check, enum instantiation checks validity
            else:
                store.setter = [
                    f"if not {minvalue} <= value <= {maxvalue}:",
                    f'   raise ValueError("out of range, {minvalue} <= value <= {maxvalue}")',
                ]
            if self.typ is int:
                store.setter.append(f"self[{self.index}] = value")
            else:
                typ = cls_name.replace("cls.", "type(self).")
                store.setter.append(f"self[{self.index}] = {typ}(value)")

        if not self.default_is_a_factory:
            store.init_begin += [
                f"if not {minvalue} <= {self.name} <= {maxvalue}:",
                f'   raise ValueError("{self.name!r} out of range, {minvalue} <= {self.name} <= {maxvalue}")',
            ]

        return index


def bitfield_member(
    doc: str = "",
    *,
    size: int,
    lsb: Optional[int] = None,
    typ: type = int,
    signed: bool = False,
    default: Any = NO_DEFAULT,
    ignore: bool = False,
    readonly: bool = False,
    compute: bool = False,
    nbytes: int = 0,
    argrepr: Optional[str] = None,
) -> Any:
    """Bit field structure member definition.

    :param doc: accessor documentation string
    :param size: bit field width (in bits)
    :param lsb: least significant bit position
    :param signed: interpret as signed integer
    :param typ: field type (e.g. ``IntEnum`` subclass)
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param compute: initializer defaults to compute based on another member
    :param nbytes: bytes occupied by this bit field and ones that follow (0 => calculate)
    :param argrepr: format to represent member argument in structure repr

    """
    return BitFieldMember(
        doc, size, lsb, typ, signed, default, ignore, readonly, compute, nbytes, argrepr
    )
