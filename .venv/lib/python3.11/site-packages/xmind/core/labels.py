#!/usr/bin/env python
# _*_ coding:utf-8 _*_


"""
    xmind.core.labels
"""
from . import const
from .mixin import TopicMixinElement


class LabelsElement(TopicMixinElement):
    TAG_NAME = const.TAG_LABELS

    def __init__(self, node=None, ownerTopic=None):
        super(LabelsElement, self).__init__(node, ownerTopic)


class LabelElement(TopicMixinElement):
    TAG_NAME = const.TAG_LABEL

    def __init__(self, content=None, node=None, ownerTopic=None):
        super(LabelElement, self).__init__(node, ownerTopic)
        if content is not None:
            self.setTextContent(content)

    def getLabel(self):
        return self.getTextContent()

    def setLabel(self, content):
        self.setTextContent(content)
