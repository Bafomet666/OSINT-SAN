"""IFD LONG tag structure parser module."""

from exif.ifd_tag._base import Base as BaseIfdTag


class Long(BaseIfdTag):
    """IFD LONG tag structure parser class."""

    def modify(self, value):
        """Modify tag value.

        :param value: new tag value
        :type value: corresponding Python type

        """
        self.tag_view.value_offset.set(value)

    def read(self):
        """Read tag value.

        This method does not contain logic for unpacking multiple values since the EXIF standard (v2.2) does not list
        any IFD tags of LONG type with a count greater than 1.

        :returns: tag value
        :rtype: corresponding Python type

        """
        return int(self.tag_view.value_offset)
