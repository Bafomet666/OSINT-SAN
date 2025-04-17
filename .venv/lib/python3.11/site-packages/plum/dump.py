# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Pack/unpack bytes summary."""

from enum import Enum
from typing import Any, Generator, List, Tuple, Union


class Base(list):

    """Dump/Record Base class."""

    def add_record(
        self,
        access: str = "",
        value: Any = "",
        bits: Union[Tuple[int, int], None] = None,
        memory: bytes = b"",
        fmt: Any = "",
        separate: bool = False,
    ) -> "Record":
        """Add child record.

        :param access: access description
        :param value: representation of value associated with bytes
        :param bits: start, end bit offset (None -> not a bit field)
        :param memory: bytes
        :param fmt: bytes format
        :param separate: add separator before row

        """
        # pylint: disable=too-many-arguments
        record = Record(access, value, bits, memory, fmt, separate)
        self.append(record)
        return record

    def add_extra_bytes(self, access: str, memory: bytes):
        """Add records listing bytes without access/value descriptions.

        :param access: access description
        :param memory: memory bytes

        """
        for i in range(0, len(memory), 16):
            self.add_record(access=access, memory=memory[i : i + 16])
            access = ""


class Record(Base):

    """Pack/unpack bytes summary.

    :param access: access description
    :param value: representation of value associated with bytes
    :param bits: start, end bit offset (None -> not a bit field)
    :param memory: memory bytes
    :param fmt: class name
    :param separate: add separator before row

    """

    # pylint: disable=too-many-instance-attributes

    def __init__(
        self,
        access: str = "",
        value: Any = "",
        bits: Union[Tuple[int, int], None] = None,
        memory: bytes = b"",  # pylint: disable=used-before-assignment ???
        fmt: Any = "",
        separate: bool = False,
    ) -> None:
        # pylint: disable=too-many-arguments
        super().__init__()

        self.access = access
        self._value = value
        self._bits = bits
        self.memory = memory
        self.fmt = fmt
        self.separate = separate

    def __repr__(self):  # pragma: no cover
        return (
            f"Record("
            f"bits={self.bits!r}, "
            f"access={self.access!r}, "
            f"value={self.value}, "
            f"memory={self.memory}, "
            f"fmt={self.fmt}, "
            f"records={list(self)})"
        )

    def iter_records(
        self, indent: int = 0
    ) -> Generator[Tuple[int, "Record"], None, None]:
        """Iterate dump records."""
        yield indent, self
        for record in self:
            yield from record.iter_records(indent + 1)

    @property
    def bits(self) -> str:
        """Bit field representation."""
        if self._bits is None:
            bits = ""
        else:
            lsb, size = self._bits

            if size == 1:
                bits = f"[{lsb}]"
            else:
                bits = f"[{lsb}:{lsb + size}]"

        return bits

    @property
    def value(self) -> Any:
        """Value representation."""
        # FUTURE - Any return really should be str but mypy complains
        #          leave this return self._value and leave application
        #          convert?
        if isinstance(self._value, Enum):
            return repr(self._value).split(":", 1)[0][1:]

        return str(self._value)

    @value.setter
    def value(self, value: Any) -> None:
        """Value representation."""
        self._value = value

    @property
    def fmt(self) -> str:
        """Entry format."""
        return self._fmt

    @fmt.setter
    def fmt(self, value: Any) -> None:
        if not isinstance(value, str):
            if hasattr(value, "name"):
                # plum data transform
                value = value.name
            elif hasattr(value, "__name__"):
                # class (e.g. enumeration, int, bool, etc.)
                value = value.__name__
            else:
                value = str(value)

        self._fmt = value

    @property
    def is_blank(self):
        """Has blank access, value, memory, and format fields."""
        return (
            all(x == "" for x in (self._fmt, self.access, self._value))
            and self.memory == b""
        )


