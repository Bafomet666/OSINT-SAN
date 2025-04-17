# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Transform conformance test case base class."""

from textwrap import wrap
from typing import Any, Generator, List, Optional, Tuple, Type, Union

from .bigendian import uint8
from .buffer import Buffer
from .data import Data
from .exceptions import (
    ExcessMemoryError,
    InsufficientMemoryError,
    SizeError,
    UnpackError,
)
from .transform import Transform
from .utilities import (
    pack,
    pack_and_dump,
    unpack,
    unpack_and_dump,
)

# pylint: disable=unidiomatic-typecheck,no-member


class CaseData:  # pylint: disable=too-many-instance-attributes

    """Conformance test case stimulus and expectations."""

    fmt: Union[Type[Data], Transform]
    """Transform to test."""

    bindata: bytes
    """Expected packed bytes."""

    values: Tuple[Any, ...]
    """Expected value when unpacked, followed by alternative packable values."""

    dump: str
    """Expected dump of sample plum type instance."""

    nbytes: Optional[int]
    """Size of plum type being tested."""

    excess: str
    """Expected exception message of unpack() method when 1 byte extra."""

    shortage: str
    """Expected exception message of unpack() method when short 1 byte."""

    implementation: Optional[str] = None
    """Expected generated implementation code."""

    def __init__(
        self,
        *,
        fmt: Union[Type[Data], Transform],
        bindata: bytes,
        values: Tuple[Any, ...],
        dump: str,
        nbytes: Optional[int],
        excess: str,
        shortage: str,
        implementation: Optional[str] = None,
    ):
        self.fmt = fmt
        self.bindata = bindata
        self.values = values
        self.dump = dump
        self.nbytes = nbytes
        self.excess = excess
        self.shortage = shortage
        self.implementation = implementation


