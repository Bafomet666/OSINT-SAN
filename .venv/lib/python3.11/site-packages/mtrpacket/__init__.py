#
#  mtrpacket - Asynchronous network probes for Python
#  Copyright (c) 2019 Matt Kimball
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#


"""Asynchronous network probes for Python

mtrpacket is a package for sending IPv4 and IPv6 network probes ('pings')
asynchronously from Python programs.  Python's asyncio library
provides the event loop and mechanism for incorporating mtrpacket's
network probes with other concurrent operations.

mtrpacket supports a variety of probe customization options.
Time-to-live (TTL) may be explicitly used for traceroute-like
functionality.  Probes can be sent using a variety of protocols:
ICMP, UDP, TCP and SCTP.  UDP, TCP and SCTP probes may be sent
with specific source and destination ports.  Probes can be sent
with a particular packet size and payload bit-pattern.
On Linux, probes can be sent with a routing "mark".

mtrpacket works on Linux, MacOS, Windows (with Cygwin) and
various Unix systems.  Requirements are Python (>= 3.5) and
mtr (>= 0.88).  mtr is distributed with many Linux distributions --
you may have it installed already.  For other operating systems,
see https://github.com/traviscross/mtr

## Getting started

The easiest way to get started with mtrpacket is to use `async with`
to open an mtrpacket session, and then call probe on that session.
This must be done in an asyncio coroutine.  asyncio manages the event loop.

For example:

```
import asyncio
import mtrpacket

#  A simple coroutine which will start an mtrpacket session and
#  ping localhost
async def probe():
    async with mtrpacket.MtrPacket() as mtr:
        return await mtr.probe('localhost')

#  Use asyncio's event loop to start the coroutine and wait for the probe
loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(probe())
finally:
    loop.close()

#  Print the probe result
print(result)
```

Keyword arguments may be used with `mtr.probe` to further customize
the network probe.  For example:

```
#  Send a probe to the HTTPS port of example.com and limit the probe
#  to four network hops
result = await mtr.probe(
    'example.com',
    ttl=4,
    protocol='tcp',
    port=443)
```
"""


import asyncio
import os
import socket
from typing import Any, Dict, List, NamedTuple, Optional, Tuple


#
#  We resolve a hostname to an IP address in order to send a probe.
#  Because the DNS resolution can have a significant impact on
#  performance when there are hundreds of simultaneous probes
#  in-flight, we will cache IP addresses for hostnames for
#  an MtrPacket session.
#
DnsCacheType = Dict[Tuple[str, Optional[int]], Tuple[str, int]]


