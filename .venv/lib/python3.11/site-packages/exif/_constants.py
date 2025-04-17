"""Package constants."""

# pylint: disable=too-few-public-methods

from enum import IntEnum


class ColorSpace(IntEnum):
    """Color space specifier."""

    SRGB = 1
    "sRBG"

    UNCALIBRATED = 0xFFFF
    "Uncalibrated or Other"


class ExifMarkers:
    """EXIF marker segments bytes."""

    SEG_PREFIX = b"\xff"
    """Generic Segment Prefix"""

    SOI = SEG_PREFIX + b"\xd8"
    """Start of Image"""

    APP1 = SEG_PREFIX + b"\xe1"
    """EXIF Attribute Information (Application Segment 1)"""

    APP2 = SEG_PREFIX + b"\xe2"
    """EXIF Extended Data (Application Segment 2)"""

    DQT = SEG_PREFIX + b"\xdb"
    """Quantization Table Definition"""

    DHT = SEG_PREFIX + b"\xc4"
    """Huffman Table Definition"""

    DRI = SEG_PREFIX + b"\xdd"
    """Restart Interoperability Definition"""

    SOF = SEG_PREFIX + b"\xc0"
    """Start of Frame"""

    SOS = SEG_PREFIX + b"\xda"
    """Start of Scan"""

    EOI = SEG_PREFIX + b"\xd9"
    """End of Image"""


class ExifTypes(IntEnum):
    """EXIF datatype indicator for IFD structure."""

    BYTE = 1
    """8-Bit Unsigned Integer"""

    ASCII = 2
    """Null-Terminated ASCII Codes"""

    SHORT = 3
    """16-Bit Unsigned Integer"""

    LONG = 4
    """32-Bit Unsigned Integer"""

    RATIONAL = 5
    """Two (Numerator and Denominator) LONGs"""

    SSHORT = 8
    """16-Bit Signed Integer"""

    SLONG = 9
    """32-Bit Signed Integer"""

    SRATIONAL = 10
    """Two (Numerator and Denominator) SLONGs"""


class ExposureMode(IntEnum):
    """Exposure mode set when the image was shot."""

    AUTO_EXPOSURE = 0
    """Auto Exposure"""

    MANUAL_EXPOSURE = 1
    """Manual Exposure"""

    AUTO_BRACKET = 2
    """Auto Bracket"""


class ExposureProgram(IntEnum):
    """Class of the program used by the camera to set exposure when the picture is taken."""

    NOT_DEFINED = 0
    """Not Defined"""

    MANUAL = 1
    """Manual"""

    NORMAL_PROGRAM = 2
    """Normal Program"""

    APERTURE_PRIORITY = 3
    """Aperture Priority"""

    SHUTTER_PRIORITY = 4
    """Shutter Priority"""

    CREATIVE_PROGRAM = 5
    """Creative Program (Biased Toward Depth of Field)"""

    ACTION_PROGRAM = 6
    """Action Program (Biased Toward Fast Shutter Speed)"""

    PORTRAIT_MODE = 7
    """Portrait Mode (For Closeup Photos with the Background out of Focus)"""

    LANDSCAPE_MODE = 8
    """Landscape Kode (For Landscape Photos with the Background in Focus)"""


class GpsAltitudeRef(IntEnum):
    """Altitude used as the reference altitude."""

    ABOVE_SEA_LEVEL = 0
    """Above Sea Level"""

    BELOW_SEA_LEVEL = 1
    """Below Sea Level"""


class LightSource(IntEnum):
    """Class of the program used by the camera to set exposure when the picture is taken."""

    UNKNOWN = 0
    """Unknown"""

    DAYLIGHT = 1
    """Daylight"""

    FLUORESCENT = 2
    """Fluorescent"""

    TUNGSTEN = 3
    """Tungsten (Incandescent Light)"""

    FLASH = 4
    """Flash"""

    FINE_WEATHER = 9
    """Fine Weather"""

    CLOUDY_WEATHER = 10
    """Cloudy Weather"""

    SHADE = 11
    """Shade"""

    DAYLIGHT_FLUORESCENT = 12
    """Daylight Fluorescent (D 5700 - 7100K)"""

    DAY_WHITE_FLUORESCENT = 13
    """Day White Fluorescent (N 4600 - 5400K)"""

    COOL_WHITE_FLUORESCENT = 14
    """Cool White Fluorescent (W 3900 - 4500K)"""

    WHITE_FLUORESCENT = 15
    """White Fluorescent (WW 3200 - 3700K)"""

    STANDARD_LIGHT_A = 17
    """Standard Light A"""

    STANDARD_LIGHT_B = 18
    """Standard Light B"""

    STANDARD_LIGHT_C = 19
    """Standard Light C"""

    D55 = 20
    """D55"""

    D65 = 21
    """D65"""

    D75 = 22
    """D75"""

    D50 = 23
    """D50"""

    ISO_STUDIO_TUNGSTEN = 24
    """ISO Studio Tungsten"""

    OTHER = 255
    """Other Light Source"""


