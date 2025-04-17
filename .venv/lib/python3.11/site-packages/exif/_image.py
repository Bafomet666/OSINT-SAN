"""Image EXIF metadata interface module."""

import logging
import os
import warnings
from typing import Any, BinaryIO, Dict, List, Union

from plum.bigendian import uint16

from exif._constants import ATTRIBUTE_ID_MAP, ExifMarkers
from exif._app1_create import generate_empty_app1_bytes
from exif._app1_metadata import App1MetaData

logger = logging.getLogger(__name__)


class Image:
    """Image EXIF metadata interface class.

    :param img_file: image file with EXIF metadata
    :type image_file: str (file path), bytes (already-read contents), or File

    """

    def _parse_segments(self, img_bytes: bytes) -> None:
        cursor = 0

        # Traverse hexadecimal string until EXIF APP1 segment found.
        while img_bytes[cursor : cursor + len(ExifMarkers.APP1)] != ExifMarkers.APP1:
            cursor += len(ExifMarkers.APP1)
            if cursor > len(img_bytes):
                self._has_exif = False
                cursor = 2  # should theoretically go after SOI marker (if adding)
                break

        self._segments["preceding"] = img_bytes[:cursor]
        app1_start_index = cursor

        if self._has_exif:
            # Determine the expected length of the APP1 segment.
            app1_len = uint16.unpack(
                img_bytes[app1_start_index + 2 : app1_start_index + 4]
            )
            cursor += app1_len + 2  # skip APP1 marker and all data

            # If the expected length stops early, keep traversing until another section is found.
            while img_bytes[cursor : cursor + 1] != ExifMarkers.SEG_PREFIX:
                cursor += 1
                # raise IOError("no subsequent EXIF segment found, is this an EXIF-encoded JPEG?")
                if cursor > len(img_bytes):
                    self._has_exif = False
                    break

        if self._has_exif:
            # Instantiate an APP1 segment object to create an EXIF tag interface.
            self._segments["APP1"] = App1MetaData(img_bytes[app1_start_index:cursor])
            self._segments["succeeding"] = img_bytes[cursor:]
        else:
            # Store the remainder of the image so that it can be reconstructed when exporting.
            self._segments["succeeding"] = img_bytes[app1_start_index:]

    def __init__(
        self,
        img_file: Union[BinaryIO, bytes, str],  # pylint: disable=unsubscriptable-object
    ) -> None:
        self._has_exif = True
        self._segments: Dict[
            str, Union[App1MetaData, bytes]  # pylint: disable=unsubscriptable-object
        ] = {}

        if hasattr(img_file, "read"):
            img_bytes = img_file.read()  # type: ignore
        elif isinstance(img_file, bytes):
            img_bytes = img_file
        elif os.path.isfile(img_file):  # type: ignore
            with open(img_file, "rb") as file_descriptor:  # type: ignore
                img_bytes = file_descriptor.read()
        else:  # pragma: no cover
            raise ValueError("expected file object, file path as str, or bytes")

        self._parse_segments(img_bytes)

    def __dir__(self) -> List[str]:
        members = [
            "delete",
            "delete_all",
            "get",
            "get_all",
            "get_file",
            "get_thumbnail",
            "has_exif",
            "list_all",
            "_segments",
        ]

        if self._has_exif:
            assert isinstance(self._segments["APP1"], App1MetaData)
            members += self._segments["APP1"].get_tag_list()

        return members

    def __getattr__(self, item):
        return getattr(self._segments["APP1"], item)

    def __setattr__(self, key, value):
        try:
            ATTRIBUTE_ID_MAP[key.lower()]
        except KeyError:
            super(Image, self).__setattr__(key, value)
        else:
            if not self._has_exif:
                self._segments["APP1"] = App1MetaData(generate_empty_app1_bytes())
                self._has_exif = True

            setattr(self._segments["APP1"], key.lower(), value)

    def __delattr__(self, item):
        try:
            ATTRIBUTE_ID_MAP[item]
        except KeyError:
            super(Image, self).__delattr__(item)
        else:
            delattr(self._segments["APP1"], item)

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __delitem__(self, key):
        self.__delattr__(key)

    def delete(self, attribute: str) -> None:
        """Remove the specified attribute from the image.

        :param attribute: image EXIF attribute name

        """
        delattr(self, attribute)

    def delete_all(self) -> None:
        """Remove all EXIF tags from the image."""
        for _ in range(
            2
        ):  # iterate twice to delete thumbnail tags the second time around
            assert isinstance(self._segments["APP1"], App1MetaData)
            for tag in self._segments["APP1"].get_tag_list():
                if not tag in ["_exif_ifd_pointer", "_gps_ifd_pointer", "exif_version"]:
                    try:
                        delattr(self, tag)
                    except AttributeError:
                        warnings.warn("could not delete tag " + tag, RuntimeWarning)

            self._parse_segments(self.get_file())

    def get(self, attribute: str, default: Any = None) -> Any:
        """Return the value of the specified tag.

        If the attribute is not available or set, return the value specified by the ``default``
        keyword argument.

        :param attribute: image EXIF attribute name
        :param default: return value if attribute does not exist
        :returns: tag value if present, ``default`` otherwise
        :rtype: corresponding Python type

        """
        try:
            retval = getattr(self, attribute)
        except (AttributeError, NotImplementedError):
            retval = default

        return retval

    def get_all(self) -> Dict[str, Any]:
        """Return dictionary containing all EXIF tag values keyed by tag name."""
        all_tags = {}

        for tag_name in self.list_all():
            try:
                tag_value = getattr(self, tag_name)
            except Exception:  # pylint: disable=broad-except
                logger.warning("unable to read tag %r", tag_name)
            else:
                all_tags[tag_name] = tag_value

        return all_tags

    def get_file(self) -> bytes:
        """Generate equivalent binary file contents.

        :returns: image binary with EXIF metadata

        """
        assert isinstance(self._segments["preceding"], bytes)
        img_bytes = self._segments["preceding"]

        if self._has_exif:
            assert isinstance(self._segments["APP1"], App1MetaData)
            img_bytes += self._segments["APP1"].get_segment_bytes()

        assert isinstance(self._segments["succeeding"], bytes)
        img_bytes += self._segments["succeeding"]

        return img_bytes

    def get_thumbnail(self) -> bytes:
        """Extract thumbnail binary contained in EXIF metadata.

        :returns: thumbnail binary
        :raises RuntimeError: image does not contain thumbnail

        """
        thumbnail_bytes = None

        try:
            app1_segment = self._segments["APP1"]
        except KeyError:
            pass
        else:
            assert isinstance(app1_segment, App1MetaData)
            thumbnail_bytes = app1_segment.thumbnail_bytes

        if not thumbnail_bytes:
            raise RuntimeError("image does not contain thumbnail")

        return thumbnail_bytes

    @property
    def has_exif(self) -> bool:
        """Report whether or not the image currently has EXIF metadata."""
        return self._has_exif

    def list_all(self) -> List[str]:
        """List all EXIF tags contained in the image."""
        tags_list = []

        if self._has_exif:
            assert isinstance(self._segments["APP1"], App1MetaData)
            tags_list += self._segments["APP1"].get_tag_list(include_unknown=False)

        return tags_list

    def set(self, attribute: str, value) -> None:
        """Set the value of the specified attribute.

        :param attribute: image EXIF attribute name
        :param value: tag value
        :type value: corresponding Python type

        """
        setattr(self, attribute, value)
