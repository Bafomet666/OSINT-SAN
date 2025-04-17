# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""AttrDict to bytes and bytes to AttrDict transform."""

from typing import Any, Dict, List, Optional, Tuple, Union

from .dump import Record
from .transform import Transform
from .exceptions import SizeError


class AttrDict(dict):

    """Dictionary with access to items as attributes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def __repr__(self):
        params = [f"{key}={value!r}" for key, value in self.items()]
        return f"AttrDict({', '.join(params)})"


class AttrDictX(Transform):

    """AttrDict to bytes and bytes to AttrDict transform."""

    __nbytes__: Optional[int]

    members: Dict[str, Any]

    def __init__(
        self,
        members: Union[Dict[str, Any], List[Tuple[str, Any]]],
        name: str = "AttrDict",
    ) -> None:
        super().__init__(name, hint="AttrDict")

        self.members = dict(members)
        self.__nbytes__ = 0

        for transform in self.members.values():
            try:
                self.__nbytes__ += transform.nbytes
            except SizeError:
                self.__nbytes__ = None
                break

    def __unpack__(
        self,
        buffer: bytes,
        offset: int,
        dump: Optional[Record] = None,
    ) -> Tuple[AttrDict, int]:
        attrdict = AttrDict()

        if dump is None:
            for name, transform in self.members.items():
                value, offset = transform.__unpack__(buffer, offset, dump)
                attrdict[name] = value
        elif self.members:
            for name, transform in self.members.items():
                subdump = dump.add_record(access=name, fmt=transform)
                value, offset = transform.__unpack__(buffer, offset, subdump)
                attrdict[name] = value
        else:
            dump.value = {}

        return attrdict, offset

    def __pack__(
        self, value, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        if dump is None:
            for name, transform in self.members.items():
                transform.__pack__(value[name], pieces, dump)

        elif self.members:
            for name, transform in self.members.items():
                subdump = dump.add_record(access=name, fmt=transform)
                member_value = value[name]
                transform.__pack__(member_value, pieces, subdump)

        else:
            dump.value = {}
