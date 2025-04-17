"""IFD SHORT tag structure parser module."""

from plum.bigendian import uint16
from plum.littleendian import uint16 as uint16_le

from exif._constants import (
    ATTRIBUTE_ID_MAP,
    ColorSpace,
    ExposureMode,
    ExposureProgram,
    LightSource,
    MeteringMode,
    Orientation,
    ResolutionUnit,
    Saturation,
    SceneCaptureType,
    SensingMethod,
    Sharpness,
    WhiteBalance,
)
from exif._datatypes import Flash, TiffByteOrder
from exif.ifd_tag._base import Base as BaseIfdTag


class Short(BaseIfdTag):
    """IFD SHORT tag structure parser class."""

    CUSTOM_TYPES_MAP = {
        ATTRIBUTE_ID_MAP["flash"]: Flash,
    }

    ENUMS_MAP = {
        ATTRIBUTE_ID_MAP["color_space"]: ColorSpace,
        ATTRIBUTE_ID_MAP["exposure_mode"]: ExposureMode,
        ATTRIBUTE_ID_MAP["exposure_program"]: ExposureProgram,
        ATTRIBUTE_ID_MAP["metering_mode"]: MeteringMode,
        ATTRIBUTE_ID_MAP["light_source"]: LightSource,
        ATTRIBUTE_ID_MAP["orientation"]: Orientation,
        ATTRIBUTE_ID_MAP["resolution_unit"]: ResolutionUnit,
        ATTRIBUTE_ID_MAP["saturation"]: Saturation,
        ATTRIBUTE_ID_MAP["scene_capture_type"]: SceneCaptureType,
        ATTRIBUTE_ID_MAP["sensing_method"]: SensingMethod,
        ATTRIBUTE_ID_MAP["sharpness"]: Sharpness,
        ATTRIBUTE_ID_MAP["white_balance"]: WhiteBalance,
    }

    def __init__(self, tag_offset, app1_ref):
        super().__init__(tag_offset, app1_ref)

        if self._app1_ref.endianness == TiffByteOrder.BIG:
            self._uint16_cls = uint16
        else:
            self._uint16_cls = uint16_le

    def modify(self, value):
        """Modify tag value.

        This method does not contain logic for unpacking multiple values since the EXIF standard (v2.2) does not list
        any IFD tags of SHORT type with a count greater than 1.

        :param value: new tag value
        :type value: corresponding Python type

        """
        self._uint16_cls.view(
            self._app1_ref.body_bytes, self.tag_view.value_offset.__offset__
        ).set(int(value))

    def read(self):
        """Read tag value.

        This method does not contain logic for unpacking multiple values since the EXIF standard (v2.2) does not list
        any IFD tags of SHORT type with a count greater than 1.

        :returns: tag value
        :rtype: corresponding Python type

        """
        as_int = int(
            self._uint16_cls.view(
                self._app1_ref.body_bytes, self.tag_view.value_offset.__offset__
            )
        )

        try:
            enum_type = self.ENUMS_MAP[int(self.tag_view.tag_id)]
        except KeyError:
            try:
                custom_type = self.CUSTOM_TYPES_MAP[int(self.tag_view.tag_id)]
            except KeyError:
                retval = as_int  # leave return value as-is
            else:
                retval = custom_type.unpack(bytes([as_int]))
        else:
            retval = enum_type(as_int)

        return retval
