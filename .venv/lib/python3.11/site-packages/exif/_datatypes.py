"""Package EXIF-specific datatypes."""

from enum import IntEnum, IntFlag

from plum.array import ArrayX
from plum.bigendian import uint16, uint32
from plum.bitfields import BitFields, bitfield
from plum.enum import EnumX
from plum.littleendian import uint16 as uint16_l, uint32 as uint32_l
from plum.structure import (
    member,
    sized_member,
    Structure,
)


class TiffByteOrder(IntEnum):
    """TIFF Header Byte Order Indicator"""

    LITTLE = 0x4949
    BIG = 0x4D4D


tiff_byte_order = EnumX(
    enum=TiffByteOrder,
    nbytes=2,
    byteorder="big",
    signed=False,
    strict=True,
    name="tiff_byte_order",
)
BYTE_ORDER_MAP = {TiffByteOrder.LITTLE: uint32_l, TiffByteOrder.BIG: uint32}


class TiffHeader(Structure):
    """TIFF Header"""

    byte_order: int = member(fmt=tiff_byte_order)
    reserved: int = member(fmt=uint16)
    ifd_offset: int = member(fmt=BYTE_ORDER_MAP.__getitem__, fmt_arg=byte_order)  # type: ignore


class ExifType(IntEnum):
    """EXIF Tag Types"""

    EMPTY = 0
    BYTE = 1
    ASCII = 2
    SHORT = 3
    LONG = 4
    RATIONAL = 5
    UNDEFINED = 7
    SSHORT = 8
    SLONG = 9
    SRATIONAL = 10


exif_type = EnumX(
    enum=ExifType,
    nbytes=2,
    byteorder="big",
    signed=False,
    name="exif_type",
)
exif_type_le = EnumX(
    enum=ExifType, nbytes=2, byteorder="little", signed=False, name="exif_type"
)


class IfdTag(Structure):
    """IFD Tag"""

    tag_id: int = member(fmt=uint16)
    type: int = member(fmt=exif_type)
    value_count: int = member(fmt=uint32)
    value_offset: int = member(fmt=uint32)


class IfdTagLe(Structure):
    """IFD Tag (Little Endian)"""

    tag_id: int = member(fmt=uint16_l)
    type: int = member(fmt=exif_type_le)
    value_count: int = member(fmt=uint32_l)
    value_offset: int = member(fmt=uint32_l)


ifd_tag_array = ArrayX(fmt=IfdTag, name="ifd_tag")
ifd_tag_array_le = ArrayX(fmt=IfdTagLe, name="ifd_tag_le")


class Ifd(Structure):
    """IFD Segment"""

    count: int = member(fmt=uint16, compute=True)  # type: ignore
    tags: list = sized_member(size=count, fmt=ifd_tag_array, ratio=IfdTag.nbytes)  # type: ignore
    next: int = member(fmt=uint32)


class IfdLe(Structure):
    """IFD Segment (Little Endian)"""

    count: int = member(fmt=uint16_l, compute=True)  # type: ignore
    tags: list = sized_member(size=count, fmt=ifd_tag_array_le, ratio=IfdTagLe.nbytes)  # type: ignore
    next: int = member(fmt=uint32_l)


class FlashReturn(
    IntFlag
):  # FUTURE: Remove `IntFlag` sublclass to address below Pylint suppression (and other uses)
    """Flash status of returned light."""

    NO_STROBE_RETURN_DETECTION_FUNCTION = 0
    RESERVED = 1
    STROBE_RETURN_LIGHT_DETECTED = 2
    STROBE_RETURN_LIGHT_NOT_DETECTED = 3  # pylint: disable=implicit-flag-alias


class FlashMode(IntFlag):
    """Flash mode of the camera."""

    UNKNOWN = 0
    COMPULSORY_FLASH_FIRING = 1
    COMPULSORY_FLASH_SUPPRESSION = 2
    AUTO_MODE = 3  # pylint: disable=implicit-flag-alias


class Flash(BitFields, nbytes=1):  # type: ignore
    """Status of the camera's flash when the image was taken. (Reported by the ``flash`` tag.)"""

    flash_fired: bool = bitfield(typ=bool, size=1)
    flash_return: FlashReturn = bitfield(typ=FlashReturn, size=2)
    flash_mode: FlashMode = bitfield(typ=FlashMode, size=2)
    flash_function_not_present: bool = bitfield(typ=bool, size=1)
    red_eye_reduction_supported: bool = bitfield(typ=bool, size=1)
    reserved: int = bitfield(typ=int, size=1)
