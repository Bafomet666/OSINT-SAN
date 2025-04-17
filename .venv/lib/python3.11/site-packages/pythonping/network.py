import socket
import select
import time


class Socket:
    DONT_FRAGMENT = (socket.SOL_IP, 10, 1)           # Option value for raw socket
    PROTO_LOOKUP = {"icmp": socket.IPPROTO_ICMP, "tcp": socket.IPPROTO_TCP, "udp": socket.IPPROTO_UDP,
                    "ip": socket.IPPROTO_IP, "raw": socket.IPPROTO_RAW}

    def __init__(self, destination, protocol, options=(), buffer_size=2048, source=None):
        """Creates a network socket to exchange messages

        :param destination: Destination IP address
        :type destination: str
        :param protocol: Name of the protocol to use
        :type protocol: str
        :param options: Options to set on the socket
        :type options: tuple
        :param source: Source IP to use - implemented in future releases
        :type source: Union[None, str]
        :param buffer_size: Size in bytes of the listening buffer for incoming packets (replies)
        :type buffer_size: int"""
        try:
            self.destination = socket.gethostbyname(destination)
        except socket.gaierror as e:
            raise RuntimeError('Cannot resolve address "' + destination + '", try verify your DNS or host file')

        self.protocol = Socket.getprotobyname(protocol)
        self.buffer_size = buffer_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, self.protocol)
        self.source = source
        if options:
            self.socket.setsockopt(*options)

    # Implementing a version of socket.getprotobyname for this library since built-in is not thread safe
    # for python 3.5, 3.6, and 3.7:
    # https://bugs.python.org/issue30482
    # This bug was causing failures as it would occasionally return a 0 (incorrect) instead of a 1 (correct)
    # for the 'icmp' string, causing a OSError for "Protocol not supported" in multi-threaded usage:
    # https://github.com/alessandromaggio/pythonping/issues/40
    @staticmethod
    def getprotobyname(name):
        try:
            return Socket.PROTO_LOOKUP[name.lower()]
        except KeyError:
            raise KeyError("'" + str(name) + "' is not in the list of supported proto types: "
                           + str(list(Socket.PROTO_LOOKUP.keys())))

    def send(self, packet):
        """Sends a raw packet on the stream

        :param packet: The raw packet to send
        :type packet: bytes"""
        if self.source:
            self.socket.bind((self.source, 0))
        self.socket.sendto(packet, (self.destination, 0))

    def receive(self, timeout=2):
        """Listen for incoming packets until timeout

        :param timeout: Time after which stop listening
        :type timeout: Union[int, float]
        :return: The packet, the remote socket, and the time left before timeout
        :rtype: (bytes, tuple, float)"""
        time_left = timeout
        while time_left > 0:
            start_select = time.perf_counter()
            data_ready = select.select([self.socket], [], [], time_left)
            elapsed_in_select = time.perf_counter() - start_select
            time_left -= elapsed_in_select
            if not data_ready[0]:
                # Timeout
                return b'', '', time_left
            packet, source = self.socket.recvfrom(self.buffer_size)
            return packet, source, time_left

    def __del__(self):
        try:
            if hasattr(self, "socket") and self.socket:
                self.socket.close()
        except AttributeError:
            raise AttributeError("Attribute error because of failed socket init. Make sure you have the root privilege."
                                 " This error may also be caused from DNS resolution problems.")
