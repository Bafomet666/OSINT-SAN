"""Decimal to bytes and bytes to decimal transform."""

from decimal import Decimal, InvalidOperation
from typing import Optional, Union, Tuple, List
from plum.transform import Transform
from plum.dump import Record
from plum.exceptions import InsufficientMemoryError
from plum._getbytes import getbytes
from ._typing import ByteOrderHint


class DecimalX(Transform):

    """Decimal to bytes and bytes to decimal transform."""

    __nbytes__: int
    __bdns__: Tuple[ByteOrderHint, int, int, bool]
    __precision__: int

    def __init__(
        self,
        nbytes: int,
        precision: int,
        byteorder: ByteOrderHint = "little",
        *,
        signed: bool = False,
        name: Optional[str] = None,
    ) -> None:
        if name is None:
            name = f"Decimal (precision={precision})"

        super().__init__(name, hint="Decimal")

        assert nbytes > 0
        assert byteorder in {"big", "little"}
        assert precision >= 0

        self.__nbytes__ = nbytes
        divisor = 10**precision
        self.__bdns__ = byteorder, divisor, nbytes, signed
        self.__precision__ = precision

    @property
    def byteorder(self) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        return self.__bdns__[0]

    @property
    def signed(self) -> bool:
        """Signed decimal."""
        return self.__bdns__[3]

    @property
    def precision(self) -> int:
        """Precision."""
        return self.__precision__

    def __pack__(
        self,
        value: Union[int, float, str, Decimal],
        pieces: List[bytes],
        dump: Optional[Record] = None,
    ) -> None:
        byteorder, divisor, nbytes, signed = self.__bdns__

        try:
            decimal_value = Decimal(value)
        except InvalidOperation:
            raise ValueError(
                f"Value {value!r} cannot be converted to decimal."
            ) from None

        decimal_value *= divisor
        int_value = int(decimal_value.to_integral_value())
        if dump is None:
            pieces.append(int_value.to_bytes(nbytes, byteorder, signed=signed))
        else:
            dump.value = repr(value)

            piece = int_value.to_bytes(nbytes, byteorder, signed=signed)

            dump.value = value
            dump.memory = piece

            pieces.append(piece)

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[Decimal, int]:
        byteorder, divisor, nbytes, signed = self.__bdns__

        if dump is None:
            end = offset + nbytes

            if len(buffer) < end:
                raise InsufficientMemoryError("too few bytes to unpack")

            int_value = int.from_bytes(buffer[offset:end], byteorder, signed=signed)
            decimal_value = Decimal(int_value) / divisor
            return decimal_value, end

        chunk, end = getbytes(buffer, offset, dump, nbytes)

        int_value = int.from_bytes(chunk, byteorder, signed=signed)

        decimal_value = Decimal(int_value) / divisor
        dump.value = decimal_value
        return decimal_value, end