class MeteringMode(IntEnum):
    """Metering mode."""

    UNKNOWN = 0
    """Unknown"""

    AVERAGE = 1
    """Average"""

    CENTER_WEIGHTED_AVERAGE = 2
    """Center Weighted Average"""

    SPOT = 3
    """Spot"""

    MULTI_SPOT = 4
    """Multi Spot"""

    PATTERN = 5
    """Pattern"""

    PARTIAL = 6
    """Partial"""

    OTHER = 255
    """Other"""


class Orientation(IntEnum):
    """Image orientation in terms of rows and columns."""

    TOP_LEFT = 1
    """The 0th row is at the visual top of the image and the 0th column is the visual
    left-hand side."""

    TOP_RIGHT = 2
    """The 0th row is at the visual top of the image and the 0th column is the visual
    right-hand side."""

    BOTTOM_RIGHT = 3
    """The 0th row is at the visual bottom of the image and the 0th column is the visual
    right-hand side."""

    BOTTOM_LEFT = 4
    """The 0th row is at the visual bottom of the image and the 0th column is the visual
    left-hand side."""

    LEFT_TOP = 5
    """The 0th row is the visual left-hand side of the image and the 0th column is the
    visual top."""

    RIGHT_TOP = 6
    """The 0th row is the visual right-hand side of the image and the 0th column is the
    visual bottom."""

    RIGHT_BOTTOM = 7
    """The 0th row is the visual right-hand side of the image and the 0th column is the
    visual bottom."""

    LEFT_BOTTOM = 8
    """The 0th row is the visual left-hand side of the image and the 0th column is the
    visual bottom."""


class ResolutionUnit(IntEnum):
    """Unit for measuring X resolution and Y resolution tags."""

    INCHES = 2
    """Inches or Unknown"""

    CENTIMETERS = 3
    """Centimeters"""


class Saturation(IntEnum):
    """Saturation processing applied by camera."""

    NORMAL = 0
    """Normal Saturation"""

    LOW = 1
    """Low Saturation"""

    HIGH = 2
    """High Saturation"""


class SceneCaptureType(IntEnum):
    """Type of scene that was shot or the mode in which the image was shot."""

    STANDARD = 0
    """Standard"""

    LANDSCAPE = 1
    """Landscape"""

    PORTRAIT = 2
    """Portrait"""

    NIGHT_SCENE = 3
    """Night Scene"""


class SensingMethod(IntEnum):
    """Image sensor type on the camera or input device."""

    NOT_DEFINED = 1
    """Not Defined"""

    ONE_CHIP_COLOR_AREA_SENSOR = 2
    """One-Chip Color Area Sensor"""

    TWO_CHIP_COLOR_AREA_SENSOR = 3
    """Two-Chip Color Area Sensor"""

    THREE_CHIP_COLOR_AREA_SENSOR = 4
    """Three-Chip Color Area Sensor"""

    COLOR_SEQUENTIAL_AREA_SENSOR = 5
    """Color Sequential Area Sensor"""

    TRILINEAR_SENSOR = 7
    """Trilinear Sensor"""

    COLOR_SEQUENTIAL_LINEAR_SENSOR = 8
    """Color Sequential Linear Sensor"""


class Sharpness(IntEnum):
    """Sharpness processing applied by camera."""

    NORMAL = 0
    """Normal"""

    SOFT = 1
    """Soft"""

    HARD = 2
    """Hard"""


class WhiteBalance(IntEnum):
    """White balance mode set when the image was shot."""

    AUTO = 0
    """Auto White Balance"""

    MANUAL = 1
    """Manual White Balance"""


