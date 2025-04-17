#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.relationship
"""
from xmind import utils
from . import const
from .mixin import WorkbookMixinElement
from .topic import TopicElement
from .title import TitleElement


class RelationshipElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_RELATIONSHIP

    def __init__(self, node=None, ownerWorkbook=None):
        super(RelationshipElement, self).__init__(node, ownerWorkbook)

        self.addIdAttribute(const.ATTR_ID)
        self.setAttribute(const.ATTR_TIMESTAMP, int(utils.get_current_time()))

    def _get_title(self):
        return self.getFirstChildNodeByTagName(const.TAG_TITLE)

    def _find_end_point(self, id):
        owner_workbook = self.getOwnerWorkbook()
        if owner_workbook is None:
            return

        end_point = owner_workbook.getElementById(id)
        if end_point is None:
            return

        if end_point.tagName == const.TAG_TOPIC:
            return TopicElement(end_point, owner_workbook)

    # FIXME: Convert the following to getter/setter

    def getEnd1ID(self):
        return self.getAttribute(const.ATTR_END1)

    def setEnd1ID(self, id):
        self.setAttribute(const.ATTR_END1, id)
        self.updateModifiedTime()

    def getEnd2ID(self):
        return self.getAttribute(const.ATTR_END2)

    def setEnd2ID(self, id):
        self.setAttribute(const.ATTR_END2, id)
        self.updateModifiedTime()

    def getEnd1(self):
        return self._find_end_point(self.getEnd1ID())

    def getEnd2(self):
        return self._find_end_point(self.getEnd2ID())

    def getTitle(self):
        title = self._get_title()
        if title:
            title = TitleElement(title, self.getOwnerWorkbook())
            return title.getTextContent()

    def setTitle(self, text):
        _title = self._get_title()
        title = TitleElement(_title, self.getOwnerWorkbook())
        title.setTextContent(text)

        if _title is None:
            self.appendChild(title)

        self.updateModifiedTime()


class RelationshipsElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_RELATIONSHIPS

    def __init__(self, node=None, ownerWorkbook=None):
        super(RelationshipsElement, self).__init__(node, ownerWorkbook)

    def getRelationships(self):
        """
        List all relationships
        """
        relationships = []
        owner_workbook = self.getOwnerWorkbook()
        for r in self.getChildNodesByTagName(const.TAG_RELATIONSHIP):
            relationships.append(RelationshipElement(r, owner_workbook))

        return relationships
