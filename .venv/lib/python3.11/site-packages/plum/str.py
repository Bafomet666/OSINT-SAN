# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a string."""

import codecs
from typing import List, Optional, Tuple, Union

from ._getbytes import getbytes
from .dump import Record
from .exceptions import InsufficientMemoryError
from .transform import Transform


def _decode_str_bytes(buffer, decoder, zipped_char_bytes, zero_termination=False):
    reset = True
    for i, byte in enumerate(buffer):
        if reset:
            char_bytes = []
            zipped_char_bytes.append(["", char_bytes])
            reset = False

        if zero_termination and byte == 0:
            break

        char = decoder.decode(buffer[i : i + 1])
        char_bytes.append(byte)

        if char:
            zipped_char_bytes[-1][0] = char
            reset = True

    # FUTURE - test this
    # raise exception if bytes remain in decoder (character not complete)
    decoder.decode(b"", final=True)


def _encode_str_bytes(string, encoder, zipped_char_bytes):
    for char in string:
        zipped_char_bytes.append((char, encoder.encode(char)))

    assert not encoder.encode("", final=True)


def _iter_str_rows(zipped_char_bytes):
    row_index = 0
    row_chars, row_bytes = [], []

    for char, char_bytes in zipped_char_bytes:
        if len(char_bytes) + len(row_bytes) > 16:
            yield row_index, "".join(row_chars), bytearray(row_bytes)
            row_index += len(row_chars)
            row_chars, row_bytes = [], []

        row_chars.append(char)
        row_bytes += char_bytes

    if row_bytes:
        yield row_index, "".join(row_chars), bytearray(row_bytes)
    else:
        yield row_index, "", bytearray()


def _add_str_rows_to_dump(dump, zipped_char_bytes, buffer=None, string=None):
    nbytes = 0
    nchar = 0
    for index, chars, bytes_ in _iter_str_rows(zipped_char_bytes):
        dump.add_record(
            access=f"[{index}:{index + len(chars)}]", value=repr(chars), memory=bytes_
        )
        nbytes += len(bytes_)
        nchar += len(chars)

    if buffer:
        dump.add_extra_bytes("--error--", buffer[nbytes:])

    if string:
        string = string[nchar:]
        access = "--error--"
        for i in range(0, len(string), 16):
            dump.add_record(access).value = repr(string[i : i + 16])
            access = ""


def _add_str_bytes_to_dump(dump, buffer, decoder):
    zipped_char_bytes = []
    try:
        _decode_str_bytes(buffer, decoder, zipped_char_bytes)
    finally:
        _add_str_rows_to_dump(dump, zipped_char_bytes, buffer=buffer)


def _add_str_value_to_dump(dump, string, encoder):
    zipped_char_bytes = []
    try:
        _encode_str_bytes(string, encoder, zipped_char_bytes)
    finally:
        _add_str_rows_to_dump(dump, zipped_char_bytes, string=string)


