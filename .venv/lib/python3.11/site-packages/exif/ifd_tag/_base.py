"""Base IFD tag structure parser module."""

from exif._datatypes import IfdTag, IfdTagLe, TiffByteOrder


class Base:
    """Base IFD tag structure parser class."""

    def __init__(self, tag_offset, app1_ref):
        self._tag_offset = tag_offset
        self._app1_ref = app1_ref

        if self._app1_ref.endianness == TiffByteOrder.BIG:
            self._ifd_tag_cls = IfdTag
        else:
            self._ifd_tag_cls = IfdTagLe

        self.tag_view = self._ifd_tag_cls.view(
            self._app1_ref.body_bytes, self._tag_offset
        )

    def __repr__(self):  # pragma: no cover
        return f"exif.ifd_tag.Base(tag_offset={self._tag_offset})"

    def modify(self, value):  # pragma: no cover
        """Modify tag value.

        :param value: new tag value
        :type value: corresponding Python type

        """
        raise NotImplementedError("cannot modify a base/unknown IFD tag instance")

    def read(self):  # pragma: no cover
        """Read tag value.

        :returns: tag value
        :rtype: corresponding Python type

        """
        raise NotImplementedError("cannot read a base/unknown IFD tag instance")

    def wipe(self):  # pragma: no cover
        """Wipe value pointer target bytes to null."""
