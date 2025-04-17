#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xmind.core.loader
"""
from xmind.core.comments import CommentsBookDocument
from xmind.core.styles import StylesBookDocument
from . import const
from .workbook import WorkbookDocument
from .. import utils


class WorkbookLoader(object):
    def __init__(self, path):
        """ Load XMind workbook from given path

        :param path:    path to XMind file. If not an existing file, will not raise an exception.

        """
        super(WorkbookLoader, self).__init__()
        self._input_source = utils.get_abs_path(path)

        file_name, ext = utils.split_ext(self._input_source)

        if ext != const.XMIND_EXT:
            raise Exception("The XMind filename is missing the '%s' extension!" % const.XMIND_EXT)

        # Input Stream
        self._content_stream = None
        self._styles_stream = None
        self._comments_steam = None

        try:
            with utils.extract(self._input_source) as input_stream:
                for stream in input_stream.namelist():
                    if stream == const.CONTENT_XML:
                        self._content_stream = utils.parse_dom_string(input_stream.read(stream))
                    elif stream == const.STYLES_XML:
                        self._styles_stream = utils.parse_dom_string(input_stream.read(stream))
                    elif stream == const.COMMENTS_XML:
                        self._comments_steam = utils.parse_dom_string(input_stream.read(stream))

        except BaseException:
            pass

    def get_workbook(self):
        """ Parse XMind file to `WorkbookDocument` object and return
        """
        path = self._input_source
        content = self._content_stream
        styles = self._styles_stream
        comments = self._comments_steam
        stylesbook = StylesBookDocument(node=styles, path=path)
        commentsbook = CommentsBookDocument(node=comments, path=path)
        workbook = WorkbookDocument(node=content, path=path, stylesbook=stylesbook, commentsbook=commentsbook)

        return workbook

    def get_stylesbook(self):
        """ Parse Xmind styles.xml to `StylesBookDocument` object and return
        """
        content = self._styles_stream
        path = self._input_source

        stylesbook = StylesBookDocument(node=content, path=path)
        return stylesbook

    def get_commentsbook(self):
        content = self._comments_steam
        path = self._input_source

        commentsbook = CommentsBookDocument(node=content, path=path)
        return commentsbook

