# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure methods generator."""

from typing import Any, Dict, Generator, List, Tuple, ValuesView

from .member import Member


class CodeMaker:

    """Structure method code generator."""

    members: tuple
    names_tuple: str

    def __init__(
        self,
        structure_name: str,
        members: Tuple[Member, ...],
        new_members: ValuesView[Member],
    ) -> None:
        names = [member.temp_store.local_name for member in members]

        names_tuple = ", ".join(name for name in names if name)

        if "," not in names_tuple:
            names_tuple += ", "

        self.structure_name = structure_name
        self.members = members
        self.names_tuple = names_tuple
        self.new_members = new_members

    def iter_init_lines(self) -> Generator[str, None, None]:
        """Generate __init__ method lines."""
        indent = "    "

        member_stores = [member.temp_store for member in self.members]
        parameters = [store.init_parameter for store in member_stores]
        args = ", ".join(parameters)

        yield f"def __init__(self, *, {args}) -> None:"

        def lines_from_store(store_name: str):
            nonlocal member_stores, indent
            for member_store in member_stores:
                lines = getattr(member_store, store_name)
                if lines:
                    for line in lines:
                        yield (indent + line).rstrip()
                    yield ""

        yield from lines_from_store("init_pre_begin")

        yield from lines_from_store("init_begin")

        yield indent + f'self[:] = ({self.names_tuple[2:].replace(", m_", ", ")})'
        yield ""

        yield from lines_from_store("init_end")

    def iter_pack_lines(self) -> Generator[str, None, None]:
        """Structure __pack__ method generator."""
        indent = "    "

        yield "@classmethod"
        yield "def __pack__(cls, value, pieces: List[bytes], dump: Optional[Record] = None) -> None:"

        yield indent + "if isinstance(value, dict):"
        yield indent + "    value = cls._make_structure_from_dict(value)"
        yield ""

        yield indent + f"({self.names_tuple}) = value"
        yield ""

        yield indent + "if dump is None:"

        for member in self.members:
            lines = getattr(member.temp_store, "pack")
            for line in lines:
                yield indent + indent + line
            yield ""

        yield indent + "else:"

        for member in self.members:
            lines = getattr(member.temp_store, "pack_and_dump")
            for line in lines:
                yield indent + indent + line
            yield ""

    def iter_unpack_lines(self) -> Generator[str, None, None]:
        """Structure __unpack__ method generator."""
        indent = "    "

        factory_present = any(
            m.fmt_is_a_factory and m.fmt_arg is None for m in self.members
        )

        yield "@classmethod"
        yield f'def __unpack__(cls, buffer: bytes, offset: int, dump: Optional[Record] = None) -> Tuple["{self.structure_name}", int]:'
        yield indent + "structure = list.__new__(cls)"
        if factory_present:
            yield indent + "add_member = structure.append"
        yield ""

        yield indent + "if dump is None:"

        for member in self.members:
            for line in member.temp_store.unpack:
                yield indent + indent + line
            if factory_present:
                yield indent + indent + f"add_member(m_{member.name})"
            for line in member.temp_store.unpack_checks:
                yield indent + indent + line
            yield ""

        yield indent + "else:"

        for member in self.members:
            for line in member.temp_store.unpack_and_dump:
                yield indent + indent + line
            if factory_present:
                yield indent + indent + f"add_member(m_{member.name})"
            for line in member.temp_store.unpack_checks:
                yield indent + indent + line
            yield ""

        if not factory_present:
            yield indent + f"structure[:] = ({self.names_tuple})"
            yield ""

        yield indent + "return structure, offset"
        yield ""

    def iter_compare_unfold(
        self, source: str, compute_members: List[str]
    ) -> Generator[str, None, None]:
        """Generate lines to get local variable for each member."""
        indent = " " * 8
        prefix = f"_{source[0]}_"
        left_side = ", ".join(prefix + m.name for m in self.members)
        compute_members = [prefix + name for name in compute_members]

        yield indent + f"{left_side} = {source}"

        if len(compute_members) == 1:
            yield indent + f"if {compute_members[0]} is None:"
            yield indent + f"    {left_side} = self.unpack({source}.ipack())"
        elif compute_members:
            yield indent + f"if None in ({', '.join(compute_members)}):"
            yield indent + f"    {left_side} = self.unpack({source}.ipack())"

    def iter_compare(self, name: str) -> Generator[str, None, None]:
        """Structure __eq__ and __ne__ method generator."""
        compute_members = [m.name for m in self.members if m.compute and not m.ignore]
        names = [m.name for m in self.members if not m.ignore]

        yield f"def __{name}__(self, other: Any) -> bool:"
        yield "    if isinstance(other, dict):"
        yield "        other = self._make_structure_from_dict(other)"

        if (
            not names
            or any(member.ignore for member in self.members)
            or compute_members
        ):
            yield "    elif isinstance(other, type(self)):"
            if names:
                left = ", ".join("_s_" + n for n in names)
                right = ", ".join("_o_" + n for n in names)
                if len(names) > 1:
                    left = f"({left})"
                    right = f"({right})"
                operator = "==" if name == "eq" else "!="
                yield from self.iter_compare_unfold("self", compute_members)
                yield from self.iter_compare_unfold("other", compute_members)
                yield f"        return {left} {operator} {right}"
            else:
                yield f"        return {name == 'eq'}"

            yield "    else:"
            yield f"        return list.__{name}__(self, other)"
        else:
            yield f"    return list.__{name}__(self, other)"

        yield ""

    def iter_repr(self) -> Generator[str, None, None]:
        """Structure __repr__ method generator."""
        member_names = ["_" + m.name for m in self.members]
        if len(member_names) == 1:
            member_names.append("")

        arg_reprs = ", ".join(m.argrepr for m in self.members if m.argrepr)
        class_name = "{type(self).__name__}"

        yield "def __repr__(self) -> str:"
        yield "    try:"
        yield f'        return f"{class_name}({arg_reprs})"'
        yield "    except Exception:"
        yield f'        return f"{class_name}()"'
        yield ""

    def iter_lines(self, namespace: Dict[str, Any]) -> Generator[str, None, None]:
        """Generate structure class method code lines."""
        if "__init__" not in namespace:
            yield from self.iter_init_lines()

        for member in self.new_members:
            yield from member.iter_getter_lines()
            yield from member.iter_setter_lines()

        if "__pack__" not in namespace:
            yield from self.iter_pack_lines()

        if "__unpack__" not in namespace:
            yield from self.iter_unpack_lines()

        if "__eq__" not in namespace:
            yield from self.iter_compare("eq")

        if "__ne__" not in namespace:
            yield from self.iter_compare("ne")

        if "__repr__" not in namespace:
            yield from self.iter_repr()
