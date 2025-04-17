# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""BitFields __init__ and property methods generator."""

from enum import EnumMeta
from typing import Any, Dict, Generator, Tuple, ValuesView

from ..enum import EnumX
from .bitfield import BitField

INDENT = "    "


class CodeMaker:

    """BitFields method code generator."""

    bitfields: Tuple[BitField, ...]

    def __init__(
        self,
        bitfields: ValuesView[BitField],
    ) -> None:
        self.bitfields = tuple(bitfields)

        self.hints = {}
        self.typ_params = {}
        self.typ_names = {}

        for bitfield in bitfields:
            bitfield_name = bitfield.name
            bitfield_typ = bitfield.typ

            if bitfield_typ in {int, bool}:
                hint = typ_name = bitfield_typ.__name__

            elif isinstance(bitfield_typ, EnumX):
                # assume not strict (otherwise definition would just use Enum)
                hint = f"Union[int, '{bitfield_typ.enum.__name__}']"
                typ_name = "_typ"

            else:
                # must be BitFields type or IntEnum
                hint = repr(bitfield_typ.__name__)
                typ_name = "_typ"

            if typ_name == "_typ":
                self.typ_params[bitfield_name] = f", _typ={bitfield_name}.typ"
            else:
                self.typ_params[bitfield_name] = ""

            self.typ_names[bitfield_name] = typ_name
            self.hints[bitfield_name] = hint

    def iter_init_lines(self, default: int) -> Generator[str, None, None]:
        """Generate __init__ method lines."""
        parameters = []

        for bitfield in self.bitfields:
            parameter = f"{bitfield.name}: {self.hints[bitfield.name]}"

            if bitfield.default is not None:
                parameter += f" = {bitfield.default}"

            parameters.append(parameter)

        args = ", ".join(parameters)

        if args:
            yield f"def __init__(self, *, {args}) -> None:"
        else:
            yield "def __init__(self) -> None:"
        yield INDENT + f"self.__value__ = {default}"

        for bitfield in self.bitfields:
            yield INDENT + f"self.{bitfield.name} = {bitfield.name}"

        yield ""

    def iter_getter_lines(self, bitfield: BitField):
        """Generate getter."""
        bitfield_name = bitfield.name

        yield f"@{bitfield_name}.getter"
        yield f"def {bitfield_name}(self{self.typ_params[bitfield_name]}) -> {self.hints[bitfield_name]}:"
        if bitfield.doc:
            yield INDENT + f'"""{bitfield.doc}"""'

        if bitfield.lsb:
            retval = f"(int(self) >> {bitfield.lsb}) & {bitfield.mask}"
        else:
            retval = f"int(self) & {bitfield.mask}"

        if bitfield.signed:
            yield INDENT + f"value = {retval}"
            yield INDENT + f"value = -((1 << {bitfield.size}) - value) if {bitfield.signbit} & value else value"
            retval = "value"

        if hasattr(bitfield.typ, "__fields__"):
            yield INDENT + f"value = _typ.from_int({retval})"
            yield INDENT + "try:"
            yield INDENT + "    bitoffset, store = self.__bitoffset_store__"
            yield INDENT + "except AttributeError:"
            yield INDENT + f"    bitoffset, store = {bitfield.lsb}, self"
            if bitfield.lsb:
                yield INDENT + "else:"
                yield INDENT + f"    bitoffset += {bitfield.lsb}"
            yield INDENT + "value.__bitoffset_store__ = bitoffset, store"
            retval = "value"

        elif self.typ_names[bitfield_name] != "int":
            retval = f"{self.typ_names[bitfield_name]}({retval})"

        yield INDENT + f"return {retval}"
        yield ""

    def iter_setter_lines(self, bitfield: BitField, nested: bool):
        """Generate setter."""
        bitfield_name = bitfield.name

        typ = bitfield.typ
        hint = self.hints[bitfield_name]
        typ_param = self.typ_params[bitfield_name]
        typ_name = self.typ_names[bitfield_name]

        yield f"@{bitfield_name}.setter"
        yield f"def {bitfield_name}(self, value: {hint}{typ_param}) -> None:"
        if bitfield.doc:
            yield INDENT + f'"""{bitfield.doc}"""'

        if hasattr(bitfield.typ, "__fields__"):
            yield INDENT + "value = int(_typ.from_int(value))"
        elif typ_name == "int":
            yield INDENT + "value = int(value)"
        else:
            yield INDENT + f"value = int({typ_name}(value))"

        if (
            not hasattr(typ, "__fields__")
            and not isinstance(typ, EnumMeta)
            and typ is not bool
        ):
            yield INDENT + f"if not ({bitfield.minvalue} <= value <= {bitfield.maxvalue}):"
            yield INDENT + f'    raise ValueError("bit field {bitfield_name!r} requires {bitfield.minvalue} <= number <= {bitfield.maxvalue}")'

        if nested:
            yield INDENT + "try:"
            yield INDENT + "    bitoffset, store = self.__bitoffset_store__"
            yield INDENT + "except AttributeError:"
            yield INDENT + f"    bitoffset, store = {bitfield.lsb}, self"
            if bitfield.lsb:
                yield INDENT + "else:"
                yield INDENT + f"    bitoffset += {bitfield.lsb}"
            yield INDENT + f"store.__value__ = (store.__value__ & ~({bitfield.mask} << bitoffset)) | ((value & {bitfield.mask}) << bitoffset)"
        elif bitfield.lsb:
            yield INDENT + f"self.__value__ = (self.__value__ & {~(bitfield.mask << bitfield.lsb)}) | ((value & {bitfield.mask}) << {bitfield.lsb})"
        else:
            yield INDENT + f"self.__value__ = (self.__value__ & {~bitfield.mask}) | (value & {bitfield.mask})"
        yield ""

    def iter_repr_lines(self) -> Generator[str, None, None]:
        """Bitfields __repr__ method generator."""
        arg_reprs = ", ".join(f.argrepr for f in self.bitfields if f.argrepr)
        class_name = "{type(self).__name__}"

        yield "def __repr__(self) -> str:"
        yield "    try:"
        yield f'        return f"{class_name}({arg_reprs})"'
        yield "    except Exception:"
        yield f'        return f"{class_name}()"'
        yield ""

    def iter_lines(
        self, namespace: Dict[str, Any], default: int, nested: bool
    ) -> Generator[str, None, None]:
        """Generate BitFields class method code lines."""
        if "__init__" not in namespace:
            yield from self.iter_init_lines(default)

        for bitfield in self.bitfields:
            if bitfield.fget is None:
                yield from self.iter_getter_lines(bitfield)
            if bitfield.fset is None and not bitfield.readonly:
                yield from self.iter_setter_lines(bitfield, nested)

        if "__repr__" not in namespace:
            yield from self.iter_repr_lines()
