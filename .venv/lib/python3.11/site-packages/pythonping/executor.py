"""Module that actually performs the ping, sending and receiving packets"""

import os
import sys
import time
from . import icmp
from . import network

# Python 3.5 compatibility
if sys.version_info[1] == 5:
    from enum import IntEnum, Enum

    class AutoNumber(Enum):
        def __new__(cls):
            value = len(cls.__members__) + 1
            obj = object.__new__(cls)
            obj._value = value
            return obj

    class SuccessOn(AutoNumber):
        One = ()
        Most = ()
        All = ()
else:
    from enum import IntEnum, auto

    class SuccessOn(IntEnum):
        One = auto()
        Most = auto()
        All = auto()


class Message:
    """Represents an ICMP message with destination socket"""
    def __init__(self, target, packet, source):
        """Creates a message that may be sent, or used to represent a response

        :param target: Target IP or hostname of the message
        :type target: str
        :param packet: ICMP packet composing the message
        :type packet: icmp.ICMP
        :param source: Source IP or hostname of the message
        :type source: str"""
        self.target = target
        self.packet = packet
        self.source = source

    def send(self, source_socket):
        """Places the message on a socket

        :param source_socket: The socket to place the message on
        :type source_socket: network.Socket"""
        source_socket.send(self.packet.packet)

    def __repr__(self):
        return repr(self.packet)


def represent_seconds_in_ms(seconds):
    """Converts seconds into human-readable milliseconds with 2 digits decimal precision

    :param seconds: Seconds to convert
    :type seconds: Union[int, float]
    :return: The same time expressed in milliseconds, with 2 digits of decimal precision
    :rtype: float"""
    return round(seconds * 1000, 2)


class Response:
    """Represents a response to an ICMP message, with metadata like timing"""
    def __init__(self, message, time_elapsed, source_request=None, repr_format=None):
        """Creates a representation of ICMP message received in response

        :param message: The message received
        :type message: Union[None, Message]
        :param time_elapsed: Time elapsed since the original request was sent, in seconds
        :type time_elapsed: float
        :param source_request: ICMP packet represeting the request that originated this response
        :type source_request: ICMP
        :param repr_format: How to __repr__ the response. Allowed: legacy, None
        :type repr_format: str"""
        self.message = message
        self.time_elapsed = time_elapsed
        self.source_request = source_request
        self.repr_format = repr_format

    @property
    def success(self):
        return self.error_message is None

    @property
    def error_message(self):
        if self.message is None:
            return 'No response'
        if self.message.packet.message_type == 0 and self.message.packet.message_code == 0:
            # Echo Reply, response OK - no error
            return None
        if self.message.packet.message_type == 3:
            # Destination unreachable, returning more details based on message code
            unreachable_messages = [
                'Network Unreachable',
                'Host Unreachable',
                'Protocol Unreachable',
                'Port Unreachable',
                'Fragmentation Required',
                'Source Route Failed',
                'Network Unknown',
                'Host Unknown',
                'Source Host Isolated',
                'Communication with Destination Network is Administratively Prohibited',
                'Communication with Destination Host is Administratively Prohibited',
                'Network Unreachable for ToS',
                'Host Unreachable for ToS',
                'Communication Administratively Prohibited',
                'Host Precedence Violation',
                'Precedence Cutoff in Effect'
            ]
            try:
                return unreachable_messages[self.message.packet.message_code]
            except IndexError:
                # Should never generate IndexError, this serves as additional protection
                return 'Unreachable'
        # Error was not identified
        return 'Network Error'

    @property
    def time_elapsed_ms(self):
        return represent_seconds_in_ms(self.time_elapsed)

    def legacy_repr(self):
        if self.message is None:
            return 'Request timed out'
        if self.success:
            return 'Reply from {0}, {1} bytes in {2}ms'.format(self.message.source,
                                                               len(self.message.packet.raw),
                                                               self.time_elapsed_ms)
        # Not successful, but with some code (e.g. destination unreachable)
        return '{0} from {1} in {2}ms'.format(self.error_message, self.message.source, self.time_elapsed_ms)

    def __repr__(self):
        if self.repr_format == 'legacy':
            return self.legacy_repr()
        if self.message is None:
            return 'Timed out'
        if self.success:
            return 'status=OK\tfrom={0}\tms={1}\t\tbytes\tsnt={2}\trcv={3}'.format(
                self.message.source,
                self.time_elapsed_ms,
                len(self.source_request.raw)+20,
                len(self.message.packet.raw)
            )
        return 'status=ERR\tfrom={1}\terror="{0}"'.format(self.message.source, self.error_message)

