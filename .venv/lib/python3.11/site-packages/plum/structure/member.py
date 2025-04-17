# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure member definition."""

# pylint: disable=too-many-instance-attributes,too-many-public-methods,too-many-arguments

from dataclasses import dataclass, field
from types import FunctionType, MethodType, BuiltinFunctionType, BuiltinMethodType
from typing import Any, Generator, List, Optional, Tuple, Type, Union

from .._code_injector import CodeInjector
from .._default import NO_DEFAULT
from .._typing import FactoryFormat
from ..enum import EnumX
from ..flag import FlagX
from ..data import Data, DataMeta
from ..transform import Transform

FUNCTION_TYPES = (FunctionType, MethodType, BuiltinFunctionType, BuiltinMethodType)


@dataclass
class TempStore:

    """Temporary information store for generating implementation code."""

    num_associated: int = 0

    local_name: str = ""
    cls_name: str = ""
    type_hint: str = ""

    init_parameter: str = ""
    init_pre_begin: List[str] = field(default_factory=list)
    init_begin: List[str] = field(default_factory=list)
    init_end: List[str] = field(default_factory=list)

    pack: List[str] = field(default_factory=list)
    pack_and_dump: List[str] = field(default_factory=list)

    unpack: List[str] = field(default_factory=list)
    unpack_and_dump: List[str] = field(default_factory=list)
    unpack_checks: List[str] = field(default_factory=list)

    getter: List[str] = field(default_factory=list)
    setter: List[str] = field(default_factory=list)


