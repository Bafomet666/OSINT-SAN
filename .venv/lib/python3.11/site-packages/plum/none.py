# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""None to no bytes and no bytes to None transform."""

from typing import List, Optional, Tuple

from .dump import Record
from .transform import Transform


class NoneX(Transform):

    """None to no bytes and no bytes to None transform."""

    __nbytes__ = 0

    def __init__(self, name: str = "None") -> None:
        super().__init__(name, hint="None")

    def __pack__(
        self, value: None, pieces: List[bytes], dump: Optional[Record] = None
    ) -> None:
        if dump is not None:
            dump.value = repr(value)

        if value is not None:
            raise TypeError("value must be 'None'")

    def __unpack__(
        self, buffer: bytes, offset: int, dump: Optional[Record] = None
    ) -> Tuple[None, int]:
        if dump is not None:
            dump.value = "None"

        return None, offset
