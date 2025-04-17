# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bytes transform."""

from typing import List, Optional, Tuple, Union

from ._getbytes import getbytes
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform


class BytesX(Transform):

    """Bytes transform."""

    __np__: Tuple[Union[int, None], bytes]

    def __init__(
        self,
        nbytes: Optional[int] = None,
        pad: bytes = b"",
        name: Optional[str] = None,
    ) -> None:
        if name is None:
            if nbytes is None:
                descriptions = ["greedy"]
            else:
                descriptions = ["fixed"]

            if pad:
                descriptions.append("padded")

            name = f"bytes ({','.join(descriptions)})"

        super().__init__(name, hint="bytes")

        assert 0 <= len(pad) <= 1
        assert not (nbytes is None and pad), "must set nbytes when setting pad"

        self.__nbytes__ = nbytes
        self.__np__ = nbytes, pad

    @property
    def pad(self) -> bytes:
        """Pad byte."""
        return self.__np__[1]

    def __unpack__(
        self,
        buffer: bytes,
        offset: int,
        dump: Optional[Record] = None,
        nbytes: Optional[int] = None,
    ) -> Tuple[bytes, int]:
        # pylint: disable=arguments-differ
        if dump is not None:
            return self.__unpack_and_dump__(buffer, offset, dump, nbytes)

        nbytes_x, pad = self.__np__

        if nbytes is None:
            nbytes = nbytes_x

        if nbytes is None:
            value = bytes(buffer[offset:])
            offset += len(value)
        else:
            start = offset
            offset += nbytes
            value = bytes(buffer[start:offset])

            if len(value) < nbytes:
                raise InsufficientMemoryError("insufficient bytes")

            if pad:
                value = value.rstrip(pad)

        return value, offset

    def __unpack_and_dump__(
        self, buffer: bytes, offset: int, dump: Record, nbytes: Optional[int] = None
    ) -> Tuple[bytes, int]:
        # pylint: disable=arguments-differ
        nbytes_x, pad = self.__np__

        if nbytes is None:
            nbytes = nbytes_x

        try:
            value, offset = getbytes(buffer, offset, dump, nbytes)
        except InsufficientMemoryError:
            # getbytes() adds records in 16 byte chunks showing bytes it was able
            # to unpack, reassemble them as if operation was successful
            value = b"".join(subdump.memory for subdump in dump)
            del dump[:]
            for i in range(0, len(value), 16):
                chunk = value[i : i + 16]
                dump.add_record(
                    access=f"[{i}:{i + len(chunk)}]",
                    value=repr(chunk),
                    memory=chunk,
                )
            raise

        if nbytes is not None and pad:
            value = value.rstrip(pad)
            pad = pad * (nbytes - len(value))
        else:
            pad = b""

        dump.memory = b""
        if value:
            for i in range(0, len(value), 16):
                chunk = value[i : i + 16]
                dump.add_record(
                    access=f"[{i}:{i + len(chunk)}]",
                    value=repr(chunk),
                    memory=chunk,
                )
        else:
            dump.add_record(access="[0:0]", value=repr(value))

        for i in range(0, len(pad), 16):
            chunk = pad[i : i + 16]
            dump.add_record(
                access="--pad--",
                value=repr(chunk),
                memory=chunk,
            )

        return value, offset

    def __pack__(
        self,
        value: Union[bytes, bytearray],
        pieces: List[bytes],
        dump: Optional[Record] = None,
    ) -> None:
        if dump is not None:
            self.__pack_and_dump__(value, pieces, dump)

        else:
            nbytes, pad = self.__np__

            piece = bytes(value)

            if nbytes is not None:
                actual_nbytes = len(piece)

                if pad and actual_nbytes < nbytes:
                    piece += pad * (nbytes - actual_nbytes)

                elif actual_nbytes != nbytes:
                    raise ValueError(
                        f"expected length to be {nbytes} but instead found {actual_nbytes}"
                    )

            pieces.append(piece)

    def __pack_and_dump__(
        self,
        value: Union[bytes, bytearray],
        pieces: List[bytes],
        dump: Record,
    ) -> None:
        nbytes, pad = self.__np__

        piece = bytes(value)

        actual_nbytes = len(piece)

        if actual_nbytes:
            for i in range(0, actual_nbytes, 16):
                chunk = piece[i : i + 16]
                dump.add_record(
                    access=f"[{i}:{i + len(chunk)}]",
                    value=repr(chunk),
                    memory=chunk,
                )
        else:
            dump.add_record(access="[0:0]", value=repr(piece))

        if nbytes is not None and pad and actual_nbytes < nbytes:
            pad = pad * (nbytes - actual_nbytes)
            piece += pad

            for i in range(0, len(pad), 16):
                chunk = pad[i : i + 16]
                dump.add_record(
                    access="--pad--",
                    value=repr(chunk),
                    memory=chunk,
                )

        elif nbytes is not None and actual_nbytes != nbytes:
            raise ValueError(
                f"expected length to be {nbytes} but instead found {actual_nbytes}"
            )

        pieces.append(piece)