class ResponseList:
    """Represents a series of ICMP responses"""
    def __init__(self, initial_set=[], verbose=False, output=sys.stdout):
        """Creates a ResponseList with initial data if available

        :param initial_set: Already existing responses
        :type initial_set: list
        :param verbose: Flag to enable verbose mode, defaults to False
        :type verbose: bool
        :param output: File where to write verbose output, defaults to stdout
        :type output: file"""
        self._responses = []
        self.clear()
        self.verbose = verbose
        self.output = output
        self.rtt_avg = 0
        self.rtt_min = 0
        self.rtt_max = 0
        self.stats_packets_sent = 0
        self.stats_packets_returned = 0
        for response in initial_set:
            self.append(response)

    def success(self, option=SuccessOn.One):
        """Check success state of the request.

        :param option: Sets a threshold for success sign. ( 1 - SuccessOn.One, 2 - SuccessOn.Most, 3 - SuccessOn.All )
        :type option: int
        :return: Whether this set of responses is successful
        :rtype: bool
        """
        result = False
        success_list = [resp.success for resp in self._responses]
        if option == SuccessOn.One:
            result = True in success_list
        elif option == SuccessOn.Most:
            result = success_list.count(True) / len(success_list) > 0.5
        elif option == SuccessOn.All:
            result = False not in success_list
        return result

    @property
    def packet_loss(self):
        return self.packets_lost

    @property
    def rtt_min_ms(self):
        return represent_seconds_in_ms(self.rtt_min)

    @property
    def rtt_max_ms(self):
        return represent_seconds_in_ms(self.rtt_max)

    @property
    def rtt_avg_ms(self):
        return represent_seconds_in_ms(self.rtt_avg)

    def clear(self):
        self._responses = []
        self.stats_packets_sent = 0
        self.stats_packets_returned = 0


    def append(self, value):
        self._responses.append(value)
        self.stats_packets_sent += 1
        if len(self) == 1:
            self.rtt_avg = value.time_elapsed
            self.rtt_max = value.time_elapsed
            self.rtt_min = value.time_elapsed
        else:
            # Calculate the total of time, add the new value and divide for the new number
            self.rtt_avg = ((self.rtt_avg * (len(self)-1)) + value.time_elapsed) / len(self)
            if value.time_elapsed > self.rtt_max:
                self.rtt_max = value.time_elapsed
            if value.time_elapsed < self.rtt_min:
                self.rtt_min = value.time_elapsed
        if value.success:
            self.stats_packets_returned += 1

        if self.verbose:
            print(value, file=self.output)

    @property
    def stats_packets_lost(self):
        return self.stats_packets_sent - self.stats_packets_returned

    @property
    def stats_success_ratio(self):
        return self.stats_packets_returned / self.stats_packets_sent

    @property
    def stats_lost_ratio(self):
        return 1 - self.stats_success_ratio

    @property
    def packets_lost(self):
        return self.stats_lost_ratio

    def __len__(self):
        return len(self._responses)

    def __repr__(self):
        ret = ''
        for response in self._responses:
            ret += '{0}\r\n'.format(response)
        ret += '\r\n'
        ret += 'Round Trip Times min/avg/max is {0}/{1}/{2} ms'.format(self.rtt_min_ms, self.rtt_avg_ms, self.rtt_max_ms)
        return ret

    def __iter__(self):
        for response in self._responses:
            yield response


