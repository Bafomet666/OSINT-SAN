"""IFD SLONG tag structure parser module."""

from exif.ifd_tag._base import Base as BaseIfdTag


class Slong(BaseIfdTag):
    """IFD SLONG tag structure parser class."""

    def modify(self, value):  # pragma: no cover
        """Modify tag value.

        :param value: new tag value
        :type value: corresponding Python type

        """
        raise NotImplementedError(
            "this package does not yet support setting SLONG tags since no SLONG tags "
            "exist in EXIF specification"
        )

    def read(self):  # pragma: no cover
        """Read tag value.

        :returns: tag value
        :rtype: corresponding Python type

        """
        raise NotImplementedError(
            "this package does not yet support setting SLONG tags since no SLONG tags "
            "exist in EXIF specification"
        )
