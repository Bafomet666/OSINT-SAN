"""Module generating ICMP payloads (with no header)"""


class PayloadProvider:
    def __init__(self):
        raise NotImplementedError('Cannot create instances of PayloadProvider')

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()


class List(PayloadProvider):
    def __init__(self, payload_list):
        """Creates a provider of payloads from an existing list of payloads

        :param payload_list: An existing list of payloads
        :type payload_list: list"""
        self._payloads = payload_list
        self._counter = 0

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter < len(self._payloads):
            ret = self._payloads[self._counter]
            self._counter += 1
            return ret
        raise StopIteration


class Repeat(PayloadProvider):
    def __init__(self, pattern, count):
        """Creates a provider of many identical payloads

        :param pattern: The existing payload
        :type pattern: Union[str, bytes]
        :param count: How many payloads to generate
        :type count: int"""
        self.pattern = pattern
        self.count = count
        self._counter = 0

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter < self.count:
            self._counter += 1
            return self.pattern
        raise StopIteration


class Sweep(PayloadProvider):
    def __init__(self, pattern, start_size, end_size):
        """Creates a provider of payloads of increasing size

        :param pattern: The existing payload, may be cut or replicated to fit the size
        :type pattern: Union[str, bytes]
        :param start_size: The first payload size to start with, included
        :type start_size: int
        :param end_size: The payload size to end with, included
        :type end_size: int"""
        if start_size > end_size:
            raise ValueError('end_size must be greater or equal than start_size')
        if len(pattern) == 0:
            raise ValueError('pattern cannot be empty')
        self.pattern = pattern
        self.start_size = start_size
        self.end_size = end_size
        # Extend the length of the pattern if needed
        while not len(self.pattern) >= end_size:
            self.pattern += pattern
        self._current_size = self.start_size

    def __iter__(self):
        self._current_size = self.start_size
        return self

    def __next__(self):
        if self._current_size <= self.end_size:
            ret = self.pattern[0:self._current_size]
            self._current_size += 1
            return ret
        raise StopIteration
