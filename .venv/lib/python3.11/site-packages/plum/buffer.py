# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bytes sequence incremental unpacker."""

from .dump import Dump
from .exceptions import ExcessMemoryError, ImplementationError, UnpackError
from .items import ItemsFormat, items


class Buffer(bytes):

    """Bytes sequence incremental unpacker."""

    offset: int

    def __new__(cls, *args, **kwargs):
        instance = bytes.__new__(cls, *args, **kwargs)
        instance.offset = 0
        return instance

    def unpack(self, fmt: ItemsFormat):
        """Unpack value from formatted bytes at current buffer offset.

        :raises: ``UnpackError`` if insufficient bytes or value error

        """
        try:
            # None -> dump
            value, self.offset = items.__unpack__(self, self.offset, None, fmt)
        except Exception as exc:
            # do it over to include dump in exception message
            self.unpack_and_dump(fmt)
            raise ImplementationError() from exc  # pragma: no cover

        return value

    def unpack_and_dump(self, fmt: ItemsFormat):
        """Unpack value from bytes at current offset and produce a packed bytes summary.

        :raises: ``UnpackError`` if insufficient bytes or value error

        """
        offset = self.offset

        dump = Dump(offset=offset)

        try:
            # empty record added so so pack always called with a Record instance
            value, self.offset = items.__unpack__(self, offset, dump.add_record(), fmt)
        except Exception as exc:
            dump.trim_blank_record()
            raise UnpackError(dump, exc) from exc

        dump.trim_blank_record()

        return value, dump

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:  # don't check if already an exception
            extra_bytes = self[self.offset :]

            if extra_bytes:
                raise ExcessMemoryError(extra_bytes)
