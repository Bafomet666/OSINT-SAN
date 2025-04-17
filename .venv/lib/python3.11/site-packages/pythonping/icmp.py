import os
import struct

def checksum(data):
    """Creates the ICMP checksum as in RFC 1071

    :param data: Data to calculate the checksum ofs
    :type data: bytes
    :return: Calculated checksum
    :rtype: int

    Divides the data in 16-bits chunks, then make their 1's complement sum"""
    subtotal = 0
    for i in range(0, len(data)-1, 2):
        subtotal += ((data[i] << 8) + data[i+1])                # Sum 16 bits chunks together
    if len(data) % 2:                                           # If length is odd
        subtotal += (data[len(data)-1] << 8)                    # Sum the last byte plus one empty byte of padding
    while subtotal >> 16:                                       # Add carry on the right until fits in 16 bits
        subtotal = (subtotal & 0xFFFF) + (subtotal >> 16)
    check = ~subtotal                                           # Performs the one complement
    return ((check << 8) & 0xFF00) | ((check >> 8) & 0x00FF)    # Swap bytes


class ICMPType:
    """Represents an ICMP type, as combination of type and code

    ICMP Types should inherit from this class so that the code can identify them easily.
    This is a static class, not meant to be instantiated"""
    def __init__(self):
        raise TypeError('ICMPType may not be instantiated')


class Types(ICMPType):
    class EchoReply(ICMPType):
        type_id = 0
        ECHO_REPLY = (type_id, 0,)

    class DestinationUnreachable(ICMPType):
        type_id = 3
        NETWORK_UNREACHABLE = (type_id, 0,)
        HOST_UNREACHABLE = (type_id, 1,)
        PROTOCOL_UNREACHABLE = (type_id, 2,)
        PORT_UNREACHABLE = (type_id, 3,)
        FRAGMENTATION_REQUIRED = (type_id, 4,)
        SOURCE_ROUTE_FAILED = (type_id, 5,)
        NETWORK_UNKNOWN = (type_id, 6,)
        HOST_UNKNOWN = (type_id, 7,)
        SOURCE_HOST_ISOLATED = (type_id, 8,)
        NETWORK_ADMINISTRATIVELY_PROHIBITED = (type_id, 9,)
        HOST_ADMINISTRATIVELY_PROHIBITED = (type_id, 10,)
        NETWORK_UNREACHABLE_TOS = (type_id, 11,)
        HOST_UNREACHABLE_TOS = (type_id, 12,)
        COMMUNICATION_ADMINISTRATIVELY_PROHIBITED = (type_id, 13,)
        HOST_PRECEDENCE_VIOLATION = (type_id, 14,)
        PRECEDENCE_CUTOFF = (type_id, 15,)

    class SourceQuench(ICMPType):
        type_id = 4
        SOURCE_QUENCH = (type_id, 0,)

    class Redirect(ICMPType):
        type_id = 5
        FOR_NETWORK = (type_id, 0,)
        FOR_HOST = (type_id, 1,)
        FOR_TOS_AND_NETWORK = (type_id, 2,)
        FOR_TOS_AND_HOST = (type_id, 3,)

    class EchoRequest(ICMPType):
        type_id = 8
        ECHO_REQUEST = (type_id, 0,)

    class RouterAdvertisement(ICMPType):
        type_id = 9
        ROUTER_ADVERTISEMENT = (type_id, 0,)

    class RouterSolicitation(ICMPType):
        type_id = 10
        ROUTER_SOLICITATION = (type_id, 0)
        # Aliases
        ROUTER_DISCOVERY = ROUTER_SOLICITATION
        ROUTER_SELECTION = ROUTER_SOLICITATION

    class TimeExceeded(ICMPType):
        type_id = 11
        TTL_EXPIRED_IN_TRANSIT = (type_id, 0)
        FRAGMENT_REASSEMBLY_TIME_EXCEEDED = (type_id, 1)

    class BadIPHeader(ICMPType):
        type_id = 12
        POINTER_INDICATES_ERROR = (type_id, 0)
        MISSING_REQUIRED_OPTION = (type_id, 1)
        BAD_LENGTH = (type_id, 2)

    class Timestamp(ICMPType):
        type_id = 13
        TIMESTAMP = (type_id, 0)

    class TimestampReply(ICMPType):
        type_id = 14
        TIMESTAMP_REPLY = (type_id, 0)

    class InformationRequest(ICMPType):
        type_id = 15
        INFORMATION_REQUEST = (type_id, 0)

    class InformationReply(ICMPType):
        type_id = 16
        INFORMATION_REPLY = (type_id, 0)

    class AddressMaskRequest(ICMPType):
        type_id = 17
        ADDRESS_MASK_REQUEST = (type_id, 0)

    class AddressMaskReply(ICMPType):
        type_id = 18
        ADDRESS_MASK_REPLY = (type_id, 0)

    class Traceroute(ICMPType):
        type_id = 30
        INFORMATION_REQUEST = (type_id, 30)


