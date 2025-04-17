# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Transform dict/iterable values to bytes and vice versa."""

import sys
from enum import Enum
from typing import Any, Dict, Iterable, List, Optional, Type, Tuple, Union

from .bytes import BytesX
from .data import Data, DataMeta
from .dump import Record
from .transform import Transform

bytes_x = BytesX(name="bytes")


class Default(Enum):

    """Default sentinel."""

    UNSPECIFIED = "UNSPECIFIED"


if sys.version_info >= (3, 8):  # pragma: no cover
    from typing import Literal

    DefaultUnspecified = Literal[Default.UNSPECIFIED]

else:  # pragma: no cover
    DefaultUnspecified = Default

ItemsFormat = Union[
    Dict[str, Any], List[Any], Transform, Tuple[Any, ...], Type[Data], None
]
DefaultFormat = Union[
    Dict[str, Any],
    List[Any],
    Transform,
    Tuple[Any, ...],
    Type[Data],
    None,
    DefaultUnspecified,
]


def calcsize(fmt: ItemsFormat) -> Union[int, None]:
    """Calculate format size (return None if not a fixed size)."""
    if fmt is None:
        return None

    if isinstance(fmt, (Transform, DataMeta)):
        return fmt.__nbytes__

    if isinstance(fmt, dict):
        sizes = [calcsize(f) for f in fmt.values()]
    elif isinstance(fmt, (tuple, list)):
        sizes = [calcsize(f) for f in fmt]
    else:
        raise TypeError(f"invalid format {fmt!r}")

    try:
        return sum(sizes)  # type: ignore
    except TypeError:
        # must be None in list indicating something variable size
        return None