class StrX(Transform):

    """String to bytes and bytes to string transform."""

    def __init__(
        self,
        encoding: str,
        errors: str = "strict",
        nbytes: Union[int, None] = None,
        pad: bytes = b"",
        zero_termination: bool = False,
        name: Optional[str] = None,
    ) -> None:
        # pylint: disable=too-many-arguments
        assert len(pad) <= 1

        if name is None:
            name = f"str ({encoding})"

        super().__init__(name, hint="str")

        codecs_info = codecs.lookup(encoding)

        self.__nbytes__ = nbytes
        self.__cenpz__ = codecs_info, errors, nbytes, pad, zero_termination

    @property
    def encoding(self) -> str:
        """Codecs encoding name."""
        codecs_info = self.__cenpz__[0]
        return codecs_info.name

    @property
    def errors(self) -> str:
        """Codecs error handling."""
        return self.__cenpz__[1]

    @property
    def pad(self) -> bytes:
        """Pad byte."""
        return self.__cenpz__[3]

    @property
    def zero_termination(self) -> bool:
        """Zero termination byte present."""
        return self.__cenpz__[4]

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[str, int]:
        # pylint: disable=too-many-branches,too-many-locals
        if dump is not None:
            return self.__unpack_and_dump__(buffer, offset, dump)

        codecs_info, errors, nbytes, pad, zero_termination = self.__cenpz__

        original_offset = offset

        if nbytes is None:
            chunk = buffer[offset:]
            offset += len(chunk)
        else:
            start = offset
            offset += nbytes
            chunk = buffer[start:offset]

            if len(chunk) < nbytes:
                raise InsufficientMemoryError(
                    "insufficient bytes for String, retry with dump"
                )

        if zero_termination:

            decoder = codecs_info.incrementaldecoder(errors)

            zipped_char_bytes: List[Tuple[str, bytes]] = []
            _decode_str_bytes(chunk, decoder, zipped_char_bytes, zero_termination=True)

            nstr_membytes = len(b"".join(bytes(b) for c, b in zipped_char_bytes))
            termination = chunk[nstr_membytes : nstr_membytes + 1]

            if termination != b"\x00":
                termination = b""

            if nbytes is None:
                offset = original_offset + nstr_membytes + len(termination)

            if termination != b"\x00":
                raise InsufficientMemoryError("no zero termination present")

            value = "".join(c for c, b in zipped_char_bytes)

        else:
            if pad and pad in chunk:
                chunk = chunk[: chunk.index(pad)]

            value = str(chunk, codecs_info.name, errors)

        return value, offset

    def __unpack_and_dump__(
        self, buffer: bytes, offset: int, dump: Record
    ) -> Tuple[str, int]:
        # pylint: disable=too-many-branches,too-many-locals
        codecs_info, errors, nbytes, pad, zero_termination = self.__cenpz__

        original_offset = offset

        chunk, offset = getbytes(buffer, offset, dump, nbytes)

        if zero_termination:

            decoder = codecs_info.incrementaldecoder(errors)

            dump.memory = b""

            zipped_char_bytes: List[Tuple[str, bytes]] = []
            try:
                _decode_str_bytes(
                    chunk, decoder, zipped_char_bytes, zero_termination=True
                )
            except UnicodeDecodeError:
                _add_str_rows_to_dump(dump, zipped_char_bytes, buffer=chunk)
                raise

            nstr_membytes = len(b"".join(bytes(b) for c, b in zipped_char_bytes))
            termination = chunk[nstr_membytes : nstr_membytes + 1]

            if termination == b"\x00":
                leftover_bytes = chunk[nstr_membytes + 1 :]
            else:
                leftover_bytes = chunk[nstr_membytes:]
                termination = b""

            if nbytes is None:
                offset = original_offset + nstr_membytes + len(termination)
                leftover_bytes = b""

            _add_str_rows_to_dump(dump, zipped_char_bytes)
            if termination:
                dump.add_record(access="--termination--", memory=bytes(termination))
            if leftover_bytes:
                dump.add_extra_bytes("--pad--", bytes(leftover_bytes))

            if termination != b"\x00":
                raise InsufficientMemoryError("no zero termination present")

            value = "".join(c for c, b in zipped_char_bytes)

        else:
            if pad and pad in chunk:
                i = chunk.index(pad)
                pad_bytes = chunk[i:]
                chunk = chunk[:i]
            else:
                pad_bytes = b""

            dump.memory = b""
            _add_str_bytes_to_dump(dump, chunk, codecs_info.incrementaldecoder(errors))

            if pad_bytes:
                dump.add_extra_bytes("--pad--", bytes(pad_bytes))

            value = str(chunk, codecs_info.name, errors)

        return value, offset

    def __pack__(
        self, value: str, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        if dump is not None:
            self.__pack_and_dump__(value, pieces, dump)

        else:
            codecs_info, errors, nbytes, pad, zero_termination = self.__cenpz__

            chunk = value.encode(codecs_info.name, errors)

            if zero_termination:
                chunk = chunk + b"\x00"

            actual_nbytes = len(chunk)

            if nbytes is not None:

                if actual_nbytes > nbytes:
                    raise TypeError(
                        f"number of string bytes ({actual_nbytes}) "
                        f"exceeds limit ({nbytes}) for {self!r}"
                    )

                if actual_nbytes < nbytes:
                    if not pad:
                        raise ValueError(
                            f"number of string bytes ({actual_nbytes}) "
                            f"falls short of ({nbytes}) for {self!r}"
                        )

                    chunk += pad * (nbytes - actual_nbytes)

            pieces.append(chunk)

    def __pack_and_dump__(self, value: str, pieces: List[bytes], dump: Record) -> None:
        codecs_info, errors, nbytes, pad, zero_termination = self.__cenpz__

        _add_str_value_to_dump(dump, value, codecs_info.incrementalencoder(errors))
        if zero_termination:
            dump.add_record("--termination--", memory=b"\x00")

        chunk = value.encode(codecs_info.name, errors)

        if zero_termination:
            chunk = chunk + b"\x00"

        actual_nbytes = len(chunk)

        if nbytes is not None:

            if actual_nbytes > nbytes:
                raise TypeError(
                    f"number of string bytes ({actual_nbytes}) "
                    f"exceeds limit ({nbytes}) for {self!r}"
                )

            if actual_nbytes < nbytes:
                if not pad:
                    raise ValueError(
                        f"number of string bytes ({actual_nbytes}) "
                        f"falls short of ({nbytes}) for {self!r}"
                    )
                pad = pad * (nbytes - actual_nbytes)
                chunk += pad

                dump.add_extra_bytes("--pad--", pad)

        pieces.append(chunk)