class MtrPacket:

    """The mtr-packet subprocess which can send network probes

    MtrPacket opens a subprocess to an external 'mtr-packet' program,
    and request that the subprocess send network probes.  Multiple
    probe requests can be simultaneously in-transit, with results
    processed asynchronously, as they arrive.
    """

    def __init__(self):
        self.process = None

        self._opened = False
        self._command_futures = {}
        self._result_task = None
        self._next_command_token = 1
        self._subprocess_name = ''
        self._dns_cache = {}

    def __repr__(self):
        rep = '<MtrPacket'
        if self.process:
            rep += ' PID {}'.format(self.process.pid)
        rep += '>'

        return rep

    async def __aenter__(self):

        """Open the subprocess when entering a 'async with' block"""

        await self.open()
        return self

    async def __aexit__(self, etype, evalue, traceback):

        """Close the subprocess when leaving a 'async with' block"""

        await self.close()

    def _raise_exception_in_command_futures(self, exception) -> None:

        """Raise an anception in all command futures

        If the dispatch tasks terminates before all command futures
        have completed, because the subprocess terminated,
        because of an unexpected exception, or because the task
        was cancelled, we need to complete all command futures
        with an exception."""

        for future in self._command_futures.values():
            #  the Future may have already been cancelled
            if not future.done():
                future.set_exception(exception)

        self._command_futures.clear()

    async def _dispatch_results(self) -> None:

        """Task which handles results printed to the stdout of mtr-packet

        Each time the result of a command is printed to stdout of the
        mtr-packet subprocess, dispatch that result to the future waiting
        on command completion.

        If the stdout of the subprocess is closed, complete all outstanding
        futures with an exception.  This is needed if the process is killed
        unexpectedly.
        """

        try:
            while not self.process.stdout.at_eof():
                line = await self.process.stdout.readline()
                self._dispatch_result_line(line.decode('ascii'))
        finally:
            exc_description = \
                'failure to communicate with subprocess "{}"'.format(
                    self._subprocess_name)
            exc_description += "  (is it installed and in the PATH?)"
            exception = ProcessError(exc_description)

            self._raise_exception_in_command_futures(exception)

    def _generate_command_token(self) -> str:

        """Return a command token usable for a new command

        Command tokens are unique 32-bit integers associated with
        command requests which allow the command result to be matched
        with the request, even with results arriving out of order.
        """

        token = str(self._next_command_token)
        if self._next_command_token < 0x7FFFFFFF:
            self._next_command_token += 1
        else:
            self._next_command_token = 1

        assert token not in self._command_futures
        return token

    def _dispatch_result_line(self, line: str) -> None:

        """Given a command result in string form, dispatch to originator

        This is called with a command string read from the stdout of
        the mtr-packet subprocess.  We will package the result arguments
        into a dictionary, and then dispatch the result and arguments
        to the future associated with the request.
        """

        atoms = line.strip().split(' ')
        if len(atoms) < 2:
            return

        token = atoms[0]
        result = atoms[1]

        arguments = {}
        argument_index = 2
        while argument_index + 1 < len(atoms):
            argument_name = atoms[argument_index]
            argument_value = atoms[argument_index + 1]
            arguments[argument_name] = argument_value

            argument_index += 2

        result_tuple = (result, arguments)
        future = self._command_futures.get(token)
        if future:
            del self._command_futures[token]

            #  if the command task is canceled, the future may be done
            if not future.done():
                future.set_result(result_tuple)

    async def _command(
            self,
            command_type: str,
            arguments: Dict[str, str]) -> Tuple[str, Dict[str, str]]:

        """Send a command with arguments to the mtr-packet subprocess

        Assign a command token to a new command request.  Construct
        a string with the command and all arguments, sending it to
        stdin of the subprocess.  Wait on a future to be completed
        when the result of the command is available.
        """

        if not self._opened:
            raise StateError('not open')

        if self._result_task.done():
            exc_description = 'subprocess "{}" exited'.format(
                self._subprocess_name)
            raise ProcessError(exc_description)

        token = self._generate_command_token()
        future = asyncio.get_event_loop().create_future()
        self._command_futures[token] = future

        command_str = token + ' ' + command_type
        for argument_name in arguments:
            argument_value = arguments[argument_name]
            command_str += ' ' + argument_name + ' ' + argument_value
        command_str += '\n'

        self.process.stdin.write(command_str.encode('ascii'))
        return await future

    async def open(self) -> 'MtrPacket':

        """Launch an mtr-packet subprocess to accept commands
        (asynchronous)

        Start a subprocess for accepting probe commands.  The 'mtr-packet'
        executable in the PATH is used by default, however,
        the MTR_PACKET environment variable can be used to specify
        an alternate subprocess executable.

        As an alternative to calling open() explicitly, an 'async with'
        block can be used with the MtrPacket object to open and close the
        subprocess.

        Raises ProcessError if the subprocess fails to execute or
        if the subprocess doesn't support sending packets.

        Raises StateError if the subprocess is already open.
        """

        if self._opened:
            raise StateError('already open')

        mtr_packet_executable = os.environ.get('MTR_PACKET')
        if not mtr_packet_executable:
            mtr_packet_executable = 'mtr-packet'

        self._subprocess_name = mtr_packet_executable
        self.process = await asyncio.create_subprocess_shell(
            mtr_packet_executable,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE)

        self._result_task = asyncio.ensure_future(self._dispatch_results())
        self._opened = True

        if not await self.check_support('send-probe'):
            await self.close()

            raise ProcessError('subprocess missing probe support')

        return self

    async def close(self) -> None:

        """Close an open mtr-packet subprocess
        (asynchronous)

        If open() was explicitly called to launch the mtr-packet
        subprocess, close() should be used to terminate the process
        and clean up resources.
        """

        self._opened = False

        if self._result_task:
            self._result_task.cancel()
            self._result_task = None

        if self.process:
            self.process.stdin.close()

            try:
                self.process.kill()
            except ProcessLookupError:
                pass

            await self.process.wait()
            self.process = None

    async def check_support(self, feature: str) -> bool:

        """Check for support of a particular feature of mtr-packet
        (asynchronous)

        check_support() can be used to check support for particular
        features in the mtr-packet subprocess.  For example, 'udp',
        'tcp' and 'sctp' can be used to check support for UDP probes,
        TCP probes, and SCTP probes.

        See 'check-support' in the mtr-packet(8) man page for more
        information.

        Raises ProcessError if the mtr-packet subprocess has unexpectedly
        terminated.

        Raises StateError if the MtrPacket session hasn't been opened.
        """

        check_args = {'feature': feature}
        (_, args) = await self._command('check-support', check_args)

        return args.get('support') == 'ok'

    async def probe(self, host: str, **args) -> 'ProbeResult':

        """Asynchronously send a network probe
        (asynchronous)

        Send a network probe to a particular hostname or IP address,
        returning a ProbeResult, which includes the status of the probe,
        the address of the host responding to the probe and the round trip
        time of the probe.

        A number of optional keyword arguments can be used with the
        probe request:


        ip_version:
            Set the IP protocol version to either IPv4 or IPv6.

        ttl:
            Set the "time to live" of the probe request.  This is used
            to limit the number of network hops the probe takes before
            the probe result is reported.

        protocol:
            Can be 'icmp', 'udp', 'tcp' or 'sctp'.  A probe of the requested
            protocol is used.

        port:
            The destination port to use for 'udp', 'tcp' or 'sctp' probes.

        local_ip:
            Set the source address of the probe to a particular
            IP address.  Useful when sending from a host with multiple
            IP local addresses.

        local_port:
            Send the probe from a particular port, when sending 'udp',
            'tcp' or 'sctp' probes.

        timeout:
            The number of seconds to wait for a response before assuming
            the probe has been lost.

        size:
            The size of the generated probe packet, in bytes.

        bit_pattern:
            A byte value used to fill the payload of the probe packet.

        tos:
            The value to use in the "type of service" field for IPv4
            packets, or the "traffic class" field of IPv6 packets.

        mark:
            The packet "mark" value to be used by the Linux routing
            subsystem.


        Raises ProcessError if the mtr-packet subprocess has unexpectedly
        terminated.

        Raises HostResolveError if the hostname can't be resolved to
        an IP address.

        Raises StateError if the MtrPacket session hasn't been opened.
        """

        pack = await _package_args(self._dns_cache, host, args)

        return _make_probe_result(*await self._command('send-probe', pack))

    def clear_dns_cache(self) -> None:

        """Clear MtrPacket's DNS cache

        For performance reasons, when repeatedly probing a particular
        host, MtrPacket will only resolve the hostname one time, and
        will use the same IP address for subsequent probes to
        the same host.

        clear_dns_cache can be used to clear that cache, forcing
        new resolution of hostnames to IP addresses for future probes.
        This can be useful for scripts which are intended to run
        for an extended period of time.  (Hours, or longer)
        """

        self._dns_cache = {}


