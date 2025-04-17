#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.utils provide a handy way for internal used by xmind,
    and excepted that function defined here will be useful to others.

"""
import os
import time
import random
import tempfile
import zipfile
from hashlib import md5
from functools import wraps
from xml.dom.minidom import parse, parseString


# ********** Misc **********
temp_dir = tempfile.mkdtemp


def generate_id():
    """
    Generate unique 26-digit random string
    """
    # FIXME: Why not use something like the builtin uuid.uuid1() method?
    # md5 current time get 32-digit random string
    timestamp = md5(str(get_current_time()).encode('utf-8')).hexdigest()
    lotter = md5(str(random.random()).encode('utf-8')).hexdigest()
    _id = timestamp[19:] + lotter[:13]
    return _id


# ********** Zip **********
def extract(path):
    return zipfile.ZipFile(path, "r")


def compress(path):
    return zipfile.ZipFile(path, "w")


# ********** Path **********
join_path = os.path.join
split_ext = os.path.splitext


def get_abs_path(path):
    """
        Return the absolute path of a file

        If path contains a start point (eg Unix '/') then use the specified start point
        instead of the current working directory. The starting point of the file path is
        allowed to begin with a tilde "~", which will be replaced with the user's home directory.
    """

    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()

    fp = os.path.abspath(os.path.expanduser(fp))

    return join_path(fp, fn)


# ********** Time **********
def get_current_time():
    """
    Get the current time in milliseconds
    """
    return int(round(time.time() * 1000))


def readable_time(timestamp):
    """
    Convert timestamp to human-readable time format

    Timestamp in milliseconds, convert to seconds
    Cause Python handle time in seconds
    """
    timestampe_in_seconds = float(timestamp) / 1000
    return time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(timestampe_in_seconds))


# ********** DOM **********

parse_dom = parse
parse_dom_string = parseString


# def create_document():
#     return dom.Document()
#
#
# def create_element(tagName, namespaceURI=None, prefix=None, localName=None):
#     return dom.Element(tagName, namespaceURI, prefix, localName)
#
#
# def load_XML(stream):
#     """
#         Create new Document while occure load XML error
#     """
#     try:
#         return dom.parse(stream)
#     except:
#         return create_document()


# ********** Decorator **********

def prevent(func):
    """
        Decorate func with this to prevent raising an Exception when
        an error is encountered
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException:
            return

    return wrapper


def check(attr):
    def decorator(method):
        """
            Decorate method with this to check whether the object
            has an attribute with the given name.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, attr):
                return method(self, *args, **kwargs)

            return None
        return wrapper
    return decorator
