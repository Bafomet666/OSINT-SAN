# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure of uniquely named and typed members data store and transform."""

from typing import Any, Dict, Optional, Tuple, Union

from ..data import Data
from .bitfield_member import bitfield_member
from .dimmed_member import dimmed_member
from .member import member, Member
from .meta import StructureMeta
from .sized_member import sized_member
from .structureview import StructureView

bitfield_member.__module__ = "plum.structure"
dimmed_member.__module__ = "plum.structure"
member.__module__ = "plum.structure"
StructureMeta.__module__ = "plum.structure"
sized_member.__module__ = "plum.structure"


class Structure(list, Data, metaclass=StructureMeta):

    """Structured data store type."""

    # filled in by metaclass
    __ignore_flags__: Tuple[bool, ...] = ()
    __members__: Tuple[Member, ...] = ()
    __nbytes__: Union[None, int] = 0
    __offsets__: Union[None, Tuple[int, ...]] = ()
    __byteorder__: str = "little"
    __implementation__: Optional[str] = None
    __format_name__: str
    __hint__: str

    # Metaclass generates the following methods for each subclass:
    #   __init__
    #   member getter/setters
    #   __eq__
    #   __ne__
    #   __pack__
    #   __pack_and_dump__
    #   __repr__
    #   __unpack__
    #   __unpack_and_dump__

    def asdict(self) -> Dict[str, Any]:
        """Return structure members in dictionary form.

        :returns: structure members

        """
        return {
            name: getattr(self, name)
            for name in (member.name for member in self.__members__)
        }

    @classmethod
    def _make_structure_from_dict(cls, members: Dict[str, Any]) -> "Structure":
        return cls(**members)

    def __setattr__(self, name, value):
        # get the attribute to raise an exception if invalid name
        getattr(self, name)
        object.__setattr__(self, name, value)

    @classmethod
    def __view__(cls, buffer, offset: int = 0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param offset: byte offset

        """
        if not cls.__nbytes__:
            raise TypeError(
                f"cannot create view for structure {cls.__name__!r} "
                "with variable size"
            )

        return StructureView(cls, buffer, offset)


__all__ = [
    "bitfield_member",
    "dimmed_member",
    "member",
    "StructureMeta",
    "sized_member",
    "Structure",
]
