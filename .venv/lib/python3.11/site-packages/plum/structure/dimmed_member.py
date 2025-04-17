# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Variable dimensions array structure member definition."""

# pylint: disable=too-many-arguments

from typing import Any, Generator, List, Optional, Tuple

from .._code_injector import CodeInjector
from .._default import NO_DEFAULT
from ..array import ArrayX
from ..int import IntX
from .member import Member


class DimmedMember(Member):

    """Variably dimensioned array structure member definition.

    :param doc: accessor documentation string
    :param fmt: array transform (or factory function)
    :param dims: array dimensions member definition
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """

    _attributes_to_copy: Tuple[str, ...] = Member._attributes_to_copy + ("_dims",)

    def __init__(
        self,
        doc: str,
        fmt: ArrayX,
        dims: Member,
        default: Any,
        ignore: bool,
        readonly: bool,
        argrepr: Optional[str],
    ) -> None:
        compute = False
        fmt_arg = None
        super().__init__(
            doc,
            default,
            ignore,
            readonly,
            compute,
            argrepr,
            fmt,
            fmt_arg,
        )

        error = False

        if not isinstance(dims, Member):
            error = True

        elif isinstance(dims.fmt, ArrayX):
            dims_dims, _fmt = dims.fmt.__df__

            if not isinstance(dims_dims, tuple) or len(dims_dims) != 1:
                error = True

        elif not isinstance(dims.fmt, IntX):
            error = True

        if error:
            raise TypeError(
                "invalid 'dims', must be a member() where 'fmt' is either "
                "an integer transform or an array transform with a single dim "
                "and non-greedy"
            )

        self._dims: Member = dims

    @property
    def dims(self) -> Member:
        """Array dimensions member definition."""
        return self._dims

    @staticmethod
    def compute_dims(array: List[Any], ndims: int) -> Generator[int, None, None]:
        """Determine dimensions from multi-dimensional array value."""
        for _ in range(ndims):
            yield len(array)
            array = array[0]

    def add_name_index(
        self,
        name: str,
        index: int,
        code_injector: CodeInjector,
    ) -> int:
        """Assign name, index number, and prepare for code generation."""
        dims = self.dims

        dims.temp_store.num_associated += 1

        if dims.compute:

            # add logic to __init__ to compute dimensions when it was left to default
            if isinstance(dims.fmt, IntX):
                computation = f"len({name})"
            else:
                # must be ArrayX
                dims_dims, _fmt = dims.fmt.__df__
                ndims = dims_dims[0]
                computation = f"list(type(self).{name}.compute_dims({name}, {ndims}))"

            dims.temp_store.init_begin += [
                f"if {dims.name} is None:",
                f"    {dims.name} = {computation}",
            ]

            # add logic to this member's setter to recompute associated dims member
            # (but only when setter not explicitly defined in structure class)
            if not self.readonly and not self.fset:
                if isinstance(self.dims.fmt, IntX):
                    computation = "len(value)"
                else:  # must be ArrayX
                    dims_dims, _fmt = self.dims.fmt.__df__
                    num_dims = dims_dims[0]
                    computation = (
                        f"list(type(self).{name}.compute_dims(value, {num_dims}))"
                    )
                self.temp_store.setter.append(
                    f"self[{self.dims.index}] = {computation}  "
                    f"# update {self.dims.name!r} member"
                )

        return Member.add_name_index(self, name, index, code_injector)

    @property
    def extra_args(self) -> str:
        """Additional __pack__ and __unpack__ arguments (for code generation)."""
        if isinstance(self.dims.fmt, IntX):
            args = f", dims=(m_{self.dims.name}, )"
        else:
            args = f", dims=m_{self.dims.name}"

        return args


def dimmed_member(
    doc: str = "",
    *,
    fmt: ArrayX,
    dims: Member,
    default: Any = NO_DEFAULT,
    ignore: bool = False,
    readonly: bool = False,
    argrepr: Optional[str] = None,
) -> Any:
    """Define variably dimensioned array structure member.

    :param doc: accessor documentation string
    :param fmt: array transform (or factory function)
    :param dims: array dimensions member definition
    :param default: initializer default value
    :param ignore: ignore member during comparisons
    :param readonly: block setting member attribute
    :param argrepr: format to represent member argument in structure repr

    """
    return DimmedMember(doc, fmt, dims, default, ignore, readonly, argrepr)
