#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
xmind.core.styles implements encapsulation of the XMind styles.xml.
"""
from xmind.core import Document, const, Element


class StylesBookDocument(Document):
    """ `StylesBookDocument` as central object correspond XMind stylebook.
    """

    def __init__(self, node=None, path=None):
        """Construct new `StylesBookDocument` object
        :param node: pass DOM node object and parse as `StylesBookDocument` object.
                     if node not given then created new one.
        :param path: set stylesbook will to be placed.
        """
        super(StylesBookDocument, self).__init__(node)
        self._path = path
        _stylesbook_element = self.getFirstChildNodeByTagName(const.TAG_STYLESBOOK)

        self._stylesbook_element = StylesBookElement(_stylesbook_element, self)

        if not _stylesbook_element:
            self.appendChild(self._stylesbook_element)

        self.setVersion(const.VERSION)

    def getStylesbookElement(self):
        return self._stylesbook_element

    def getStyleElements(self):
        style_element_list = []
        stylesbook_element = self.getStylesbookElement()
        styles_element = stylesbook_element.getFirstChildNodeByTagName(const.TAG_STYLES)
        if styles_element:
            for style_element in styles_element.childNodes:
                style_element_list.append(StyleElement(style_element))
        else:
            return style_element_list


class StylesBookElement(Element):
    """ `StylesBookElement` as the one and only root element of the styles book document.
    """
    TAG_NAME = const.TAG_STYLESBOOK

    def __init__(self, node=None, ownerStylesBook=None):
        super(StylesBookElement, self).__init__(node)
        self._owner_stylesbook = ownerStylesBook
        self.registerOwnerStylesBook()

        # Initialize StylesBookElement with default attribute
        namespace = (const.NAMESPACE, const.XMLNS_STYLE)
        attrs = [const.NS_FO, const.NS_SVG]
        for attr in attrs:
            self.setAttributeNS(namespace, attr)

    def registerOwnerStylesBook(self):
        if self._owner_stylesbook:
            self.setOwnerDocument(self._owner_stylesbook.getOwnerDocument())


class StyleElement(Element):
    """ `StyleElement` as element of the styles book document.

    such as:
    <style id="4sfj39toumgj9tupqn113ck9kq" type="topic">
        <topic-properties shape-class="org.xmind.topicShape.ellipse"/>
    </style>
    """
    TAG_NAME = const.TAG_STYLE

    def __init__(self, node=None, ownerStylesBook=None):
        super(StyleElement, self).__init__(node)
        self._owner_stylesbook = ownerStylesBook
        self.registerOwnerStylesBook()

    def registerOwnerStylesBook(self):
        if self._owner_stylesbook:
            self.setOwnerDocument(self._owner_stylesbook.getOwnerDocument())

    def getID(self):
        return self.getAttribute(const.ATTR_ID)

    def getTopicStylePropertyByName(self, attr_name):
        """Get topic-properties element's attribute

        :param attr_name: const.ATTR_SHAPE_CLASS or const.ATTR_LINE_CLASS
        :return: attr_value
        """
        topic_properties_element = self.getFirstChildNodeByTagName(const.TAG_TOPIC_PROPERTIES)
        if not topic_properties_element.hasAttribute(attr_name):
            return ''
        return topic_properties_element.getAttribute(attr_name)
