"""IFD tag structure parser classes."""

from exif.ifd_tag._ascii import Ascii
from exif.ifd_tag._base import Base as BaseIfdTag
from exif.ifd_tag._byte import Byte
from exif.ifd_tag._exifversion import ExifVersion
from exif.ifd_tag._long import Long
from exif.ifd_tag._rational import Rational
from exif.ifd_tag._short import Short
from exif.ifd_tag._slong import Slong
from exif.ifd_tag._sshort import Sshort
from exif.ifd_tag._srational import Srational
from exif.ifd_tag._user_comment import UserComment
from exif.ifd_tag._windows_xp import WindowsXp