async def _resolve_ip(
        dns_cache: DnsCacheType,
        host: str,
        target_ip_version: Optional[int]
) -> Tuple[str, int]:

    """Asynchronously resolve a hostname to an IP address

    Resolve a hostname prior to sending a network probe.  An optional
    IP version parameter can be used to require either an IPv4 or
    IPv6 address.
    """

    cache_key = (host, target_ip_version)
    if cache_key in dns_cache:
        return dns_cache[cache_key]

    try:
        addrinfo = await asyncio.get_event_loop().getaddrinfo(host, 0)
    except socket.gaierror:
        raise HostResolveError("Unable to resolve '{}'".format(host))

    for info in addrinfo:
        (family, _, _, _, addr) = info

        if family == socket.AF_INET:
            if not target_ip_version or target_ip_version == 4:
                dns_addr = (addr[0], 4)
                dns_cache[cache_key] = dns_addr
                return dns_addr

        if family == socket.AF_INET6:
            if not target_ip_version or target_ip_version == 6:
                dns_addr = (addr[0], 6)
                dns_cache[cache_key] = dns_addr
                return dns_addr

    raise HostResolveError("Unable to resolve '{}'".format(host))


async def _package_args(
        dns_cache: DnsCacheType,
        host: str,
        args: Dict[str, Any]
) -> Dict[str, str]:

    """Package the arguments from a call to MtrPacket.probe

    In preparation for sending a command to the mtr-packet subprocess,
    package the arguments from MtrPacket.probe into the format
    expected by the mtr-packet subprocess.  Resolve hostnames to
    IP addresses, prefering either IPv4 or IPv6 as specified by
    the ip_version argument.
    """

    host_ip = None
    host_ip_version = None
    target_ip_version = args.get('ip_version')
    if target_ip_version and target_ip_version not in (4, 6):
        raise ValueError('expected ip_version to be either 4 or 6')

    pack = {}

    (host_ip, host_ip_version) = await _resolve_ip(
        dns_cache, host, target_ip_version)

    if host_ip_version == 4:
        pack['ip-4'] = host_ip
    elif host_ip_version == 6:
        pack['ip-6'] = host_ip

    validargs = [
        'protocol', 'port', 'local-port', 'timeout', 'ttl', 'size',
        'bit-pattern', 'tos', 'mark'
    ]

    for argname in args:
        keyname = argname.replace('_', '-')

        if argname == 'local_ip':
            (local_ip, _) = await _resolve_ip(
                    dns_cache, args[argname], host_ip_version)

            if host_ip_version == 4:
                pack['local-ip-4'] = local_ip
            elif host_ip_version == 6:
                pack['local-ip-6'] = local_ip
        elif argname == 'ip_version':
            pass  # We've handled 'ip_version' above.
        elif keyname in validargs:
            pack[keyname] = str(args[argname])
        else:
            raise TypeError(
                "unexpected keyword argument '{}'".format(keyname))

    return pack


