import os
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class WhoisException(Exception):
    # make all other exeptions based on a generic exception
    pass


class UnknownTld(WhoisException):
    pass


class FailedParsingWhoisOutput(WhoisException):
    pass


class WhoisQuotaExceeded(WhoisException):
    pass


class UnknownDateFormat(WhoisException):
    pass


class WhoisCommandFailed(WhoisException):
    pass


class WhoisPrivateRegistry(WhoisException):
    # also known as restricted : see comments at the bottom in tld_regexpr.py
    # almost no info is returned or there is no cli whois server at all:
    # see: https://www.iana.org/domains/root/db/<tld>.html
    pass


class WhoisCommandTimeout(WhoisException):
    pass
