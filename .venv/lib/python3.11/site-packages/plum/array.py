# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Array to bytes and bytes to array transform."""

from typing import Any, Generator, List, Optional, Sequence, Tuple, Union

from ._typing import Format
from .data import DataMeta
from .dump import Record
from .int import IntX
from .transform import Transform

Dims = Sequence[Optional[int]]
DimsArg = Union[Dims, "ArrayX", IntX]

GREEDY_DIMS: Dims = (None,)


def iterate_dims(array: Sequence[Any], ndims: int) -> Generator[int, None, None]:
    """Determine dimensions from multi-dimensional array value."""
    for _ in range(ndims):
        yield len(array)
        array = array[0]


class ArrayX(Transform):

    """Array to bytes and bytes to array transform."""

    __ndims__: int
    __df__: Tuple[DimsArg, Format]

    def __init__(
        self,
        fmt: Format,
        dims: Optional[DimsArg] = None,
        name: Optional[str] = None,
    ) -> None:
        assert isinstance(fmt, (DataMeta, Transform))

        locked_dims: DimsArg

        num_dims = 1

        if dims is None:
            locked_dims = GREEDY_DIMS

        elif isinstance(dims, IntX):
            locked_dims = dims

        elif isinstance(dims, ArrayX):
            locked_dims = dims
            dims_dims, _fmt = dims.__df__

            if (
                not isinstance(dims_dims, tuple)
                or len(dims_dims) != 1
                or dims_dims[0] is None
            ):
                raise TypeError(
                    "invalid 'dims', when providing an array transform for `dims`, "
                    "it must have a single, fixed (non-greedy) dimension"
                )

            num_dims = dims_dims[0]

        else:
            locked_dims = tuple(None if d is None else int(d) for d in dims)
            assert all(True if d is None else d > 0 for d in locked_dims)
            num_dims = len(dims)

        nbytes: Optional[int] = fmt.__nbytes__

        if nbytes is not None:
            if isinstance(locked_dims, tuple):
                for dim in locked_dims:
                    if dim is None:
                        nbytes = None
                        break

                    nbytes *= dim

            else:
                nbytes = None

        hint = fmt.__hint__ or "Any"

        for _ in range(num_dims):
            hint = f"List[{hint}]"

        if name is None:
            name = hint

        super().__init__(name, hint)

        self.__df__ = locked_dims, fmt
        self.__ndims__ = num_dims
        self.__nbytes__ = nbytes

    @property
    def fmt(self) -> Format:
        """Array element format."""
        return self.__df__[1]

    @property
    def dims(self) -> DimsArg:
        """Array dimensions."""
        return self.__df__[0]

    def __unpack__(
        self,
        buffer: bytes,
        offset: int,
        dump: Optional[Record] = None,
        dims: Optional[Dims] = None,
    ) -> Tuple[List[Any], int]:
        # pylint: disable=arguments-differ,too-many-branches
        if dump is not None:
            return ArrayX.__unpack_and_dump__(self, buffer, offset, dump, dims)

        x_dims, fmt = self.__df__

        if dims is None:
            if isinstance(x_dims, tuple):
                dims = x_dims
                if None in dims[1:]:
                    raise TypeError(
                        "array unpack does not support greedy secondary dimensions"
                    )

            elif isinstance(x_dims, IntX):
                dim, offset = x_dims.__unpack__(buffer, offset, dump)
                dims = (dim,)

            elif isinstance(x_dims, ArrayX):
                # must be isinstance(x_dims, ArrayX):
                dims, offset = x_dims.__unpack__(buffer, offset, dump)

            else:  # pragma: no cover
                raise RuntimeError("unexpected implementation error")

        array: List[Any] = []
        append = array.append

        this_dim, *item_dims = dims

        if this_dim is None:
            end = len(buffer)
            while offset < end:
                item, offset = fmt.__unpack__(buffer, offset, dump)
                append(item)

        elif item_dims:
            for _ in range(this_dim):
                item, offset = ArrayX.__unpack__(self, buffer, offset, dump, item_dims)
                append(item)
        else:
            for _ in range(this_dim):
                item, offset = fmt.__unpack__(buffer, offset, dump)
                append(item)

        return array, offset

    def __unpack_and_dump__(
        self,
        buffer: bytes,
        offset: int,
        dump: Record,
        dims: Optional[Dims] = None,
    ) -> Tuple[List[Any], int]:
        # pylint: disable=arguments-differ,too-many-locals,too-many-branches
        x_dims, fmt = self.__df__

        if dims is None:
            if isinstance(x_dims, tuple):
                dims = x_dims
                if None in dims[1:]:
                    raise TypeError(
                        "array unpack does not support greedy secondary dimensions"
                    )

            elif isinstance(x_dims, IntX):
                dim, offset = x_dims.__unpack__(
                    buffer, offset, dump.add_record(access="len()", fmt=x_dims)
                )
                dims = (dim,)

            elif isinstance(x_dims, ArrayX):
                dims, offset = x_dims.__unpack__(
                    buffer, offset, dump.add_record(access="--dims--", fmt=x_dims)
                )

            else:  # pragma: no cover
                raise RuntimeError(f"invalid 'dims' {x_dims!r}")

        array: List[Any] = []
        append = array.append

        this_dim, *item_dims = dims

        if this_dim is None:
            end = len(buffer)
            i = 0
            fmt_name = fmt.name
            while offset < end:
                item, offset = fmt.__unpack__(
                    buffer, offset, dump.add_record(access=f"[{i}]", fmt=fmt_name)
                )
                append(item)
                i += 1

        elif item_dims:
            for i in range(this_dim):
                item, offset = ArrayX.__unpack_and_dump__(
                    self, buffer, offset, dump.add_record(access=f"[{i}]"), item_dims
                )
                append(item)
        else:
            fmt_name = fmt.name
            for i in range(this_dim):
                item, offset = fmt.__unpack__(
                    buffer, offset, dump.add_record(access=f"[{i}]", fmt=fmt_name)
                )
                append(item)

        if not array:
            dump.value = []

        return array, offset

    def __pack__(
        self,
        value: Sequence[Any],
        pieces: List[bytes],
        dump: Optional[Record] = None,
        dims: Optional[Dims] = None,
    ) -> None:
        # pylint: disable=arguments-differ,too-many-branches
        if dump is not None:
            ArrayX.__pack_and_dump__(self, value, pieces, dump, dims)

        else:
            x_dims, fmt = self.__df__

            if dims is None:
                if isinstance(x_dims, tuple):
                    this_dim, *item_dims = x_dims

                elif isinstance(x_dims, IntX):
                    this_dim, item_dims = len(value), []
                    x_dims.__pack__(this_dim, pieces, dump)

                elif isinstance(x_dims, ArrayX):
                    dims = tuple(iterate_dims(value, self.__ndims__))
                    this_dim, *item_dims = dims
                    x_dims.__pack__(dims, pieces, dump)

                else:  # pragma: no cover
                    raise RuntimeError(f"invalid 'dims' {x_dims!r}")

            else:
                this_dim, *item_dims = dims

            try:
                actual_length = len(value)
            except TypeError:
                raise TypeError("invalid array value, retrying with dump") from None

            if this_dim is not None and actual_length != this_dim:
                raise TypeError("invalid array value, retrying with dump")

            if item_dims:
                for item in value:
                    ArrayX.__pack__(self, item, pieces, dump, item_dims)
            else:
                for item in value:
                    fmt.__pack__(item, pieces, dump)

    def __pack_and_dump__(
        self,
        value: Sequence[Any],
        pieces: List[bytes],
        dump: Record,
        dims: Optional[Dims] = None,
    ) -> None:
        # pylint: disable=arguments-differ,too-many-branches
        x_dims, fmt = self.__df__

        if dims is None:
            if isinstance(x_dims, tuple):
                this_dim, *item_dims = x_dims

            elif isinstance(x_dims, IntX):
                this_dim, item_dims = len(value), []
                x_dims.__pack__(
                    this_dim, pieces, dump.add_record(access="len()", fmt=x_dims)
                )

            elif isinstance(x_dims, ArrayX):
                dims = tuple(iterate_dims(value, self.__ndims__))
                this_dim, *item_dims = dims
                x_dims.__pack__(
                    dims, pieces, dump.add_record(access="--dims--", fmt=x_dims)
                )

            else:  # pragma: no cover
                raise RuntimeError(f"invalid 'dims' {x_dims!r}")

        else:
            this_dim, *item_dims = dims

        try:
            actual_length = len(value)
        except TypeError:
            dump.value = value
            raise TypeError(
                f"invalid value, expected iterable of "
                f'{"any " if this_dim is None else ""}'
                f'length{"" if this_dim is None else " " + str(this_dim)}'
                f", got non-iterable"
            ) from None

        if not actual_length:
            dump.value = []

        if this_dim is None:
            this_dim = actual_length

        if item_dims:
            for i, item in zip(range(this_dim), value):
                ArrayX.__pack_and_dump__(
                    self, item, pieces, dump.add_record(access=f"[{i}]"), item_dims
                )
        else:
            fmt_name = fmt.name

            for i, item in zip(range(this_dim), value):
                fmt.__pack__(
                    item, pieces, dump.add_record(access=f"[{i}]", fmt=fmt_name)
                )

        if actual_length != this_dim:
            for i in range(actual_length, this_dim):
                dump.add_record(access=f"[{i}]", value="<missing>")

            for i, item in zip(range(this_dim, actual_length), value[this_dim:]):
                dump.add_record(
                    access=f"[{i}] <extra>", value=item, separate=(i == this_dim)
                )
            raise TypeError(
                f"invalid value, expected iterable of "
                f"{this_dim} length, got iterable of length {actual_length}"
            )