#
#  A named tuple describing the result of a network probe
#
#  A call to MtrPacket.probe will result in an instance of
#  ProbeResult with the following members:
#
#  success:
#      a bool which is True only if the probe arrived at the target
#      host.
#
#  result:
#      the command reply string from mtr-packet.  Common values
#      are 'reply' for a probe which arrives at the target host,
#      'ttl-expired' for a probe which has its "time to live"
#      counter reach zero before arriving at the target host,
#      and 'no-reply' for a probe which is unanswered.
#
#      See the mtr-packet(8) man page for further command reply
#      strings.
#
#  time_ms:
#      a floating point value indicating the number of milliseconds
#      the probe was in-transit, prior to receiving a result.
#      Will be None in cases other than 'reply' or 'ttl-expired'.
#
#  responder:
#      a string with the IP address of the host responding to the
#      probe.  Will be None in cases other than 'reply' or 'ttl-expired'.
#
#  mpls:
#      a list of Mpls tuples representing the MPLS label stack present in
#      a 'ttl-expired' response, when Multiprotocol Label Switching (MPLS)
#      is used to route the probe.
#
ProbeResult = NamedTuple('ProbeResult', [
    ('success', bool),
    ('result', str),
    ('time_ms', Optional[float]),
    ('responder', Optional[str]),
    ('mpls', List['Mpls'])
])


def _make_probe_result(
        command_result: str, args: Dict[str, str]) -> ProbeResult:

    """Construct a ProbeResult from the output of mtr-packet

    Given the command response strings from the mtr-packet subprocess,
    construct a ProbeResult NamedTuple, suitable for returning
    from a call to MtrPacket.probe.
    """

    success = (command_result == 'reply')
    responder = args.get('ip-4') or args.get('ip-6')

    time_us = args.get('round-trip-time')
    if time_us:
        time_ms = float(time_us) / 1000.0  # type: Optional[float]
    else:
        time_ms = None

    #  The MPLS values are a sequence of comma separated integers
    mpls = []
    mpls_arg = args.get('mpls')
    if mpls_arg:
        mpls_values = list(map(int, mpls_arg.split(',')))

        while len(mpls_values) >= 4:
            mpls.append(Mpls(
                mpls_values[0],
                mpls_values[1],
                bool(mpls_values[2]),
                mpls_values[3]))

            mpls_values = mpls_values[4:]

    return ProbeResult(success, command_result, time_ms, responder, mpls)


#
#  A named tuple describing an MPLS header.
#
#  Multiprotocol Label Switching (MPLS) routes packet using explicit
#  headers attach to the packet, rather than using the IP address
#  for routing.  When a probe's time-to-live (TTL) expires, and MPLS is
#  used at the router where the expiration occurs, the MPLS headers
#  attached to the packet may be returned with the TTL expiration
#  notification.
#
#  Mpls contains one of those headers, with:
#
#  label:
#      the numeric MPLS label.
#
#  traffic_class:
#      the traffic class (for quality of service).
#      This field was formerly known as "experimental use".
#
#  bottom_of_stack:
#      a boolean indicating whether the label terminates the stack.
#
#  ttl:
#      the time-to-live of the MPLS header
#
Mpls = NamedTuple('Mpls', [
    ('label', int),
    ('traffic_class', int),
    ('bottom_of_stack', bool),
    ('ttl', int)
])


class StateError(Exception):

    """Exception raised when attempting to use MtrPacket in an invalid state

    StateError is raised when attempting to send a command to the mtr-packet
    subprocess without first opening the MtrPacket subprocess, or when
    attempting to open a subprocess which is already open.
    """


class HostResolveError(Exception):

    """Exception raised when attempting to probe a non-resolving hostname

    If a hostname is passed to MtrPacket.probe, and that hostname fails
    to resolve to an IP address, HostResolveError is raised.
    """


class ProcessError(Exception):

    """Exception raised when the mtr-packet subprocess unexpectedly exits

    ProcessError is raised by a call to MtrPacket.probe
    or MtrPacket.check_support when the mtr-packet subprocess has
    unexpectly terminated.  It is also raised by MtrPacket.open when
    the subprocess doesn't support the mtr-packet interface.
    """
