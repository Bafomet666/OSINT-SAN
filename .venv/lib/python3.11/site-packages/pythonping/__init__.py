import sys
from random import randint
from . import network, executor, payload_provider
from .utils import random_text


# this needs to be available across all thread usages and will hold ints
SEED_IDs = []


def ping(target,
         timeout=2,
         count=4,
         size=1,
         interval=0,
         payload=None,
         sweep_start=None,
         sweep_end=None,
         df=False,
         verbose=False,
         out=sys.stdout,
         match=False,
         source=None,
         out_format='legacy'):
    """Pings a remote host and handles the responses

    :param target: The remote hostname or IP address to ping
    :type target: str
    :param timeout: Time in seconds before considering each non-arrived reply permanently lost.
    :type timeout: Union[int, float]
    :param count: How many times to attempt the ping
    :type count: int
    :param size: Size of the entire packet to send
    :type size: int
    :param interval: Interval to wait between pings
    :type interval: int
    :param payload: Payload content, leave None if size is set to use random text
    :type payload: Union[str, bytes]
    :param sweep_start: If size is not set, initial size in a sweep of sizes
    :type sweep_start: int
    :param sweep_end: If size is not set, final size in a sweep of sizes
    :type sweep_end: int
    :param df: Don't Fragment flag value for IP Header
    :type df: bool
    :param verbose: Print output while performing operations
    :type verbose: bool
    :param out: Stream to which redirect the verbose output
    :type out: stream
    :param match: Do payload matching between request and reply (default behaviour follows that of Windows which is
    by packet identifier only, Linux behaviour counts a non equivalent payload in reply as fail, such as when pinging
    8.8.8.8 with 1000 bytes and reply is truncated to only the first 74 of request payload with packet identifiers
    the same in request and reply)
    :type match: bool
    :param repr_format: How to __repr__ the response. Allowed: legacy, None
    :type repr_format: str
    :return: List with the result of each ping
    :rtype: executor.ResponseList"""
    provider = payload_provider.Repeat(b'', 0)
    if sweep_start and sweep_end and sweep_end >= sweep_start:
        if not payload:
            payload = random_text(sweep_start)
        provider = payload_provider.Sweep(payload, sweep_start, sweep_end)
    elif size and size > 0:
        if not payload:
            payload = random_text(size)
        provider = payload_provider.Repeat(payload, count)
    options = ()
    if df:
        options = network.Socket.DONT_FRAGMENT

    # Fix to allow for pythonping multithreaded usage;
    # no need to protect this loop as no one will ever surpass 0xFFFF amount of threads
    while True:
        # seed_id needs to be less than or equal to 65535 (as original code was seed_id = getpid() & 0xFFFF)
        seed_id = randint(0x1, 0xFFFF)
        if seed_id not in SEED_IDs:
            SEED_IDs.append(seed_id)
            break


    comm = executor.Communicator(target, provider, timeout, interval, socket_options=options, verbose=verbose, output=out,
                                 seed_id=seed_id, source=source, repr_format=out_format)

    comm.run(match_payloads=match)

    SEED_IDs.remove(seed_id)

    return comm.responses
