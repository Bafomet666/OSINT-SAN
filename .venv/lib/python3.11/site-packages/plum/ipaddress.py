# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2022 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""IPv4/Ipv6 object to bytes and bytes to IPv4/Ipv6 object transform."""

from ipaddress import IPv4Address
from typing import Any, Callable, Union

from ._typing import ByteOrderHint
from .object import ObjectX

PackType = Callable[[Any], bytes]
UnpackType = Callable[[bytes], Any]


class IPv4AddressX(ObjectX):

    """IPv4Address to bytes and bytes to IPv4Address transform."""

    def __init__(
        self,
        byteorder: ByteOrderHint = "big",
        name: str = "IPv4Address",
    ) -> None:
        nbytes = 4

        def pack(ipv4address: Union[int, str, IPv4Address]) -> bytes:
            """Pack IPv4 address as formatted bytes.

            :raises: ``PackError`` if type error, value error, etc.

            """
            return int(IPv4Address(ipv4address)).to_bytes(nbytes, byteorder)

        def unpack(buffer: bytes) -> IPv4Address:
            """Unpack IPv4Address from formatted bytes.

            :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

            """
            return IPv4Address(int.from_bytes(buffer, byteorder))

        super().__init__(pack, unpack, nbytes, name, hint="IPv4Address")

        self.__byteorder__: ByteOrderHint = byteorder

    @property
    def byteorder(self) -> ByteOrderHint:
        """Byte order ("little" or "big")."""
        return self.__byteorder__
