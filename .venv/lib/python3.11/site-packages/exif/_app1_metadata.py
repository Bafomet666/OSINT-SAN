"""APP1 metadata interface module for EXIF tags."""

import warnings
from typing import List

from plum.buffer import Buffer
from plum.bigendian import uint16
from plum.exceptions import UnpackError

from exif._utils import pack_into, value_fits_in_ifd_tag
from exif._constants import (
    ATTRIBUTE_ID_MAP,
    ATTRIBUTE_NAME_MAP,
    ATTRIBUTE_TYPE_MAP,
    ERROR_IMG_NO_ATTR,
    ExifMarkers,
)
from exif._datatypes import (
    ExifType,
    Ifd,
    IfdLe,
    IfdTag,
    IfdTagLe,
    TiffByteOrder,
    TiffHeader,
)
from exif.ifd_tag import (
    Ascii,
    BaseIfdTag,
    Byte,
    ExifVersion,
    Long,
    Rational,
    Short,
    Slong,
    Srational,
    Sshort,
    UserComment,
    WindowsXp,
)
from exif.ifd_tag._rational import RationalDtype
from exif.ifd_tag._srational import SrationalDtype
from exif.ifd_tag._user_comment import USER_COMMENT_CHARACTER_CODE_LEN_BYTES

# FUTURE: There's quite a few spots where a new Plum Buffer is created for the APP1 body bytes. Consider cleaning this
# up to share the same buffer reference. Also, fix the false positive no-member Pylint errors.
# pylint: disable=no-member