class ICMP:
    LEN_TO_PAYLOAD = 41     # Ethernet, IP and ICMP header lengths combined

    def __init__(self, message_type=Types.EchoReply, payload=None, identifier=None, sequence_number=1):
        """Creates an ICMP packet

        :param message_type: Type of ICMP message to send
        :type message_type: Union[ICMPType, (int, int), int]
        :param payload: utf8 string or bytes payload
        :type payload: Union[str, bytes]
        :param identifier: ID of this ICMP packet
        :type identifier: int"""
        self.message_code = 0
        if issubclass(message_type, ICMPType):
            self.message_type = message_type.type_id
        elif isinstance(message_type, tuple):
            self.message_type = message_type[0]
            self.message_code = message_type[1]
        elif isinstance(message_type, int):
            self.message_type = message_type
        if payload is None:
            payload = bytes('1', 'utf8')
        elif isinstance(payload, str):
            payload = bytes(payload, 'utf8')
        self.payload = payload
        if identifier is None:
            identifier = os.getpid()
        self.id = identifier & 0xFFFF           # Prevent identifiers bigger than 16 bits
        self.sequence_number = sequence_number
        self.received_checksum = None
        self.raw = None

    @property
    def packet(self):
        """The raw packet with header, ready to be sent from a socket"""
        p = self._header(check=self.expected_checksum) + self.payload
        if self.raw is None:
            self.raw = p
        return p

    def _header(self, check=0):
        """The raw ICMP header

        :param check: Checksum value
        :type check: int
        :return: The packed header
        :rtype: bytes"""
        # TODO implement sequence number
        return struct.pack("BBHHH",
                           self.message_type,
                           self.message_code,
                           check,
                           self.id,
                           self.sequence_number)

    def __repr__(self):
        return ' '.join('{:02x}'.format(b) for b in self.raw)

    @property
    def is_valid(self):
        """True if the received checksum is valid, otherwise False"""
        if self.received_checksum is None:
            return True
        return self.expected_checksum == self.received_checksum

    @property
    def expected_checksum(self):
        """The checksum expected for this packet, calculated with checksum field set to 0"""
        return checksum(self._header() + self.payload)

    @property
    def header_length(self):
        """Length of the ICMP header"""
        return len(self._header())

    @staticmethod
    def generate_from_raw(raw):
        """Creates a new ICMP representation from the raw bytes

        :param raw: The raw packet including payload
        :type raw: bytes
        :return: An ICMP instance representing the packet
        :rtype: ICMP"""
        packet = ICMP()
        packet.unpack(raw)
        return packet

    def unpack(self, raw):
        """Unpacks a raw packet and stores it in this object

        :param raw: The raw packet, including payload
        :type raw: bytes"""
        self.raw = raw
        self.message_type, \
            self.message_code, \
            self.received_checksum, \
            self.id, \
            self.sequence_number = struct.unpack("BBHHH", raw[20:28])
        self.payload = raw[28:]
