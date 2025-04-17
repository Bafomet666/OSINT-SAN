#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.position
"""
from . import const
from .mixin import WorkbookMixinElement


class PositionElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_POSITION

    def __init__(self, node=None, ownerWorkbook=None):
        super(PositionElement, self).__init__(node, ownerWorkbook)

    # FIXME: These should be converted to getter/setters

    def getX(self):
        return self.getAttribute(const.ATTR_X)

    def getY(self):
        return self.getAttribute(const.ATTR_Y)

    def setX(self, x):
        self.setAttribute(const.ATTR_X, int(x))

    def setY(self, y):
        self.setAttribute(const.ATTR_Y, int(y))