ATTRIBUTE_ID_MAP = {
    # TIFF Rev. 6.0 Section A: Image Data Structure Tags
    "image_width": 256,
    "image_height": 257,
    "bits_per_sample": 258,
    "compression": 259,
    "photometric_interpretation": 262,
    "orientation": 274,
    "samples_per_pixel": 277,
    "planar_configuration": 284,
    "subsampling_ratio_of_y_to_c": 530,
    "y_and_c_positioning": 531,
    "x_resolution": 282,
    "y_resolution": 283,
    "resolution_unit": 296,
    # TIFF Rev. 6.0 Section B: Recording Offset Tags
    "strip_offsets": 273,
    "rows_per_strip": 278,
    "strip_byte_counts": 279,
    "jpeg_interchange_format": 513,
    "jpeg_interchange_format_length": 514,
    # TIFF Rev. 6.0 Section C: Image Data Characteristic Tags
    "transfer_function": 301,
    "white_point": 318,
    "primary_chromaticities": 319,
    "matrix_coefficients": 529,
    "reference_black_white": 532,
    # TIFF Rev. 6.0 Section D: Other Tags
    "datetime": 306,
    "image_description": 270,
    "make": 271,
    "model": 272,
    "software": 305,
    "artist": 315,
    "copyright": 33432,
    "rating": 18246,
    "rating_percent": 18249,
    # EXIF Tags
    "exposure_time": 33434,
    "f_number": 33437,
    "exposure_program": 34850,
    "spectral_sensitivity": 34852,
    "photographic_sensitivity": 34855,
    "oecf": 34856,
    "sensitivity_type": 34864,
    "standard_output_sensitivity": 34865,
    "recommended_exposure_index": 34866,
    "iso_speed": 34867,
    "iso_speed_latitude_yyy": 34868,
    "iso_speed_latitude_zzz": 34869,
    "exif_version": 36864,
    "datetime_original": 36867,
    "datetime_digitized": 36868,
    "offset_time": 36880,
    "offset_time_original": 36881,
    "offset_time_digitized": 36882,
    "components_configuration": 37121,
    "compressed_bits_per_pixel": 37122,
    "shutter_speed_value": 37377,
    "aperture_value": 37378,
    "brightness_value": 37379,
    "exposure_bias_value": 37380,
    "max_aperture_value": 37381,
    "subject_distance": 37382,
    "metering_mode": 37383,
    "light_source": 37384,
    "flash": 37385,
    "focal_length": 37386,
    "subject_area": 37396,
    "maker_note": 37500,
    "user_comment": 37510,
    "subsec_time": 37520,
    "subsec_time_original": 37521,
    "subsec_time_digitized": 37522,
    "temperature": 37888,
    "humidity": 37889,
    "pressure": 37890,
    "water_depth": 37891,
    "acceleration": 37892,
    "camera_elevation_angle": 37893,
    "xp_title": 0x9C9B,
    "xp_comment": 0x9C9C,
    "xp_author": 0x9C9D,
    "xp_keywords": 0x9C9E,
    "xp_subject": 0x9C9F,
    "flashpix_version": 40960,
    "color_space": 40961,
    "pixel_x_dimension": 40962,
    "pixel_y_dimension": 40963,
    "related_sound_file": 40964,
    "flash_energy": 41483,
    "spatial_frequency_response": 41484,
    "focal_plane_x_resolution": 41486,
    "focal_plane_y_resolution": 41487,
    "focal_plane_resolution_unit": 41488,
    "subject_location": 41492,
    "exposure_index": 41493,
    "sensing_method": 41495,
    "file_source": 41728,
    "scene_type": 41729,
    "cfa_pattern": 41730,
    "custom_rendered": 41985,
    "exposure_mode": 41986,
    "white_balance": 41987,
    "digital_zoom_ratio": 41988,
    "focal_length_in_35mm_film": 41989,
    "scene_capture_type": 41990,
    "gain_control": 41991,
    "contrast": 41992,
    "saturation": 41993,
    "sharpness": 41994,
    "device_setting_description": 41995,
    "subject_distance_range": 41996,
    "image_unique_id": 42016,
    "camera_owner_name": 42032,
    "body_serial_number": 42033,
    "lens_specification": 42034,
    "lens_make": 42035,
    "lens_model": 42036,
    "lens_serial_number": 42037,
    "gamma": 42240,
    # GPS Info Tags
    "gps_version_id": 0,
    "gps_latitude_ref": 1,
    "gps_latitude": 2,
    "gps_longitude_ref": 3,
    "gps_longitude": 4,
    "gps_altitude_ref": 5,
    "gps_altitude": 6,
    "gps_timestamp": 7,
    "gps_satellites": 8,
    "gps_status": 9,
    "gps_measure_mode": 10,
    "gps_dop": 11,
    "gps_speed_ref": 12,
    "gps_speed": 13,
    "gps_track_ref": 14,
    "gps_track": 15,
    "gps_img_direction_ref": 16,
    "gps_img_direction": 17,
    "gps_map_datum": 18,
    "gps_dest_latitude_ref": 19,
    "gps_dest_latitude": 20,
    "gps_dest_longitude_ref": 21,
    "gps_dest_longitude": 22,
    "gps_dest_bearing_ref": 23,
    "gps_dest_bearing": 24,
    "gps_dest_distance_ref": 25,
    "gps_dest_distance": 26,
    "gps_processing_method": 27,
    "gps_area_information": 28,
    "gps_datestamp": 29,
    "gps_differential": 30,
    "gps_horizontal_positioning_error": 31,
    # EXIF-specific IFDs (for __dir__ Display)
    "_exif_ifd_pointer": 34665,
    "_gps_ifd_pointer": 34853,
    "_interoperability_ifd_Pointer": 40965,
}

