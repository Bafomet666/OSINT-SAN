# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Common typing hints."""

import sys
from typing import Any, Callable, Type, Union

from .data import Data
from .transform import Transform

if sys.version_info < (3, 8):
    ByteOrderHint = str
else:
    from typing import Literal

    ByteOrderHint = Union[Literal["little"], Literal["big"]]


Format = Union[Transform, Type[Data]]
FactoryFormat = Union[Callable[[Type[Any]], Format], Transform, Type[Data]]
