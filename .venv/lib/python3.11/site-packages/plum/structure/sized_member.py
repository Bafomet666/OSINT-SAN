# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variable sized member definition."""

# pylint: disable=too-many-arguments

from typing import Any, Optional, Tuple

from .._typing import Format
from .._code_injector import CodeInjector
from .._default import NO_DEFAULT
from .._getbytes import getbytes
from ..dump import Record
from ..exceptions import ExcessMemoryError, InsufficientMemoryError
from .member import Member


class SizedMember(Member):

    """Sized structure member definition.

    :param doc: accessor documentation string
    :param fmt: member format, default uses type annotation
    :param size: member property which controls size
    :param ratio: number of bytes per increment of size member
    :param offset: difference in size (in bytes)
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """

    _attributes_to_copy: Tuple[str, ...] = Member._attributes_to_copy + (
        "_offset",
        "_ratio",
        "_size",
    )

    def __init__(
        self,
        doc: str,
        fmt: Format,
        size: Member,
        ratio: float,
        offset: int,
        default: Any,
        ignore: bool,
        readonly: bool,
        argrepr: Optional[str],
    ) -> None:
        super().__init__(
            doc,
            default,
            ignore,
            readonly,
            compute=False,
            argrepr=argrepr,
            fmt=fmt,
            fmt_arg=None,
        )

        if not isinstance(size, Member):
            raise TypeError("invalid 'size', must be a 'member()'")

        self._ratio = ratio
        self._offset = offset
        self._size = size

    @property
    def offset(self) -> int:
        """Difference in size (in bytes)."""
        return self._offset

    @property
    def ratio(self) -> float:
        """Number of bytes per increment of size member."""
        return self._ratio

    @property
    def size(self) -> Member:
        """Member property which controls size."""
        return self._size

    def add_name_index(
        self,
        name: str,
        index: int,
        code_injector: CodeInjector,
    ) -> int:
        """Assign name, index number, and prepare for code generation."""
        store = self.temp_store

        size_member = self.size

        index = Member.add_name_index(self, name, index, code_injector)

        if size_member.compute:
            size_member.temp_store.num_associated += 1

            # add logic to this member's setter to recompute associated size member
            # (but only when setter not explicitly defined in structure class)
            if not self.readonly and not self.fset:
                store.setter.append(
                    f"self[{size_member.index}] = None  "
                    f"# re-compute {size_member.name!r} member"
                )

            self.adjust_related_getter()

            related_pack = self.adjust_related_pack(dump=False)
            related_pack_and_dump = self.adjust_related_pack(dump=True)

            self.adjust_pack(related_pack, dump=False)
            self.adjust_pack(related_pack_and_dump, dump=True)

        self.adjust_unpack(dump=False)
        self.adjust_unpack(dump=True)

        return index

    def adjust_related_getter(self):
        """Prepare for getter code generation for related member."""
        size_member = self.size

        if not size_member.fget:
            lines = size_member.temp_store.getter
            lines[0:0] = [
                f"if self[{size_member.index}] is None:",
                f"    self[{size_member.index}] = self.unpack(self.ipack())[{size_member.index}]",
                "",
            ]

    def adjust_related_pack(self, dump: bool) -> str:
        """Prepare for pack code generation for related member."""
        size_member = self.size
        lines = (
            size_member.temp_store.pack_and_dump
            if dump
            else size_member.temp_store.pack
        )

        pack_line = lines.pop()

        dump_extra = (
            [f'    {size_member.name}_dump.value = "<skipped>"'] if dump else []
        )

        lines += (
            [
                f"{size_member.name}_pieces_index = len(pieces)",
                f"if m_{size_member.name} is None:",
            ]
            + dump_extra
            + [
                '    pieces.append(b"")',
                "else:",
                "    " + pack_line,
            ]
        )

        return pack_line

    def adjust_pack(self, related_pack_line: str, dump: bool):
        """Prepare for pack code generation for this member."""
        size_member = self.size
        lines = self.temp_store.pack_and_dump if dump else self.temp_store.pack

        size = f'len(b"".join(pieces[{self.name}_pieces_index:]))'

        if self.ratio != 1:
            size = f"int({size} // {self.ratio})"

        if self.offset != 0:
            size += f" + {self.offset}"

        pack_line = lines.pop()

        # pylint: disable=f-string-without-interpolation
        lines += [
            f"if m_{size_member.name} is None:",
            f"    {self.name}_pieces_index = len(pieces)",
            f"    " + pack_line,
            f"    m_{size_member.name} = {size}",
            f"    " + related_pack_line,
            f"    pieces[{size_member.name}_pieces_index] = pieces.pop()",
            f"else:",
            f"    " + pack_line,
        ]

    def adjust_unpack(self, dump: bool) -> None:
        """Prepare for unpack code generation for this member."""
        size_member = self.size
        store = self.temp_store
        lines = store.unpack_and_dump if dump else store.unpack

        temp_buffer = f"{self.name}_buffer"

        unpack_line = lines.pop()
        dump_arg = f", {self.name}_dump" if dump else ""

        nbytes = f"m_{size_member.name}"
        if self.offset:
            nbytes = f"({nbytes} - {self.offset})"
        if self.ratio != 1:
            nbytes = f"int({nbytes} * {self.ratio})"

        if self.offset or self.ratio != 1:
            lines.append(f"{self.name}_nbytes = {nbytes}")
            nbytes = f"{self.name}_nbytes"

        lines += [
            f"buffer, {temp_buffer} = buffer[:offset + {nbytes}], buffer",
            f"if len(buffer) < offset + {nbytes}:",
            f"    cls.{self.name}.report_insufficient_bytes(buffer, offset, {nbytes}{dump_arg})",
            unpack_line,
            "if offset < len(buffer):",
            f"    cls.{self.name}.report_extra_bytes(buffer[offset:]{dump_arg})",
            f"buffer = {temp_buffer}",
        ]

    @staticmethod
    def report_insufficient_bytes(
        buffer: bytes, offset: int, nbytes: int, dump: Optional[Record] = None
    ):
        """Add unconsumed bytes leftover from unpacking to dump summary."""
        if dump is None:
            raise InsufficientMemoryError(
                "insufficient bytes, redo-ing to include dump"
            )

        getbytes(buffer, offset, dump, nbytes)

    @staticmethod
    def report_extra_bytes(extra_bytes: bytes, dump: Optional[Record] = None) -> None:
        """Add unconsumed bytes leftover from unpacking to dump summary."""
        if dump is not None:
            for i in range(0, len(extra_bytes), 16):
                if i:
                    dump.add_record(memory=extra_bytes[i : i + 16])
                else:
                    dump.add_record(
                        separate=True,
                        value="<excess bytes>",
                        memory=extra_bytes[i : i + 16],
                    )

        raise ExcessMemoryError(extra_bytes)


def sized_member(
    doc: str = "",
    *,
    fmt: Format,
    size: Any,  # must be Member, checked at runtime
    ratio: float = 1,
    offset: int = 0,
    default: Any = NO_DEFAULT,
    ignore: bool = False,
    readonly: bool = False,
    argrepr: Optional[str] = None,
) -> Any:
    """Sized structure member definition.

    :param doc: accessor documentation string
    :param fmt: member format, default uses type annotation
    :param size: member property which controls size
    :param int ratio: number of bytes per increment of size member
    :param int offset: difference in size (in bytes)
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """
    return SizedMember(
        doc, fmt, size, ratio, offset, default, ignore, readonly, argrepr
    )