class App1MetaData:
    """APP1 metadata interface class for EXIF tags."""

    def _add_empty_ifd(self, ifd):
        if not ifd == "gps":
            raise RuntimeError(f"only can add GPS IFD to image, not {ifd}")

        if 1 not in self.ifd_pointers:
            raise RuntimeError("can't yet add to images without a subsequent IFD 1")

        if self.endianness == TiffByteOrder.BIG:
            ifd_cls = Ifd
        else:
            ifd_cls = IfdLe

        new_app1_bytes = self.body_bytes[: self.ifd_pointers[1]]
        bytes_after_new_ifd = self.body_bytes[self.ifd_pointers[1] :]

        # Inert empty IFD.
        empty_ifd = Ifd(tags=[], next=0)
        new_app1_bytes += empty_ifd.ipack()

        # Touch up pointer to IFD 1 (which we already know exists).
        new_app1_bytes_buffer = Buffer(new_app1_bytes)
        new_app1_bytes_buffer.offset = self.ifd_pointers[0]

        ifd_zero = new_app1_bytes_buffer.unpack(ifd_cls)
        ifd_zero.next += empty_ifd.nbytes
        new_app1_bytes[
            self.ifd_pointers[0] : self.ifd_pointers[0] + ifd_zero.nbytes
        ] = ifd_zero.ipack()

        # Touch up IFD 1 pointers!
        after_new_ifd_buffer = Buffer(bytes_after_new_ifd)
        after_new_ifd_buffer.offset = 0
        ifd1 = after_new_ifd_buffer.unpack(ifd_cls)

        for tag_index in range(ifd1.count):
            tag_t = ifd1.tags[tag_index]
            is_value_in_ifd_tag_itself = value_fits_in_ifd_tag(tag_t)
            if (
                tag_t.tag_id in [ATTRIBUTE_ID_MAP["jpeg_interchange_format"]]
                or not is_value_in_ifd_tag_itself
            ):
                tag_t.value_offset += empty_ifd.nbytes
            ifd1.tags[tag_index] = tag_t

        pack_into(datatype=ifd1, buffer=bytes_after_new_ifd, offset=0)

        # Parse new bytes containing the additional placeholder IFD.
        self.body_bytes = new_app1_bytes + bytes_after_new_ifd
        self._parse_ifd_segments()

        # Adjust the size of the APP1 header to reflect the new length.
        app1_len = uint16.view(
            self.header_bytes, offset=2
        )  # 2 bytes into the header, i.e., right after the marker
        app1_len += empty_ifd.nbytes

        # Add pointer tag to IFD 0.
        # new IFD bytes were appended directly in front of IFD 1, need to point to beginning of new block
        offset_of_new_ifd = self.ifd_pointers[1] - empty_ifd.nbytes
        self._add_tag("_gps_ifd_pointer", offset_of_new_ifd)

    def _add_tag(
        self, tag, value
    ):  # pylint: disable=too-many-locals, too-many-branches, too-many-statements
        # FUTURE: This method could likely use some future cleanup and abstraction.
        try:
            tag_type, ifd_number = ATTRIBUTE_TYPE_MAP[tag]
        except KeyError:
            raise AttributeError(f"cannot add attribute {tag} to image")

        if self.endianness == TiffByteOrder.BIG:
            ifd_cls = Ifd
            ifd_tag_cls = IfdTag
        else:
            ifd_cls = IfdLe
            ifd_tag_cls = IfdTagLe

        if ifd_number not in self.ifd_pointers:
            self._add_empty_ifd(ifd_number)

        # Make a list of all IFDs that will need to be re-packed with touched up pointers.
        subsequent_ifd_names = [
            ifd
            for ifd, offset in self.ifd_pointers.items()
            if offset > self.ifd_pointers[ifd_number]
        ]
        subsequent_ifd_offsets = sorted(
            [
                offset
                for offset in self.ifd_pointers.values()
                if offset > self.ifd_pointers[ifd_number]
            ]
        )

        # Determine the number of bytes that will be injected.
        added_bytes = ifd_tag_cls.nbytes
        pointer_value_bytes = 0
        value_count = 1

        if tag_type == ExifType.ASCII and len(value) >= 4:
            pointer_value_bytes = len(value) + 1  # add one for null termination

        if tag_type == ExifType.ASCII:
            value_count = len(value) + 1

        if tag_type == ExifType.RATIONAL:
            if isinstance(value, tuple):
                value_count = len(value)
            else:
                value_count = 1

            pointer_value_bytes = value_count * RationalDtype.nbytes

        if tag_type == ExifType.SRATIONAL:
            # Value count stays at 1 since EXIF specification does not define multi-valued SRATIONAL tags.
            pointer_value_bytes = value_count * SrationalDtype.nbytes

        if (
            tag == "user_comment"
        ):  # character code header followed by null-terminated ASCII string
            value_count = USER_COMMENT_CHARACTER_CODE_LEN_BYTES + len(value) + 1

            if len(value) >= 4:
                pointer_value_bytes = (
                    USER_COMMENT_CHARACTER_CODE_LEN_BYTES + len(value) + 1
                )

        added_bytes += pointer_value_bytes

        # Keep all bytes prior to the IFD where the new tag will be added.
        new_app1_bytes = self.body_bytes[: self.ifd_pointers[ifd_number]]

        # If IFD 1 occurs after that added tag, adjust the pointer to it from IFD 0.
        if ifd_number != 0:
            new_app1_buffer = Buffer(new_app1_bytes)
            new_app1_buffer.offset = self.ifd_pointers[0]
            ifd_zero = new_app1_buffer.unpack(ifd_cls)

            if ifd_zero.next and 1 in subsequent_ifd_names:
                ifd_zero.next += added_bytes

            # Also adjust the pointers to the GPS and EXIF IFDs if they occur after the added tag.
            for tag_index in range(ifd_zero.count):
                tag_t = ifd_zero.tags[tag_index]

                is_ifd_pointer_to_adjust = (
                    tag_t.tag_id == ATTRIBUTE_ID_MAP["_gps_ifd_pointer"]
                    and "gps" in subsequent_ifd_names
                )
                is_ifd_pointer_to_adjust |= (
                    tag_t.tag_id == ATTRIBUTE_ID_MAP["_exif_ifd_pointer"]
                    and "exif" in subsequent_ifd_names
                )

                if is_ifd_pointer_to_adjust:
                    tag_t.value_offset += added_bytes

                ifd_zero.tags[tag_index] = tag_t

            pack_into(
                datatype=ifd_zero, buffer=new_app1_bytes, offset=self.ifd_pointers[0]
            )

        # Adjust InteropOffset in EXIF IFD if needed
        if "interopt" in subsequent_ifd_names and "exif" not in subsequent_ifd_names:
            new_app1_buffer = Buffer(new_app1_bytes)
            new_app1_buffer.offset = self.ifd_pointers["exif"]
            ifd_exif = new_app1_buffer.unpack(ifd_cls)

            for tag_index in range(ifd_exif.count):
                tag_t = ifd_exif.tags[tag_index]
                is_ifd_pointer_to_adjust = (
                    tag_t.tag_id == ATTRIBUTE_ID_MAP["_interoperability_ifd_Pointer"]
                    and "interopt" in subsequent_ifd_names
                )

                if is_ifd_pointer_to_adjust:
                    tag_t.value_offset += added_bytes

                ifd_exif.tags[tag_index] = tag_t

            pack_into(
                datatype=ifd_exif,
                buffer=new_app1_bytes,
                offset=self.ifd_pointers["exif"],
            )

        # Unpack the original bytes of the IFD to which the new tag will be added to.
        target_ifd_offset = self.ifd_pointers[ifd_number]
        body_bytes_buffer = Buffer(self.body_bytes)
        body_bytes_buffer.offset = target_ifd_offset
        target_ifd = body_bytes_buffer.unpack(ifd_cls)

        # Find the end of the data block
        # in well structured EXIF blocks this should be identical to
        # len(self.body_bytes) or subsequent_ifd_offsets[0]
        target_ifd_end = (
            subsequent_ifd_offsets[0]
            if subsequent_ifd_offsets
            else len(self.body_bytes)
        )
        # size of this itd without data
        target_ifd_tail_start = target_ifd_offset + 2 + target_ifd.count * 12 + 4
        # now iterate throw values and check for appended data
        for tag_index in range(target_ifd.count):
            tag_t = target_ifd.tags[tag_index]
            is_value_in_ifd_tag_itself = value_fits_in_ifd_tag(tag_t)
            if (
                tag_t.tag_id in [ATTRIBUTE_ID_MAP["jpeg_interchange_format"]]
                or not is_value_in_ifd_tag_itself
            ):
                itemsize = 1
                if tag_t.type == ExifType.RATIONAL:
                    itemsize = RationalDtype.nbytes
                if tag_t.type == ExifType.SRATIONAL:
                    itemsize = SrationalDtype.nbytes
                tag_data_end = tag_t.value_offset + tag_t.value_count * itemsize
                target_ifd_tail_start = max(target_ifd_tail_start, tag_data_end)

        # store ifd data before and after insert position
        orig_ifd_values = self.body_bytes[
            target_ifd_offset + target_ifd.nbytes : target_ifd_tail_start
        ]
        orig_ifd_values_tail = self.body_bytes[target_ifd_tail_start:target_ifd_end]

        # Determine if a pointer to a value is necessary, and if so, find it.
        if (
            (tag_type == ExifType.ASCII and len(value) >= 4)
            or tag_type in [ExifType.RATIONAL, ExifType.SRATIONAL]
            or (tag == "user_comment" and len(value) >= 4)
        ):
            value_pointer = target_ifd_tail_start + ifd_tag_cls.nbytes
        elif tag == "_gps_ifd_pointer":
            # Must set pointer values now or else they'll incorrectly point to 0x00 when parsing.
            # Also add number of inserted bytes by which the target location is now shifted back
            value += added_bytes
            value_pointer = value
        else:
            value_pointer = 0

        # Iterate over the IFD's tags and increase any value offset pointers by the size of an IFD tag.
        for tag_index in range(target_ifd.count):
            tag_t = target_ifd.tags[tag_index]

            is_ifd_pointer_to_adjust = (
                tag_t.tag_id == ATTRIBUTE_ID_MAP["_gps_ifd_pointer"]
                and "gps" in subsequent_ifd_names
            )
            is_ifd_pointer_to_adjust |= (
                tag_t.tag_id == ATTRIBUTE_ID_MAP["_exif_ifd_pointer"]
                and "exif" in subsequent_ifd_names
            )

            is_value_in_ifd_tag_itself = value_fits_in_ifd_tag(tag_t)
            if is_ifd_pointer_to_adjust:
                tag_t.value_offset += added_bytes
            elif not is_value_in_ifd_tag_itself:
                tag_t.value_offset += ifd_tag_cls.nbytes

            target_ifd.tags[tag_index] = tag_t

        # Add the new tag to the IFD.
        target_ifd.count += 1
        target_ifd.tags.append(
            ifd_tag_cls(
                tag_id=ATTRIBUTE_ID_MAP[tag],
                type=tag_type,
                value_count=value_count,
                value_offset=value_pointer,
            )
        )

        # If necessary, touch up the pointer to the next IFD.
        if target_ifd.next:
            target_ifd.next += added_bytes

        # Pack new IFD bytes into the new body bytes (along with the pre-existing values that follow).
        new_app1_bytes[target_ifd_offset : target_ifd_offset + target_ifd.nbytes] = (
            target_ifd.ipack()
        )
        new_app1_bytes += orig_ifd_values
        new_app1_bytes += b"\x00" * pointer_value_bytes
        new_app1_bytes += orig_ifd_values_tail

        # Touch up pointers in any subsequent IFDs.
        # FUTURE: This could likely be better abstracted!
        while subsequent_ifd_offsets:
            current_ifd_offset = subsequent_ifd_offsets.pop(0)

            body_bytes_buffer = Buffer(self.body_bytes)
            body_bytes_buffer.offset = current_ifd_offset
            target_ifd = body_bytes_buffer.unpack(ifd_cls)

            if subsequent_ifd_offsets:
                orig_ifd_values = self.body_bytes[
                    current_ifd_offset + target_ifd.nbytes : subsequent_ifd_offsets[0]
                ]
            else:
                orig_ifd_values = self.body_bytes[
                    current_ifd_offset + target_ifd.nbytes :
                ]

            for tag_index in range(target_ifd.count):
                tag_t = target_ifd.tags[tag_index]
                is_value_in_ifd_tag_itself = value_fits_in_ifd_tag(tag_t)
                if (
                    tag_t.tag_id in [ATTRIBUTE_ID_MAP["jpeg_interchange_format"]]
                    or not is_value_in_ifd_tag_itself
                ):
                    tag_t.value_offset += added_bytes
                elif tag_t.tag_id in [
                    ATTRIBUTE_ID_MAP["_interoperability_ifd_Pointer"]
                ]:
                    tag_t.value_offset += added_bytes

                target_ifd.tags[tag_index] = tag_t

            if target_ifd.next:
                target_ifd.next += added_bytes

            new_app1_bytes += target_ifd.ipack()
            new_app1_bytes += orig_ifd_values

        # Finally, adjust the size of the APP1 header to reflect the new length.
        app1_len = uint16.view(
            self.header_bytes, offset=2
        )  # 2 bytes into the header, i.e., right after the marker
        app1_len += added_bytes

        # Reload to pick up on new bytes arrangement and then modify the currently-zero value.
        self.body_bytes = new_app1_bytes
        self._parse_ifd_segments()
        self.ifd_tags[ATTRIBUTE_ID_MAP[tag]].modify(value)

        # If the tag is a user comment, update its character code header to reflect ASCII encoding.
        if tag == "user_comment":
            self.ifd_tags[ATTRIBUTE_ID_MAP[tag]].set_character_code_to_ascii()

    def _delete_ifd_tag(self, attribute_id):
        # Overwrite pointer data with null bytes (if applicable, depending on datatype).
        self.ifd_tags[attribute_id].wipe()

        # Unpack the original IFD section.
        corresponding_ifd_offset = self.ifd_pointers[self.tag_parent_ifd[attribute_id]]
        if self.endianness == TiffByteOrder.BIG:
            ifd_cls = Ifd
        else:
            ifd_cls = IfdLe

        body_bytes_buffer = Buffer(self.body_bytes)
        body_bytes_buffer.offset = corresponding_ifd_offset
        orig_ifd = body_bytes_buffer.unpack(ifd_cls)

        # Construct a new IFD section datatype containing all tags but the deletion target.
        preserved_tags = [tag for tag in orig_ifd.tags if tag.tag_id != attribute_id]
        new_ifd = ifd_cls(tags=preserved_tags, next=orig_ifd.next)

        # Pack in new IFD bytes with null bytes (i.e., an empty IFD tag) appended to preserve pointers.
        # Note: The pack_into method overrides the pre-existing bytes.
        pack_into(
            datatype=new_ifd, buffer=self.body_bytes, offset=corresponding_ifd_offset
        )
        pack_into(
            datatype=IfdTag(tag_id=0, type=0, value_count=0, value_offset=0),
            buffer=self.body_bytes,
            offset=corresponding_ifd_offset + new_ifd.nbytes,
        )

        # Remove tag from parser tag dictionary.
        del self.ifd_tags[attribute_id]
        del self.tag_parent_ifd[attribute_id]

        # Regenerate information about existing tags.
        self._parse_ifd_segments()

    def _extract_thumbnail(self):
        if 1 in self.ifd_pointers:  # IFD segment 1 contains thumbnail (if present)
            hex_after_ifd1 = self.body_bytes[self.ifd_pointers[1] :]
            try:
                start_index = hex_after_ifd1.index(ExifMarkers.SOI)
                end_index = hex_after_ifd1.index(ExifMarkers.EOI) + len(ExifMarkers.EOI)
            except ValueError:  # pragma: no cover
                pass  # no thumbnail
            else:
                self.thumbnail_bytes = hex_after_ifd1[start_index:end_index]

    def get_segment_bytes(self) -> bytes:
        """Get equivalent APP1 segment bytes."""
        return bytes(self.header_bytes) + bytes(self.body_bytes)

    def get_tag_list(self, include_unknown: bool = True) -> List[str]:
        """Get a list of EXIF tag attributes present in the image object."""
        if include_unknown:
            tag_list = [
                ATTRIBUTE_NAME_MAP.get(key, f"<unknown EXIF tag {key}>")
                for key in self.ifd_tags
            ]

        else:
            tag_list = []

            for key in self.ifd_tags:
                try:
                    tag_list.append(ATTRIBUTE_NAME_MAP[key])
                except KeyError:
                    pass

        return tag_list

    def _iter_ifd_tags(self, ifd_key):
        ifd_offset = self.ifd_pointers[ifd_key]

        if self.endianness == TiffByteOrder.BIG:
            ifd_cls = Ifd
        else:
            ifd_cls = IfdLe

        try:
            body_bytes_buffer = Buffer(self.body_bytes)
            body_bytes_buffer.offset = ifd_offset
            ifd_t = body_bytes_buffer.unpack(ifd_cls)
        except UnpackError:
            warnings.warn(f"skipping bad IFD {ifd_key}", RuntimeWarning)
            next_ifd_offset = 0
        else:
            for tag_index in range(ifd_t.count):
                tag_offset = (
                    ifd_offset + 2 + tag_index * IfdTag.nbytes
                )  # count is 2 bytes
                tag_t = ifd_t.tags[tag_index]
                tag_py_ins = self._tag_factory(tag_t, tag_offset)

                if (
                    ifd_key != 1 or tag_t.tag_id not in self.ifd_tags
                ):  # don't let thumbnail tags override base image tags
                    self.ifd_tags[tag_t.tag_id] = tag_py_ins
                    self.tag_parent_ifd[tag_t.tag_id] = ifd_key

                if tag_t.tag_id == ATTRIBUTE_ID_MAP["_exif_ifd_pointer"]:
                    self.ifd_pointers["exif"] = tag_t.value_offset

                if tag_t.tag_id == ATTRIBUTE_ID_MAP["_gps_ifd_pointer"]:
                    self.ifd_pointers["gps"] = tag_t.value_offset

                if tag_t.tag_id == ATTRIBUTE_ID_MAP["_interoperability_ifd_Pointer"]:
                    self.ifd_pointers["interopt"] = tag_t.value_offset

            next_ifd_offset = ifd_t.next

        return next_ifd_offset

    def _parse_ifd_segments(self):
        body_bytes_buffer = Buffer(self.body_bytes)
        tiff_header = body_bytes_buffer.unpack(TiffHeader)
        self.endianness = tiff_header.byte_order

        current_ifd = 0
        current_ifd_offset = tiff_header.ifd_offset

        while current_ifd_offset:
            self.ifd_pointers[current_ifd] = current_ifd_offset
            current_ifd_offset = self._iter_ifd_tags(current_ifd)
            current_ifd += 1

        if "exif" in self.ifd_pointers:
            self._iter_ifd_tags("exif")

        if "gps" in self.ifd_pointers:
            self._iter_ifd_tags("gps")

    def _tag_factory(self, tag_t, offset):  # pylint: disable=too-many-branches
        if (
            ATTRIBUTE_ID_MAP["xp_title"]
            <= tag_t.tag_id
            <= ATTRIBUTE_ID_MAP["xp_subject"]
        ):  # legacy Windows XP tags
            cls = WindowsXp
        elif (
            ATTRIBUTE_ID_MAP["exif_version"] == tag_t.tag_id
        ):  # custom ASCII encoding without termination character
            cls = ExifVersion
        elif ATTRIBUTE_ID_MAP["user_comment"] == tag_t.tag_id:
            cls = UserComment
        elif tag_t.type == ExifType.BYTE:
            cls = Byte
        elif tag_t.type == ExifType.ASCII:
            cls = Ascii
        elif tag_t.type == ExifType.SHORT:
            cls = Short
        elif tag_t.type == ExifType.LONG:
            cls = Long
        elif tag_t.type == ExifType.RATIONAL:
            cls = Rational
        elif tag_t.type == ExifType.SLONG:
            cls = Slong
        elif tag_t.type == ExifType.SRATIONAL:
            cls = Srational
        elif tag_t.type == ExifType.SSHORT:
            cls = Sshort
        else:
            cls = BaseIfdTag

        return cls(offset, self)

    def __init__(self, segment_bytes):
        self.header_bytes = bytearray(segment_bytes[:0xA])
        self.body_bytes = bytearray(segment_bytes[0xA:])

        self.endianness = None
        self.ifd_pointers = {}
        self.ifd_tags = {}
        self.tag_parent_ifd = {}
        self.thumbnail_bytes = None

        self._parse_ifd_segments()
        self._extract_thumbnail()

    def __delattr__(self, item):
        try:
            # Determine if attribute is an IFD tag accessor.
            attribute_id = ATTRIBUTE_ID_MAP[item]
        except KeyError:  # pragma: no cover
            # Coverage and behavior tested by Image class.
            # Attribute is a class member. Delete natively.
            super(App1MetaData, self).__delattr__(item)
        else:
            # Attribute is not a class member. Delete EXIF tag value.
            try:
                self.ifd_tags[attribute_id]
            except KeyError:
                raise AttributeError(ERROR_IMG_NO_ATTR.format(item))

            self._delete_ifd_tag(attribute_id)

    def __getattr__(self, item):
        """If attribute is not a class member, get the value of the EXIF tag of the same name."""
        try:
            attribute_id = ATTRIBUTE_ID_MAP[item.lower()]
        except KeyError:
            raise AttributeError(f"unknown image attribute {item}")

        try:
            ifd_tag = self.ifd_tags[attribute_id]
        except KeyError:
            raise AttributeError(ERROR_IMG_NO_ATTR.format(item))

        return ifd_tag.read()

    def __setattr__(self, key, value):
        try:
            # Determine if attribute is an IFD tag accessor.
            attribute_id = ATTRIBUTE_ID_MAP[key]
        except KeyError:
            # Attribute is a class member. Set natively.
            super(App1MetaData, self).__setattr__(key, value)
        else:
            try:
                ifd_tag = self.ifd_tags[attribute_id]
            except KeyError:
                # Tag is not in image already.
                self._add_tag(key, value)
            else:
                try:
                    ifd_tag.modify(value)
                except (
                    ValueError
                ) as exc:  # e.g., if doesn't fit into tag, try deleting and re-adding
                    try:
                        attr_exif_type = ATTRIBUTE_TYPE_MAP[key][0]
                    except KeyError:
                        raise exc

                    if attr_exif_type == ExifType.ASCII:
                        self._delete_ifd_tag(attribute_id)
                        self._add_tag(key, value)
                    else:
                        raise exc