class Communicator:
    """Instance actually communicating over the network, sending messages and handling responses"""
    def __init__(self, target, payload_provider, timeout, interval, socket_options=(), seed_id=None,
                 verbose=False, output=sys.stdout, source=None, repr_format=None):
        """Creates an instance that can handle communication with the target device

        :param target: IP or hostname of the remote device
        :type target: str
        :param payload_provider: An iterable list of payloads to send
        :type payload_provider: PayloadProvider
        :param timeout: Timeout that will apply to all ping messages, in seconds
        :type timeout: Union[int, float]
        :param interval: Interval to wait between pings, in seconds
        :type interval: int
        :param socket_options: Options to specify for the network.Socket
        :type socket_options: tuple
        :param seed_id: The first ICMP packet ID to use
        :type seed_id: Union[None, int]
        :param verbose: Flag to enable verbose mode, defaults to False
        :type verbose: bool
        :param output: File where to write verbose output, defaults to stdout
        :type output: file
        :param repr_format: How to __repr__ the response. Allowed: legacy, None
        :type repr_format: str"""
        self.socket = network.Socket(target, 'icmp', options=socket_options, source=source)
        self.provider = payload_provider
        self.timeout = timeout
        self.interval = interval
        self.responses = ResponseList(verbose=verbose, output=output)
        self.seed_id = seed_id
        self.repr_format = repr_format
        # note that to make Communicator instances thread safe, the seed ID must be unique per thread
        if self.seed_id is None:
            self.seed_id = os.getpid() & 0xFFFF

    def __del__(self):
        pass

    def send_ping(self, packet_id, sequence_number, payload):
        """Sends one ICMP Echo Request on the socket

        :param packet_id: The ID to use for the packet
        :type packet_id: int
        :param sequence_number: The sequence number to use for the packet
        :type sequence_number: int
        :param payload: The payload of the ICMP message
        :type payload: Union[str, bytes]
        :rtype: ICMP"""
        i = icmp.ICMP(
            icmp.Types.EchoRequest,
            payload=payload,
            identifier=packet_id, sequence_number=sequence_number)
        self.socket.send(i.packet)
        return i

    def listen_for(self, packet_id, timeout, payload_pattern=None, source_request=None):
        """Listens for a packet of a given id for a given timeout

        :param packet_id: The ID of the packet to listen for, the same for request and response
        :type packet_id: int
        :param timeout: How long to listen for the specified packet, in seconds
        :type timeout: float
        :param payload_pattern: Payload reply pattern to match to request, if set to None, match by ID only
        :type payload_pattern: Union[None, bytes]
        :return: The response to the request with the specified packet_id
        :rtype: Response"""
        time_left = timeout
        response = icmp.ICMP()
        while time_left > 0:
            # Keep listening until a packet arrives
            raw_packet, source_socket, time_left = self.socket.receive(time_left)
            # If we actually received something
            if raw_packet != b'':
                response.unpack(raw_packet)

                # Ensure we have not unpacked the packet we sent (RHEL will also listen to outgoing packets)
                if response.id == packet_id and response.message_type != icmp.Types.EchoRequest.type_id:
                    if payload_pattern is None:
                        # To allow Windows-like behaviour (no payload inspection, but only match packet identifiers),
                        # simply allow for it to be an always true in the legacy usage case
                        payload_matched = True
                    else:
                        payload_matched = (payload_pattern == response.payload)

                    if payload_matched:
                        return Response(Message('', response, source_socket[0]), timeout - time_left, source_request, repr_format=self.repr_format)
        return Response(None, timeout, source_request, repr_format=self.repr_format)

    @staticmethod
    def increase_seq(sequence_number):
        """Increases an ICMP sequence number and reset if it gets bigger than 2 bytes

        :param sequence_number: The sequence number to increase
        :type sequence_number: int
        :return: The increased sequence number of 1, in case an increase was not possible
        :rtype: int"""
        sequence_number += 1
        if sequence_number > 0xFFFF:
            sequence_number = 1
        return sequence_number

    def run(self, match_payloads=False):
        """Performs all the pings and stores the responses

        :param match_payloads: optional to set to True to make sure requests and replies have equivalent payloads
        :type match_payloads: bool"""
        self.responses.clear()
        identifier = self.seed_id
        seq = 1
        for payload in self.provider:
            icmp_out = self.send_ping(identifier, seq, payload)
            if not match_payloads:
                self.responses.append(self.listen_for(identifier, self.timeout, None, icmp_out))
            else:
                self.responses.append(self.listen_for(identifier, self.timeout, icmp_out.payload, icmp_out))

            seq = self.increase_seq(seq)

            if self.interval:
                time.sleep(self.interval)
