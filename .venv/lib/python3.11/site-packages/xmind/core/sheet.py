#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xmind.core.sheet command XMind sheets manipulation
"""
from xmind import utils
from . import const
from .mixin import WorkbookMixinElement
from .topic import TopicElement
from .title import TitleElement
from .relationship import RelationshipElement, RelationshipsElement


class SheetElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_SHEET

    def __init__(self, node=None, ownerWorkbook=None):
        super(SheetElement, self).__init__(node, ownerWorkbook)

        self.addIdAttribute(const.ATTR_ID)
        self.setAttribute(const.ATTR_TIMESTAMP, int(utils.get_current_time()))
        self._root_topic = self._get_root_topic()

    def _get_root_topic(self):
        # This method initialize root topic, if not root topic DOM implementation, then create one
        topics = self.getChildNodesByTagName(const.TAG_TOPIC)
        owner_workbook = self.getOwnerWorkbook()
        if len(topics) >= 1:
            root_topic = topics[0]
            root_topic = TopicElement(root_topic, owner_workbook)
        else:
            root_topic = TopicElement(ownerWorkbook=owner_workbook)
            self.appendChild(root_topic)

        return root_topic

    def _getRelationships(self):
        return self.getFirstChildNodeByTagName(const.TAG_RELATIONSHIPS)

    def _addRelationship(self, rel):
        """
        Add relationship to sheet
        """
        _rels = self._getRelationships()
        owner_workbook = self.getOwnerWorkbook()

        rels = RelationshipsElement(_rels, owner_workbook)

        if not _rels:
            self.appendChild(rels)

        rels.appendChild(rel)

    def createRelationship(self, end1, end2, title=None):
        """
        Create a relationship between two different topics and return the
        created rel. Please notice that the created rel will be added to
        sheet.

        :param end1:    topic or topic ID
        :param end2:    topic or topic ID
        :param title:   relationship title, default by None

        :return: a `RelationshipElement` instance

        """
        rel = RelationshipElement(ownerWorkbook=self.getOwnerWorkbook())
        rel.setEnd1ID(end1 if isinstance(end1, str) else end1.getID())
        rel.setEnd2ID(end2 if isinstance(end2, str) else end2.getID())

        if title is not None:
            rel.setTitle(title)

        self._addRelationship(rel)

        return rel

    def getRelationships(self):
        """
        Get list of relationship from current sheet
        """
        _rels = self._getRelationships()
        if not _rels:
            return []
        owner_workbook = self.getOwnerWorkbook()
        return RelationshipsElement(_rels, owner_workbook).getRelationships()

    def removeRelationship(self, rel):
        """
        Remove a relationship between two different topics
        """
        rels = self._getRelationships()

        if not rels:
            return

        rel = rel.getImplementation()
        rels.removeChild(rel)
        if not rels.hasChildNodes():
            self.getImplementation().removeChild(rels)

        self.updateModifiedTime()

    def getRootTopic(self):
        return self._root_topic

    def _get_title(self):
        return self.getFirstChildNodeByTagName(const.TAG_TITLE)

    # FIXME: convert to getter/setter
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

    def getParent(self):
        workbook = self.getOwnerWorkbook()
        if workbook:
            parent = self.getParentNode()

            if parent == workbook.getWorkbookElement().getImplementation():
                return workbook

    def updateModifiedTime(self):
        super(SheetElement, self).updateModifiedTime()

        workbook = self.getParent()
        if workbook:
            workbook.updateModifiedTime()

    def getData(self):
        """
        Get sheet's main content in the form of a dictionary.
        """
        root_topic = self.getRootTopic()
        data = {
            'id': self.getAttribute(const.ATTR_ID),
            'title': self.getTitle(),
            'topic': root_topic.getData()
        }
        return data
