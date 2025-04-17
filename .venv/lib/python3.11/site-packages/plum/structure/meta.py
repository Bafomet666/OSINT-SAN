# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure type metaclass."""

from typing import Dict, Optional, Tuple

from .._code_injector import CodeInjector
from ..data import DataMeta
from .bitfield_member import BitFieldMember
from .code_maker import CodeMaker
from .member import Member


def get_offsets_and_nbytes(
    members: Dict[str, Member]
) -> Tuple[Optional[Tuple[int, ...]], Optional[int]]:
    """Compute member offsets and structure size."""
    member_sizes = tuple(member.nbytes for member in members.values())

    offset = 0
    offsets = []
    for size in member_sizes:
        offsets.append(offset)

        if size is None:
            # member variably sized, so new structure is as well
            nbytes = None
            member_offsets = None
            break

        offset += size
    else:
        member_offsets = tuple(offsets)
        nbytes = offset

    return member_offsets, nbytes


class StructureMeta(DataMeta):

    """Structure data store metaclass."""

    __byteorder__: str
    __members__: Tuple[Member, ...]

    def __new__(
        mcs,
        name,
        bases,
        namespace,
        byteorder: str = "little",
        fieldorder: str = "most_to_least",
    ):
        # pylint: disable=too-many-locals,too-many-branches

        namespace["__format_name__"] = (
            "Structure" if name == "Structure" else f"{name} (Structure)"
        )

        if byteorder not in {"big", "little"}:
            raise ValueError('byteorder must be either "big" or "little"')

        if fieldorder not in {"least_to_most", "most_to_least"}:
            raise ValueError(
                'fieldorder must be either "least_to_most" or "most_to_least"'
            )

        members_dict: Dict[str, Member] = {}
        for base_class in bases:
            if isinstance(base_class, StructureMeta):
                members_dict.update(
                    {m.name: m.copy(m.fget, m.fset) for m in base_class.__members__}
                )

        new_members: Dict[str, Member] = {
            k: m for k, m in namespace.items() if isinstance(m, Member)
        }

        if new_members:
            # namespace.update(new_members)
            members_dict.update(new_members)

            BitFieldMember.organize(members_dict, byteorder, fieldorder)

            code_injector = CodeInjector(namespace)

            index = 0
            for member_name, member in members_dict.items():
                index = member.add_name_index(member_name, index, code_injector)

            for member in members_dict.values():
                member.check()

            offsets, nbytes = get_offsets_and_nbytes(members_dict)

            members = tuple(members_dict.values())

            namespace["__ignore_flags__"] = tuple(member.ignore for member in members)
            namespace["__members__"] = members
            if "__nbytes__" not in namespace:  # pragma: no cover
                namespace["__nbytes__"] = nbytes
            namespace["__offsets__"] = offsets
            namespace["__byteorder__"] = byteorder
            if nbytes is not None:
                names = tuple(member.name for member in members)
                types = tuple(member.fmt for member in members)
                namespace["__names_types__"] = (names, types)

            code_maker = CodeMaker(name, members, new_members.values())
            lines = list(line.rstrip() for line in code_maker.iter_lines(namespace))

            code_injector.update_script(lines)
            code_injector.execute_lines(lines)
            namespace["__implementation__"] = "\n".join(lines)

        for member in members_dict.values():
            del member.temp_store

        cls = super().__new__(mcs, name, bases, namespace)

        # if boost and cls.__names_types__ != NO_MEMBERS_DEFINED:  # pragma: no cover
        #     for method_name in ['__pack__', '__unpack__']:
        #         if mcs._is_method_overridden(method_name, base_class, namespace):
        #             break
        #     else:
        #         nbytes = cls.__nbytes__
        #         _names, types = cls.__names_types__
        #
        #         # attach binary string containing plum-c accelerator "C" structure
        #         # (so structure memory de-allocated when class deleted)
        #         cls.__plum_boost_internals__ = boost.faststructure.add_c_acceleration(
        #             cls, -1 if nbytes is None else nbytes, len(types), types)
        #
        #         cls.__pack__ = boost.ipack_classmethod(cls.__pack__.__func__)
        #         cls.__unpack__ = boost.unpack_classmethod(cls.__unpack__.__func__)

        return cls

    @property
    def byteorder(cls) -> str:
        """Byte order ("little" or "big")."""
        return cls.__byteorder__
