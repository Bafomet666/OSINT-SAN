"""Utility functions."""

from exif._datatypes import ExifType


def pack_into(datatype, buffer, offset=0):
    """Pack datatype bytes into buffer."""
    buffer[offset : offset + datatype.nbytes] = datatype.ipack()


def value_fits_in_ifd_tag(tag_dt):
    """Determine if value fits inside the IFD tag itself.

    :param Structure tag_dt: IFD tag datatype instance
    :returns: value fits inside IFD tag
    :rtype: bool

    """
    is_value_in_ifd_tag_itself = False
    is_value_in_ifd_tag_itself |= tag_dt.type == ExifType.EMPTY
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.BYTE and tag_dt.value_count <= 4
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.ASCII and tag_dt.value_count <= 4
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.UNDEFINED and tag_dt.value_count <= 4
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.SHORT and tag_dt.value_count <= 2
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.SSHORT and tag_dt.value_count <= 2
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.LONG and tag_dt.value_count <= 1
    )
    is_value_in_ifd_tag_itself |= (
        tag_dt.type == ExifType.SLONG and tag_dt.value_count <= 1
    )
    # RATIONAL and SRATIONAL are never in ifd tag itself

    return is_value_in_ifd_tag_itself