ATTRIBUTE_NAME_MAP = {value: key for key, value in ATTRIBUTE_ID_MAP.items()}

ATTRIBUTE_TYPE_MAP = (
    {  # tuple of type ID and IFD number description used when adding new tags
        "aperture_value": (int(ExifTypes.RATIONAL), "exif"),
        "artist": (int(ExifTypes.ASCII), 0),
        "body_serial_number": (int(ExifTypes.ASCII), "exif"),
        "brightness_value": (int(ExifTypes.SRATIONAL), "exif"),
        "color_space": (int(ExifTypes.SHORT), "exif"),
        "contrast": (int(ExifTypes.SHORT), "exif"),
        "copyright": (int(ExifTypes.ASCII), 0),
        "custom_rendered": (int(ExifTypes.SHORT), "exif"),
        "datetime": (int(ExifTypes.ASCII), 0),
        "datetime_digitized": (int(ExifTypes.ASCII), "exif"),
        "datetime_original": (int(ExifTypes.ASCII), "exif"),
        "offset_time": (int(ExifTypes.ASCII), "exif"),
        "offset_time_original": (int(ExifTypes.ASCII), "exif"),
        "offset_time_digitized": (int(ExifTypes.ASCII), "exif"),
        "digital_zoom_ratio": (int(ExifTypes.RATIONAL), "exif"),
        "exposure_bias_value": (int(ExifTypes.SRATIONAL), "exif"),
        "exposure_index": (int(ExifTypes.RATIONAL), "exif"),
        "exposure_mode": (int(ExifTypes.SHORT), "exif"),
        "exposure_program": (int(ExifTypes.SHORT), "exif"),
        "exposure_time": (int(ExifTypes.RATIONAL), "exif"),
        "f_number": (int(ExifTypes.RATIONAL), "exif"),
        "flash": (int(ExifTypes.SHORT), "exif"),
        "flash_energy": (int(ExifTypes.RATIONAL), "exif"),
        "focal_length": (int(ExifTypes.RATIONAL), "exif"),
        "focal_length_in_35mm_film": (int(ExifTypes.SHORT), "exif"),
        "focal_plane_resolution_unit": (int(ExifTypes.SHORT), "exif"),
        "focal_plane_x_resolution": (int(ExifTypes.RATIONAL), "exif"),
        "focal_plane_y_resolution": (int(ExifTypes.RATIONAL), "exif"),
        "gain_control": (int(ExifTypes.RATIONAL), "exif"),
        "gps_altitude": (int(ExifTypes.RATIONAL), "gps"),
        "gps_altitude_ref": (int(ExifTypes.BYTE), "gps"),
        "gps_datestamp": (int(ExifTypes.ASCII), "gps"),
        "gps_dest_bearing": (int(ExifTypes.RATIONAL), "gps"),
        "gps_dest_bearing_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_dest_distance": (int(ExifTypes.RATIONAL), "gps"),
        "gps_dest_distance_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_dest_latitude": (int(ExifTypes.RATIONAL), "gps"),
        "gps_dest_latitude_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_dest_longitude": (int(ExifTypes.RATIONAL), "gps"),
        "gps_dest_longitude_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_differential": (int(ExifTypes.SHORT), "gps"),
        "gps_dop": (int(ExifTypes.RATIONAL), "gps"),
        "gps_img_direction": (int(ExifTypes.RATIONAL), "gps"),
        "gps_img_direction_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_latitude": (int(ExifTypes.RATIONAL), "gps"),
        "gps_latitude_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_longitude": (int(ExifTypes.RATIONAL), "gps"),
        "gps_longitude_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_map_datum": (int(ExifTypes.ASCII), "gps"),
        "gps_measure_mode": (int(ExifTypes.ASCII), "gps"),
        "gps_satellites": (int(ExifTypes.ASCII), "gps"),
        "gps_speed": (int(ExifTypes.RATIONAL), "gps"),
        "gps_speed_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_status": (int(ExifTypes.ASCII), "gps"),
        "gps_timestamp": (int(ExifTypes.RATIONAL), "gps"),
        "gps_track": (int(ExifTypes.RATIONAL), "gps"),
        "gps_track_ref": (int(ExifTypes.ASCII), "gps"),
        "gps_version_id": (int(ExifTypes.BYTE), "gps"),
        "image_description": (int(ExifTypes.ASCII), 0),
        "image_unique_id": (int(ExifTypes.ASCII), "exif"),
        "iso_speed": (int(ExifTypes.SHORT), "exif"),
        "lens_specification": (int(ExifTypes.RATIONAL), "exif"),
        "lens_make": (int(ExifTypes.ASCII), "exif"),
        "lens_model": (int(ExifTypes.ASCII), "exif"),
        "lens_serial_number": (int(ExifTypes.ASCII), "exif"),
        "light_source": (int(ExifTypes.SHORT), "exif"),
        "make": (int(ExifTypes.ASCII), 0),
        "max_aperture_value": (int(ExifTypes.RATIONAL), 0),
        "metering_mode": (int(ExifTypes.SHORT), "exif"),
        "model": (int(ExifTypes.ASCII), 0),
        "rating": (int(ExifTypes.SHORT), "exif"),
        "rating_percent": (int(ExifTypes.SHORT), "exif"),
        "orientation": (int(ExifTypes.SHORT), 0),
        "pixel_x_dimension": (int(ExifTypes.SHORT), "exif"),
        "pixel_y_dimension": (int(ExifTypes.SHORT), "exif"),
        "saturation": (int(ExifTypes.SHORT), "exif"),
        "scene_capture_type": (int(ExifTypes.SHORT), "exif"),
        "sensing_method": (int(ExifTypes.SHORT), "exif"),
        "shutter_speed_value": (int(ExifTypes.SRATIONAL), "exif"),
        "software": (int(ExifTypes.ASCII), 0),
        "sharpness": (int(ExifTypes.SHORT), "exif"),
        "spectral_sensitivity": (int(ExifTypes.ASCII), "exif"),
        "photographic_sensitivity": (int(ExifTypes.SHORT), "exif"),
        "subsec_time": (int(ExifTypes.ASCII), "exif"),
        "subsec_time_original": (int(ExifTypes.ASCII), "exif"),
        "subsec_time_digitized": (int(ExifTypes.ASCII), "exif"),
        "subject_distance": (int(ExifTypes.RATIONAL), "exif"),
        "subject_distance_range": (int(ExifTypes.SHORT), "exif"),
        "subject_location": (int(ExifTypes.SHORT), "exif"),
        "user_comment": (
            7,
            "exif",
        ),  # 7 is UNDEFINED (if packed in enum, it would cause downstream issues)
        "white_balance": (int(ExifTypes.SHORT), "exif"),
        "_exif_ifd_pointer": (int(ExifTypes.LONG), 0),
        "_gps_ifd_pointer": (int(ExifTypes.LONG), 0),
        "_interoperability_ifd_Pointer": (int(ExifTypes.LONG), "exif"),
    }
)


ERROR_IMG_NO_ATTR = "image does not have attribute {0}"
