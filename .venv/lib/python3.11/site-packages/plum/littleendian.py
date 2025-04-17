# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Common transforms in little endian format."""

from .float import FloatX
from .int import IntX

sint8 = IntX(nbytes=1, byteorder="little", signed=True)
sint16 = IntX(nbytes=2, byteorder="little", signed=True)
sint32 = IntX(nbytes=4, byteorder="little", signed=True)
sint64 = IntX(nbytes=8, byteorder="little", signed=True)

uint8 = IntX(nbytes=1, byteorder="little", signed=False)
uint16 = IntX(nbytes=2, byteorder="little", signed=False)
uint32 = IntX(nbytes=4, byteorder="little", signed=False)
uint64 = IntX(nbytes=8, byteorder="little", signed=False)

single = FloatX(nbytes=4, byteorder="little")
double = FloatX(nbytes=8, byteorder="little")
