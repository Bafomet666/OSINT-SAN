"""Common utilities for the Censys Python SDK."""

import datetime

from .types import Datetime


def format_rfc3339(time: Datetime) -> str:
    """Formats a datetime object into an RFC3339 string.

    Args:
        time (Datetime): Datetime object to format.

    Returns:
        str: RFC3339 formatted string.
    """
    if isinstance(time, (datetime.date, datetime.datetime)):
        time = time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return time


def format_iso8601(time: Datetime) -> str:
    """Formats a datetime object into an ISO8601 string.

    Args:
        time (Datetime): Datetime object to format.

    Returns:
        str: ISO8601 formatted string.
    """
    if isinstance(time, (datetime.date, datetime.datetime)):
        return time.strftime("%Y-%m-%d")
    return time
