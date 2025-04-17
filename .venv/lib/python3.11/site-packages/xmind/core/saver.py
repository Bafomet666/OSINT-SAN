#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.saver
"""
import codecs
import os

from . import const
from .. import utils


class WorkbookSaver(object):
    def __init__(self, workbook):
        """ Save `WorkbookDocument` as XMind file.

        :param workbook: `WorkbookDocument` object
        """
        self._workbook = workbook
        self._temp_dir = utils.temp_dir()

    def _get_content_xml(self):
        content_path = utils.join_path(self._temp_dir, const.CONTENT_XML)
        # encoding specifies the encoding which is to be used for the file.
        with codecs.open(content_path, "w", encoding="utf-8") as f:
            self._workbook.output(f)

        return content_path

    def _get_comments_xml(self):
        comments_path = utils.join_path(self._temp_dir, const.COMMENTS_XML)
        with codecs.open(comments_path, "w", encoding="utf-8") as f:
            self._workbook.commentsbook.output(f)

        return comments_path

    def _get_styles_xml(self):
        styles_path = utils.join_path(self._temp_dir, const.STYLES_XML)
        with codecs.open(styles_path, "w", encoding="utf-8") as f:
            self._workbook.stylesbook.output(f)

        return styles_path

    def _get_reference(self, except_revisions=False):
        """
        Get all references in xmind zip file.

        :param except_revisions: whether or not to save `Revisions` content in order ot save space.
        """
        original_xmind_file = self._workbook.get_path()
        reference_dir = utils.temp_dir()

        filename, suffix = utils.split_ext(original_xmind_file)
        if suffix != const.XMIND_EXT:
            raise Exception('XMind filename require a "%s" extension' % const.XMIND_EXT)

        original_zip = utils.extract(original_xmind_file)
        try:
            with original_zip as input_stream:
                for name in input_stream.namelist():
                    if name in [const.CONTENT_XML, const.STYLES_XML, const.COMMENTS_XML]:
                        continue
                    if const.REVISIONS_DIR in name and except_revisions:
                        continue
                    target_file = utils.get_abs_path(utils.join_path(reference_dir, name))
                    if not os.path.exists(os.path.dirname(target_file)):
                        os.makedirs(os.path.dirname(target_file))
                    with open(target_file, 'xb') as f:
                        f.write(original_zip.read(name))
        except BaseException:
            pass

        return reference_dir

    def save(self, path=None, only_content=False, except_attachments=False, except_revisions=False):
        """
        Save the workbook to the given path. If the path is not given,
        then will save to the path set in workbook.
        :param path: save to the target path.
        :param except_revisions: whether or not to save `Revisions` content to save space.
        :param except_attachments: only save content.xml、comments.xml、sytles.xml.
        :param only_content: only save content.xml
        """
        original_path = self._workbook.get_path()
        new_path = path or original_path

        new_path = utils.get_abs_path(new_path)
        new_filename, new_suffix = utils.split_ext(new_path)
        if new_suffix != const.XMIND_EXT:
            raise Exception('XMind filename require a "%s" extension' % const.XMIND_EXT)

        content = self._get_content_xml()
        if not only_content:
            styles = self._get_styles_xml()
            comments = self._get_comments_xml()
            if not except_attachments and os.path.exists(original_path):
                is_have_attachments = True
                reference_dir = self._get_reference(except_revisions)
            else:
                is_have_attachments = False

        f = utils.compress(new_path)
        f.write(content, const.CONTENT_XML)
        if not only_content:
            f.write(styles, const.STYLES_XML)
            f.write(comments, const.COMMENTS_XML)
            if not except_attachments and is_have_attachments:
                length = reference_dir.__len__()  # the length of the file string
                for dirpath, dirnames, filenames in os.walk(reference_dir):
                    for filename in filenames:
                        f.write(utils.join_path(dirpath, filename),
                                utils.join_path(dirpath[length + 1:] + os.sep, filename))
        f.close()

    # def save(self, path=None):
    #     """
    #     Save the workbook to the given path. If the path is not given, then
    #     will save to the path set in workbook.
    #     """
    #     path = path or self._workbook.get_path()
    #
    #     if not path:
    #         raise Exception("Please specify a filename for the XMind file")
    #
    #     path = utils.get_abs_path(path)
    #
    #     file_name, ext = utils.split_ext(path)
    #
    #     if ext != const.XMIND_EXT:
    #         raise Exception("XMind filename require a '%s' extension" % const.XMIND_EXT)
    #
    #     content_xml = self._get_content_xml()
    #     comments_xml = self._get_comments_xml()
    #     styles_xml = self._get_styles_xml()
    #
    #     f = utils.compress(path)
    #     f.write(content_xml, const.CONTENT_XML)
    #     f.write(comments_xml, const.COMMENTS_XML)
    #     f.write(styles_xml, const.STYLES_XML)

    # def save_as(self, path=None):
    #     """
    #     After update a xmind file, save it to the given path with all references in the xmind file except
    #     Revisions content for saving space. If the path is not given, then will save to the path set in workbook.
    #     """
    #     original_path = self._workbook.get_path()
    #     new_path = path or original_path
    #     if not new_path:
    #         raise Exception('Please specify a filename for the XMind file')
    #
    #     original_path = utils.get_abs_path(original_path)
    #     original_filename, original_suffix = utils.split_ext(original_path)
    #     if original_suffix != const.XMIND_EXT:
    #         raise Exception('XMind filename require a "%s" extension' % const.XMIND_EXT)
    #
    #     new_path = utils.get_abs_path(new_path)
    #     new_filename, new_suffix = utils.split_ext(new_path)
    #     if new_suffix != const.XMIND_EXT:
    #         raise Exception('XMind filename require a "%s" extension' % const.XMIND_EXT)
    #
    #     content = self._get_content_xml()
    #     styles = self._get_styles_xml()
    #     comments = self._get_comments_xml()
    #     reference_dir = self._get_reference(original_path)
    #
    #     f = utils.compress(new_path)
    #     f.write(content, const.CONTENT_XML)
    #     f.write(styles, const.STYLES_XML)
    #     f.write(comments, const.COMMENTS_XML)
    #     length = reference_dir.__len__()  # the length of the file string
    #     for dirpath, dirnames, filenames in os.walk(reference_dir):
    #         for filename in filenames:
    #             f.write(utils.join_path(dirpath, filename), utils.join_path(dirpath[length+1:]+os.sep, filename))
    #     f.close()