class Case:  # pylint: disable=too-many-public-methods

    """Test basic API conformance and utility usage."""

    data: CaseData

    def test_transform_nbytes_property(self):
        """Test transform's nbytes property."""
        try:
            nbytes = self.data.fmt.nbytes
        except SizeError:
            nbytes = None

        assert nbytes == self.data.nbytes

    def test_data_store_nbytes_property(self):
        """Test data store nbytes property."""
        if not isinstance(self.data.fmt, Transform) and issubclass(self.data.fmt, Data):
            assert unpack(self.data.fmt, self.data.bindata).nbytes == len(
                self.data.bindata
            )

    def test_data_store_dump(self):
        """Test data store dump property."""
        if not isinstance(self.data.fmt, Transform) and issubclass(self.data.fmt, Data):
            assert str(unpack(self.data.fmt, self.data.bindata).dump) == self.data.dump

    def test_utility_pack(self):
        """Test utility pack() function."""
        for value in self.data.values:
            assert pack(value, self.data.fmt) == self.data.bindata

    def test_transform_pack(self):
        """Test transform pack() method."""
        for value in self.data.values:
            assert self.data.fmt.pack(value) == self.data.bindata

    def test_data_store_ipack(self):
        """Test data store ipack() method."""
        if not isinstance(self.data.fmt, Transform) and issubclass(self.data.fmt, Data):
            assert unpack(self.data.fmt, self.data.bindata).ipack() == self.data.bindata

    def test_utility_pack_and_dump(self):
        """Test utility pack_and_dump() function."""
        for value in self.data.values:
            buffer, dump = pack_and_dump(value, self.data.fmt)
            assert str(dump) == self.data.dump
            assert buffer == self.data.bindata

    def test_transform_pack_and_dump(self):
        """Test transfrom pack_and_dump() method."""
        for value in self.data.values:
            buffer, dump = self.data.fmt.pack_and_dump(value)
            assert str(dump) == self.data.dump
            assert buffer == self.data.bindata

    def test_data_store_ipack_and_dump(self):
        """Test data store ipack_and_dump() method."""
        if not isinstance(self.data.fmt, Transform) and issubclass(self.data.fmt, Data):
            datastore = unpack(self.data.fmt, self.data.bindata)
            buffer, dump = datastore.ipack_and_dump()
            assert str(dump) == self.data.dump
            assert buffer == self.data.bindata

    def test_utility_unpack(self):
        """Test utility unpack() function."""
        expected_value = self.data.values[0]
        item = unpack(self.data.fmt, self.data.bindata)
        assert type(item) is type(expected_value)
        assert item == expected_value

    def test_transform_unpack(self):
        """Test transform unpack() method."""
        expected_value = self.data.values[0]
        item = self.data.fmt.unpack(self.data.bindata)
        assert type(item) is type(expected_value)
        assert item == expected_value

    def test_buffer_unpack(self):
        """Test Buffer.unpack() method (can unpack from the middle)."""
        try:
            self.data.fmt.nbytes
        except SizeError:
            # must be greedy transform
            with Buffer(b"\x00" + self.data.bindata) as buffer:
                head = buffer.unpack(uint8)
                item = buffer.unpack(self.data.fmt)
                tail = 0x99
        else:
            with Buffer(b"\x00" + self.data.bindata + b"\x99") as buffer:
                head = buffer.unpack(uint8)
                item = buffer.unpack(self.data.fmt)
                tail = buffer.unpack(uint8)

        expected_value = self.data.values[0]

        assert head == 0
        assert type(item) is type(expected_value)
        assert item == expected_value
        assert tail == 0x99

    def test_utility_unpack_and_dump(self):
        """Test utility unpack_and_dump() function."""
        expected_value = self.data.values[0]
        item, dump = unpack_and_dump(self.data.fmt, self.data.bindata)
        assert str(dump) == self.data.dump
        assert type(item) is type(expected_value)
        assert item == expected_value

    def test_transform_unpack_and_dump(self):
        """Test transform unpack_and_dump() method."""
        expected_value = self.data.values[0]
        item, dump = self.data.fmt.unpack_and_dump(self.data.bindata)
        assert str(dump) == self.data.dump
        assert type(item) is type(expected_value)
        assert item == expected_value

    def test_buffer_unpack_and_dump(self):
        """Test Buffer.unpack_and_dump() method (can unpack from the middle)."""
        try:
            self.data.fmt.nbytes
        except SizeError:
            # must be greedy transform
            with Buffer(b"\x00" + self.data.bindata) as buffer:
                head = buffer.unpack(uint8)
                item, dump = buffer.unpack_and_dump(self.data.fmt)
                tail = 0x99
        else:
            with Buffer(b"\x00" + self.data.bindata + b"\x99") as buffer:
                head = buffer.unpack(uint8)
                item, dump = buffer.unpack_and_dump(self.data.fmt)
                tail = buffer.unpack(uint8)

        expected_value = self.data.values[0]

        # change dump offset to make consistent with baselined dump
        assert dump.offset == 1
        dump.offset = 0

        assert str(dump) == self.data.dump
        assert head == 0
        assert type(item) is type(expected_value)
        assert item == expected_value
        assert tail == 0x99

    def test_unpack_shortage(self):
        """Test unpack() usage with insufficient bytes."""
        if self.data.shortage not in {"N/A"} and self.data.bindata:
            try:
                unpack(self.data.fmt, self.data.bindata[:-1])
            except UnpackError as exception:
                assert wrap_message(exception) == self.data.shortage
                assert isinstance(exception.__context__, InsufficientMemoryError)
            else:  # pragma: no cover
                raise AssertionError("unpack() did not raise an exception")

            if not isinstance(self.data.fmt, Transform) and issubclass(
                self.data.fmt, Data
            ):
                try:
                    self.data.fmt.unpack(self.data.bindata[:-1])
                except UnpackError as exception:
                    assert wrap_message(exception) == self.data.shortage
                    assert isinstance(exception.__context__, InsufficientMemoryError)
                else:  # pragma: no cover
                    raise AssertionError("unpack() did not raise an exception")

    def test_unpack_excess(self):
        """Test unpack() usage with excess bytes."""
        if self.data.excess not in {"N/A"}:
            try:
                unpack(self.data.fmt, self.data.bindata + b"\x99")
            except UnpackError as exception:
                assert wrap_message(exception) == self.data.excess
                assert isinstance(exception.__context__, ExcessMemoryError)
            else:  # pragma: no cover
                raise AssertionError("unpack() did not raise an exception")

            if not isinstance(self.data.fmt, Transform) and issubclass(
                self.data.fmt, Data
            ):
                try:
                    self.data.fmt.unpack(self.data.bindata + b"\x99")
                except UnpackError as exception:
                    assert wrap_message(exception) == self.data.excess
                    assert isinstance(exception.__context__, ExcessMemoryError)
                else:  # pragma: no cover
                    raise AssertionError("unpack() did not raise an exception")

    def test_implementation(self):
        """Test generated code matches baseline."""
        if self.data.implementation is not None:
            assert self.data.fmt.implementation == self.data.implementation


def wrap_message(exc: BaseException) -> str:
    """Line wrap exception message.

    Wrap exception message lines that exceed 80 characters.
    Detect and leave undisturbed `dump()` tables.

    """
    lines_out = []
    queue: List[str] = []
    for line in str(exc).split("\n"):
        stripped_line = line.strip()
        if not stripped_line or (stripped_line[0] in "+|"):
            lines_out.extend(wrap("\n".join(queue)))
            lines_out.append(line)
            queue = []
        else:
            queue.append(line)

    if queue:  # pragma: no cover
        lines_out.extend(wrap("\n".join(queue)))

    while lines_out and not lines_out[0]:
        lines_out.pop(0)

    return "\n".join(lines_out)


def _iter_lines(code: str, methodname: str) -> Generator[str, None, None]:
    lines = code.split("\n")

    active = False

    pattern = f"def {methodname}"

    for line in lines:
        lstripped_line = line.lstrip()

        if lstripped_line.startswith(pattern):
            active = True
        elif lstripped_line and lstripped_line == line:
            active = False

        if active:
            yield line


def extract_method_code(code: str, methodname: str) -> str:
    """Get code for single method from that of many methods."""
    return "\n".join(_iter_lines(code, methodname))