class ItemsX(Transform):

    """Value to bytes and bytes to value transformer."""

    _fmt: ItemsFormat

    def __init__(
        self,
        fmt: ItemsFormat = None,
        name: Optional[str] = None,
        hint: Optional[str] = None,
    ) -> None:
        hint = self._get_hint(fmt)

        if name is None:
            name = hint

        super().__init__(name, hint)

        self.__nbytes__ = calcsize(fmt)
        self._fmt = fmt

    def _get_hints(self, formats: Iterable[ItemsFormat]) -> List[str]:
        hints = []
        for fmt in formats:
            if fmt is None:
                hints.append("Any")
            elif isinstance(fmt, (dict, list, tuple)):
                hints.append(self._get_hint(fmt))
            else:
                hints.append(fmt.__hint__)
        return hints

    def _get_hint(self, fmt: ItemsFormat) -> str:
        # pylint: disable=too-many-return-statements
        if fmt is None:
            return "Any"

        if isinstance(fmt, dict):
            hints = set(self._get_hints(fmt.values()))
            if len(hints) == 1:
                return f"Dict[str, {hints.pop()}]"
            return "Dict[str, Any]"

        if isinstance(fmt, tuple):
            return f"Tuple[{', '.join(self._get_hints(fmt))}]"

        if isinstance(fmt, list):
            hints = set(self._get_hints(fmt))
            if len(hints) == 1:
                return f"List[{hints.pop()}]"

            return "List[Any]"

        return fmt.__hint__

    @property
    def fmt(self) -> ItemsFormat:
        """Items format."""
        return self._fmt

    def __pack__(
        self,
        value: Any,
        pieces: List[bytes],
        dump: Optional[Record] = None,
        fmt: DefaultFormat = Default.UNSPECIFIED,
    ) -> None:
        # pylint: disable=too-many-branches,arguments-differ
        if dump is not None:
            self.__pack_and_dump__(value, pieces, dump, fmt)

        else:
            if fmt is Default.UNSPECIFIED:
                fmt = self._fmt

            if fmt is None:
                if isinstance(value, (bytes, bytearray)):
                    pieces.append(value)

                elif isinstance(value, tuple):
                    item, bound_fmt = value
                    self.__pack__(item, pieces, dump, bound_fmt)

                elif isinstance(value, Data):
                    value.__pack__(value, pieces, dump)

                elif isinstance(value, list):
                    for item in value:
                        self.__pack__(item, pieces, dump)

                elif isinstance(value, dict):
                    for item in value.values():
                        self.__pack__(item, pieces, dump)

                else:
                    raise TypeError("invalid value")

            elif isinstance(fmt, dict):
                if not isinstance(value, dict) or (set(value) - set(fmt)):
                    raise TypeError("invalid value")

                for name, subfmt in fmt.items():
                    if isinstance(subfmt, (DataMeta, Transform)):
                        subfmt.__pack__(value[name], pieces, dump)
                    else:
                        # must be dict, list, tuple
                        self.__pack__(value[name], pieces, dump, subfmt)

            elif isinstance(fmt, (tuple, list)):
                if not isinstance(value, (tuple, list)) or len(value) != len(fmt):
                    raise TypeError("invalid value")

                for subfmt, item in zip(fmt, value):
                    if isinstance(subfmt, (DataMeta, Transform)):
                        subfmt.__pack__(item, pieces, dump)
                    else:
                        # must be dict, list, tuple
                        self.__pack__(item, pieces, dump, subfmt)

            else:
                fmt.__pack__(value, pieces, dump)

    def __pack_and_dump__(
        self,
        value: Any,
        pieces: List[bytes],
        dump: Record,
        fmt: DefaultFormat = Default.UNSPECIFIED,
    ):
        # pylint: disable=too-many-statements,too-many-branches
        # pylint: disable=too-many-locals,arguments-differ
        if fmt is Default.UNSPECIFIED:
            fmt = self._fmt
            dump.fmt = self.__format_name__

        if fmt is None:
            if dump.fmt:
                dump.fmt = f"{dump.fmt}:"

            if isinstance(value, (bytes, bytearray)):
                dump.fmt += "bytes"
                bytes_x.__pack__(value, pieces, dump)

            elif isinstance(value, tuple):
                try:
                    item, bound_fmt = value
                except ValueError:
                    dump.value = value
                    dump.fmt += "unknown"
                    raise ValueError(
                        f"expected (value, fmt) pair, but got tuple of length {len(value)}"
                    ) from None
                dump.fmt = bound_fmt
                self.__pack_and_dump__(item, pieces, dump, bound_fmt)

            elif isinstance(value, Data):
                dump.fmt += type(value).name
                value.__pack__(value, pieces, dump)

            elif isinstance(value, list):
                dump.fmt += "list"
                for i, item in enumerate(value):
                    self.__pack_and_dump__(
                        item, pieces, dump.add_record(access=f"[{i}]"), fmt=None
                    )

            elif isinstance(value, dict):
                dump.fmt += "dict"
                for name, item in value.items():
                    self.__pack_and_dump__(
                        item, pieces, dump.add_record(access=f"[{name!r}]"), fmt=None
                    )

            else:
                dump.fmt += type(value).__name__ + " (invalid)"
                dump.value = value

                raise TypeError(
                    "no format specified, value must be a packable "
                    "data type or (value, fmt) pairing (or dict/list of them)"
                )

        elif isinstance(fmt, dict):
            if not isinstance(value, dict):
                dump.fmt = "dict"
                dump.value = value
                raise TypeError(f"invalid value, expected dict, got {value!r}")

            missing = []

            for name, subfmt in fmt.items():
                subdump = dump.add_record(access=f"[{name!r}]")

                if isinstance(subfmt, (DataMeta, Transform)):
                    subdump.fmt = subfmt.name

                try:
                    subvalue = value[name]
                except KeyError:
                    missing.append(name)
                    subdump.value = "(missing)"
                    continue

                if isinstance(subfmt, (DataMeta, Transform)):
                    subfmt.__pack__(subvalue, pieces, subdump)
                else:
                    # must be dict, list, tuple
                    self.__pack_and_dump__(subvalue, pieces, subdump, subfmt)

            if missing:
                if len(missing) > 1:
                    missing_values = f"missing values: {repr(missing)[1:-1]}"
                else:
                    missing_values = f"missing value: {missing[0]!r}"
                raise TypeError(missing_values)

            extra_keys = set(value) - set(fmt)

            if extra_keys:
                separate = True
                for name in extra_keys:
                    dump.add_record(
                        access=f"[{name!r}]",
                        value=value[name],
                        fmt="(unexpected)",
                        separate=separate,
                    )
                    separate = False

                value_s = "value" if len(extra_keys) == 1 else "values"
                names = ", ".join(repr(name) for name in extra_keys)
                raise TypeError(f"unexpected {value_s}: {names}")

        elif isinstance(fmt, (tuple, list)):
            if not isinstance(value, (tuple, list)):
                dump.fmt = "tuple or list"
                dump.value = value
                raise TypeError(f"invalid value, expected list or tuple, got {value!r}")

            for i, (subfmt, item) in enumerate(zip(fmt, value)):
                subdump = dump.add_record(access=f"[{i}]")
                if isinstance(subfmt, (DataMeta, Transform)):
                    subdump.fmt = subfmt.name
                    subfmt.__pack__(item, pieces, subdump)
                else:
                    # must be dict, list, tuple, None
                    self.__pack_and_dump__(item, pieces, subdump, subfmt)

            if len(value) != len(fmt):
                if len(value) < len(fmt):
                    for i in range(len(value), len(fmt)):
                        dump.add_record(fmt=fmt[i], value="(missing)", access=f"[{i}]")
                else:
                    separate = True
                    for i in range(len(fmt), len(value)):
                        dump.add_record(
                            fmt="(unexpected)",
                            value=value[i],
                            access=f"[{i}]",
                            separate=separate,
                        )
                        separate = False

                value_s = "value" if len(value) == 1 else "values"
                raise TypeError(f"{len(value)} {value_s} given, expected {len(fmt)}")

        elif isinstance(fmt, (DataMeta, Transform)):
            dump.fmt = fmt.name
            fmt.__pack__(value, pieces, dump)
        else:
            if isinstance(fmt, type):
                dump.fmt = fmt.__name__ + " (invalid)"
            else:
                dump.fmt = str(fmt) + " (invalid)"

            dump.value = value

            raise TypeError(
                "bad item format, must be a packable data type/transform "
                "(or a dict, list, or tuple of them)"
            )

    def __unpack__(
        self,
        buffer: bytes,
        offset: int,
        dump: Optional[Record] = None,
        fmt: DefaultFormat = Default.UNSPECIFIED,
    ) -> Tuple[Any, int]:
        # pylint: disable=arguments-differ
        if dump is not None:
            return self.__unpack_and_dump__(buffer, offset, dump, fmt)

        if fmt is Default.UNSPECIFIED:
            fmt = self._fmt

        if fmt is None:
            return bytes_x.__unpack__(buffer, offset, dump)

        if isinstance(fmt, (list, tuple)):
            list_value = []
            for subfmt in fmt:
                item, offset = self.__unpack__(buffer, offset, dump, subfmt)
                list_value.append(item)

            if isinstance(fmt, tuple):
                return tuple(list_value), offset

            return list_value, offset

        if isinstance(fmt, dict):
            dict_value = {}
            for name, subfmt in fmt.items():
                item, offset = self.__unpack__(buffer, offset, dump, subfmt)
                dict_value[name] = item

            return dict_value, offset

        return fmt.__unpack__(buffer, offset)

    def __unpack_and_dump__(
        self,
        buffer: bytes,
        offset: int,
        dump: Record,
        fmt: DefaultFormat = Default.UNSPECIFIED,
    ) -> Tuple[Any, int]:
        # pylint: disable=arguments-differ
        if fmt is Default.UNSPECIFIED:
            fmt = self._fmt
            dump.fmt = self.__format_name__

        if fmt is None:
            if dump.fmt:
                dump.fmt = f"{dump.fmt}:bytes"
            else:
                dump.fmt = "bytes"

            return bytes_x.__unpack__(buffer, offset, dump)

        if isinstance(fmt, (list, tuple)):
            list_value = []
            for i, subfmt in enumerate(fmt):
                item, offset = self.__unpack_and_dump__(
                    buffer, offset, dump.add_record(access=f"[{i}]"), subfmt
                )
                list_value.append(item)

            if isinstance(fmt, tuple):
                return tuple(list_value), offset

            return list_value, offset

        if isinstance(fmt, dict):
            dict_value = {}
            for name, subfmt in fmt.items():
                item, offset = self.__unpack_and_dump__(
                    buffer, offset, dump.add_record(access=f"[{name!r}]"), subfmt
                )
                dict_value[name] = item

            return dict_value, offset

        if isinstance(fmt, (DataMeta, Transform)):
            dump.fmt = fmt.name
            return fmt.__unpack__(buffer, offset, dump)

        dump.fmt = str(fmt)

        raise TypeError(
            "bad item format, must be a packable data type/transform "
            "(or a dict, list, or tuple of them)"
        )


items = ItemsX(name="items")