class Member(property):

    """Structure member definition base class.

    :param doc: accessor documentation string
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param compute: initializer defaults to compute based on another member
    :param argrepr: format to represent member argument in structure repr
    :param fmt: member format
    :param fmt_arg: member property to use as format factory argument

    """

    _nbytes: Optional[int]
    _index: Optional[int]
    _temp_store: Optional[TempStore]

    _attributes_to_copy: Tuple[str, ...] = (
        "_argrepr",
        "_compute",
        "_doc",
        "_default",
        "_fmt",
        "_fmt_arg",
        "_ignore",
        "_nbytes",
        "_readonly",
    )

    def __init__(
        self,
        doc: str,
        default: Any,
        ignore: bool,
        readonly: bool,
        compute: bool,
        argrepr: Optional[str],
        fmt: FactoryFormat,
        fmt_arg: Optional["Member"],
    ) -> None:
        property.__init__(self)

        if compute and default is not NO_DEFAULT:
            raise TypeError("'default' may not be specified when 'compute=True'")

        if isinstance(default, property):
            default = default.fget

        nbytes = None

        if isinstance(fmt, (DataMeta, Transform)):
            if fmt_arg is not None:
                raise TypeError(
                    "when 'fmt_arg' specified, 'fmt' must be a factory function"
                )
            nbytes = fmt.__nbytes__

        else:
            if isinstance(fmt, property):
                fmt = fmt.fget

            if isinstance(fmt, FUNCTION_TYPES):
                if not (isinstance(fmt_arg, Member) or fmt_arg is None):
                    raise TypeError("'fmt_arg' must be a structure 'member()'")
            else:
                raise TypeError(
                    "'fmt' must be a data store, transform, or a factory function"
                )

        self._nbytes = nbytes
        self._doc = doc
        self._default = default
        self._ignore = ignore
        self._readonly = readonly
        self._compute = compute
        self._argrepr = argrepr
        self._fmt = fmt
        self._fmt_arg = fmt_arg

        self._name = ""  # assigned during structure class construction
        self._index = None  # assigned during structure class construction

        self._temp_store = None

    @property
    def temp_store(self) -> TempStore:
        """Temporary information store for generating implementation code."""
        store = self._temp_store

        if store is None:
            self._temp_store = store = TempStore()

        return store

    @temp_store.deleter
    def temp_store(self):
        self._temp_store = None

    @property
    def argrepr(self) -> str:
        """Format string to represent member argument in structure repr."""
        if isinstance(self._argrepr, str):
            repr_format = self._argrepr

        elif isinstance(self._fmt, (EnumX, FlagX)):
            repr_format = (
                f"{self.name}={{repr(self.{self.name}).split(':', 1)[0].lstrip('<')}}"
            )

        else:
            repr_format = f"{self.name}={{self.{self.name}!r}}"

        return repr_format

    @property
    def compute(self) -> bool:
        """Initializer defaults to compute based on another member."""
        return self._compute

    @property
    def default_is_a_factory(self) -> bool:
        """Member default is produced by a factory function."""
        return self.compute or isinstance(self.default, FUNCTION_TYPES)

    @property
    def fmt_is_a_factory(self) -> bool:
        """Member format is produced by a factory function."""
        return isinstance(self.fmt, FUNCTION_TYPES)

    @property
    def default(self) -> Any:
        """Structure initializer default value for this structure member."""
        return self._default

    @property
    def doc(self) -> str:
        """Member description."""
        return self._doc

    @property
    def fmt(self) -> Union[Transform, Type[Data]]:
        """Member format."""
        return self._fmt

    @property
    def fmt_arg(self) -> Optional["Member"]:
        """Member property to use as format factory argument."""
        return self._fmt_arg

    @property
    def ignore(self) -> bool:
        """Ignore member when compared against structure of same type."""
        return self._ignore

    @property
    def index(self) -> int:
        """Member number."""
        if self._index is None:  # pragma: no cover (for mypy)
            raise RuntimeError(
                "internal error, likely cause was getter/setter not immediately "
                "following member"
            )
        return self._index

    @index.setter
    def index(self, value: int):
        self._index = value

    @property
    def name(self) -> str:
        """Bit field name."""
        if self._name is None:  # pragma: no cover (for mypy)
            raise RuntimeError("internal error")
        return self._name

    @property
    def nbytes(self) -> Optional[int]:
        """Transform format size in bytes."""
        return self._nbytes

    @property
    def readonly(self) -> bool:
        """Block setting member attribute."""
        return self._readonly

    def copy(self, fget=None, fset=None, name="", index=None):
        """Copy structure member property definition.

        Copy every member property attribute except override with values
        provided as arguments (except always dump temp_store).

        """
        cls = type(self)

        copy = cls.__new__(cls)

        property.__init__(copy, fget, fset, self.fdel)

        for attr_name in self._attributes_to_copy:
            setattr(copy, attr_name, getattr(self, attr_name))

        # pylint: disable=protected-access
        copy._name = name
        copy._index = index
        copy._temp_store = None

        self._temp_store = None

        return copy

    def getter(self, fget):
        """Decorator to change getter method."""
        return self.copy(fget, self.fset, self._name, self._index)

    def setter(self, fset):
        """Decorator to change setter method."""
        if self.readonly:
            raise TypeError(
                "'setter' not allowed on read-only structure member properties"
            )

        return self.copy(self.fget, fset, self._name, self._index)

    def deleter(self, fdel):
        """Decorator to change deleter method."""
        raise TypeError("structure member properties do not support 'deleter'")

    def add_name_index(
        self,
        name: str,
        index: int,
        code_injector: CodeInjector,
    ) -> int:
        """Assign name, index number, and prepare for code generation."""
        # pylint: disable=too-many-branches,too-many-statements,unused-argument
        if self._name:
            raise TypeError(
                f"invalid structure member {name!r} definition, "
                f"member instance can not be shared, create a new instance"
            ) from None

        self._name = name
        self.index = index

        store = self.temp_store

        if self.fmt_is_a_factory:
            store.cls_name = f"{name}_fmt"
        else:
            store.cls_name = f"cls.{name}.fmt"

        store.local_name = "m_" + name
        store.type_hint = code_injector.get_type_hint_expression(name)

        store.init_parameter = self.get_init_parameter()

        if self.default is not NO_DEFAULT and not self.compute:
            init_expr = f"type(self).{name}.default"
            if self.default_is_a_factory:
                target_store = store.init_end
                access_expr = f"self[{self.index}]"
                init_expr += "(self)"
            else:
                target_store = store.init_pre_begin
                access_expr = name
                init_expr = code_injector.get_expression(self.default, init_expr)

            target_store.extend(
                [
                    f"if {name} is None:",
                    f"    {access_expr} = {init_expr}",
                ]
            )

        if not self.fget:
            store.getter.append(f"return self[{self.index}]")

        if not self.readonly and not self.fset:
            store.setter.append(f"self[{self.index}] = value")

        dump = f'dump.add_record(access="{name}", fmt={store.cls_name})'
        extra = self.extra_args

        if self.fmt_is_a_factory:
            if self.fmt_arg is None:
                cls_factory = [f"{store.cls_name} = cls.{name}.fmt(value)"]
            else:
                cls_factory = [
                    f"{store.cls_name} = cls.{name}.fmt(m_{self.fmt_arg.name})"
                ]
        else:
            cls_factory = []

        store.pack += cls_factory + [
            f"{store.cls_name}.__pack__(m_{name}, pieces, dump{extra})",
        ]
        store.pack_and_dump += cls_factory + [
            f"{name}_dump = {dump}",
            f"{store.cls_name}.__pack__(m_{name}, pieces, {name}_dump{extra})",
        ]

        if self.fmt_is_a_factory:
            if self.fmt_arg is None:
                # FUTURE change structure -> value
                cls_factory = [f"{store.cls_name} = cls.{name}.fmt(structure)"]
            else:
                cls_factory = [
                    f"{store.cls_name} = cls.{name}.fmt(m_{self.fmt_arg.name})"
                ]
        else:
            cls_factory = []

        store.unpack += cls_factory + [
            f"m_{name}, offset = {store.cls_name}.__unpack__(buffer, offset, dump{extra})",
        ]

        store.unpack_and_dump += cls_factory + [
            f"{name}_dump = {dump}",
            f"m_{name}, offset = {store.cls_name}.__unpack__(buffer, offset, {name}_dump{extra})",
        ]

        if (
            self.readonly
            and (self.default is not NO_DEFAULT)
            and not self.default_is_a_factory
        ):
            alternative = f"cls.{name}.default"
            default = code_injector.get_expression(self.default, alternative)
            store.unpack_checks += [
                f"if m_{name} != {default}:",
                f'    raise ValueError(f"{name!r} must be {{{default}}}")',
            ]

        return index + 1

    def iter_getter_lines(self) -> Generator[str, None, None]:
        """Iterate generated getter implementation lines."""

        store = self.temp_store

        lines = store.getter

        if lines:
            type_hint = f" -> {store.type_hint}" if store.type_hint else ""

            yield f"@{self.name}.getter"
            yield f"def {self.name}(self){type_hint}:"
            if self.doc:
                yield f'    """{self.doc}"""'
            for line in lines:
                yield ("    " + line).rstrip()
            yield ""

    def iter_setter_lines(self) -> Generator[str, None, None]:
        """Iterate generated setter implementation lines."""
        store = self.temp_store

        lines = store.setter

        if lines:
            type_hint = f": {store.type_hint}" if store.type_hint else ""

            yield f"@{self.name}.setter"
            yield f"def {self.name}(self, value{type_hint}) -> None:"
            if self.doc:
                yield f'    """{self.doc}"""'
            for line in lines:
                yield ("    " + line).rstrip()
            yield ""

    def get_init_parameter(self) -> str:
        """Get member parameter for structure __init__ method.

        Include type annotation where possible.

        """
        parameter = self.name

        type_hint = self.temp_store.type_hint
        is_optional = self.default is not NO_DEFAULT or self.compute

        if type_hint:
            if is_optional:
                type_hint = f"Optional[{type_hint}]"

            parameter += f": {type_hint}"

        if is_optional:
            parameter += " = None"

        return parameter

    @property
    def extra_args(self) -> str:
        """Additional __pack__ and __unpack__ arguments (for code generation)."""
        return ""

    def check(self):
        """Perform final checks."""
        if self.compute and not self.temp_store.num_associated:
            raise TypeError(
                f"{self.name!r} member never associated with member "
                f"used to compute it"
            )

        # self._temp_store = None

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"


def member(
    doc: str = "",
    *,
    default: Any = NO_DEFAULT,
    ignore: bool = False,
    readonly: bool = False,
    compute: bool = False,
    argrepr: Optional[str] = None,
    fmt: FactoryFormat,
    fmt_arg: Optional["Member"] = None,
) -> Any:
    """Define structure member properties.

    :param doc: accessor documentation string
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param compute: initializer defaults to compute based on another member
    :param argrepr: format to represent member argument in structure repr
    :param fmt: member format
    :param fmt_arg: member property to use as format factory argument

    """
    return Member(doc, default, ignore, readonly, compute, argrepr, fmt, fmt_arg)
