# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Common transforms in big endian format."""

from .float import FloatX
from .int import IntX


sint8 = IntX(nbytes=1, byteorder="big", signed=True)
sint16 = IntX(nbytes=2, byteorder="big", signed=True)
sint32 = IntX(nbytes=4, byteorder="big", signed=True)
sint64 = IntX(nbytes=8, byteorder="big", signed=True)

uint8 = IntX(nbytes=1, byteorder="big", signed=False)
uint16 = IntX(nbytes=2, byteorder="big", signed=False)
uint32 = IntX(nbytes=4, byteorder="big", signed=False)
uint64 = IntX(nbytes=8, byteorder="big", signed=False)

single = FloatX(nbytes=4, byteorder="big")
double = FloatX(nbytes=8, byteorder="big")