class Dump(Base):

    """Pack/unpack bytes summary.

    :param offset: master byte offset

    """

    def __init__(self, offset: int = 0) -> None:
        super().__init__()
        self.offset: int = offset

    def __repr__(self):  # pragma: no cover
        return f"Dump({list(self)})"

    def __call__(self) -> None:
        print(self)

    def iter_records(self) -> Generator[Tuple[int, "Record"], None, None]:
        """Iterate dump records, yield (level, record) pairs."""
        for record in self:
            yield from record.iter_records()

    @staticmethod
    def _get_bytes_column_cells(records) -> List[str]:
        bitfield_size = 0
        cells = []
        for record in records:
            memory = record.memory
            if memory:
                cells.append(" ".join("{:02x}".format(c) for c in memory))
                bitfield_size = len(memory) * 8
            elif record._bits is None:  # pylint: disable=protected-access
                cells.append("")
            else:
                value = record._value  # pylint: disable=protected-access
                chars = ["."] * bitfield_size
                offset, size = record._bits  # pylint: disable=protected-access
                while size:
                    try:
                        chars[offset] = str(value & 1)
                    except (IndexError, TypeError):  # pragma: no cover
                        # sometimes records are half baked during a transform and didn't
                        # get a chance to complete before a problem occurred
                        break
                    value >>= 1
                    offset += 1
                    size -= 1
                chars.reverse()
                for i in range(bitfield_size - 8, 0, -8):
                    chars[i:i] = [" "]
                cells.append("".join(chars))
        return cells

    def _get_offset_column_cells(self, records) -> List[str]:
        bits = [record.bits for record in records]

        # make bit offset information uniform in length
        if any(bits):
            fmt = "{:%ds}" % max(len(bits_desc) for bits_desc in bits)
            bits = [fmt.format(bits_desc) for bits_desc in bits]

        # compute offset cells (with bit descriptions appended on)
        nbytes = sum(len(record.memory) for record in records)
        offset_template = "{:%dd}" % len(str(nbytes + self.offset))
        filler = " " * len(str(nbytes))
        consumed = 0
        offsets = []
        for record, bits_desc in zip(records, bits):
            if record.memory:
                byte_offset = offset_template.format(self.offset + consumed)
                consumed += len(record.memory)
            else:
                byte_offset = filler
            offsets.append(byte_offset + bits_desc)

        return offsets

    def _get_lines(self) -> Generator[str, None, None]:
        if len(self):  # pylint: disable=len-as-condition
            indents, records = zip(*self.iter_records())
        else:
            indents, records = (0,), (Record(),)

        accesses = [record.access.replace("(.)", "") for record in records]

        # look for things like this and get rid of excess indentation
        # +--------+-------------+-----------+-------+-----------------+
        # | Offset | Access      | Value     | Bytes | Format          |
        # +--------+-------------+-----------+-------+-----------------+
        # |        |             |           |       | CustomStructure |
        # | 0      |   [0] (.m1) | 258       | 02 01 | uint16          |
        # | 2      |   [1] (.m2) | <invalid> | 00    | CustomError     |
        # +--------+-------------+-----------+-------+-----------------+
        if all(indent or not access for indent, access in zip(indents, accesses)):
            indents = tuple(indent - 1 if indent else 0 for indent in indents)

        columns = [
            ["Offset"] + self._get_offset_column_cells(records),
            # 'Access' gets inserted here
            ["Value"] + [record.value for record in records],
            ["Bytes"] + self._get_bytes_column_cells(records),
            ["Format"] + [record.fmt for record in records],
        ]

        if any(accesses):
            columns[1:1] = [
                ["Access"]
                + ["  " * indent + access for indent, access in zip(indents, accesses)]
            ]

        column_widths = [max([len(cell) for cell in column]) for column in columns]

        border = "+{}+".format("+".join("-" * (n + 2) for n in column_widths))
        row_template = "|{}|".format("|".join(" {:%ds} " % n for n in column_widths))

        rows = list(zip(*columns))
        separators = [record.separate for record in records]
        separators[0] = False

        yield border
        yield row_template.format(*rows.pop(0))  # header names
        yield border
        for cells, separate in zip(rows, separators):
            if separate:
                yield border
            yield row_template.format(*cells)
        yield border

    def __str__(self) -> str:
        return "\n".join(self._get_lines())

    def trim_blank_record(self):
        """Remove first record and move its child records up if nothing to show."""
        first_record = self[0]
        if first_record.is_blank:
            self[:] = first_record[:]
