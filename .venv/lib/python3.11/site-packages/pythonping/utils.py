"""Module containing service classes and functions"""

import string
import random


def random_text(size):
    """Returns a random text of the specified size

    :param size: Size of the random string, must be greater than 0
    :type size int
    :return: Random string
    :rtype: str"""
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
