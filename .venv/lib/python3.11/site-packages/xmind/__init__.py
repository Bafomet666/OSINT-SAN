#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind
"""
__version__ = "0.1.0"
from xmind.core.loader import WorkbookLoader
from xmind.core.saver import WorkbookSaver


def load(path):
    """ Load XMind workbook from given path. If file no exist on given path then created new one. """
    loader = WorkbookLoader(path)
    return loader.get_workbook()


def save(workbook, path=None, only_content=False, except_attachments=False, except_revisions=False):
    """ Save workbook to given path. If path not given, then will save to path that set to workbook. """
    saver = WorkbookSaver(workbook)
    saver.save(path=path, only_content=only_content, except_attachments=except_attachments, except_revisions=except_revisions)

