#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.topic
"""
from . import const
from .mixin import WorkbookMixinElement
from .title import TitleElement
from .position import PositionElement
from .notes import NotesElement, PlainNotes
from .labels import LabelsElement, LabelElement
from .markerref import MarkerRefElement
from .markerref import MarkerRefsElement
from .markerref import MarkerId
from .. import utils


def split_hyperlink(hyperlink):
    colon = hyperlink.find(":")
    if colon < 0:
        protocol = None
    else:
        protocol = hyperlink[:colon]

    hyperlink = hyperlink[colon + 1:]
    while hyperlink.startswith("/"):
        hyperlink = hyperlink[1:]

    return protocol, hyperlink


class TopicElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_TOPIC

    def __init__(self, node=None, ownerWorkbook=None):
        super(TopicElement, self).__init__(node, ownerWorkbook)

        self.addIdAttribute(const.ATTR_ID)
        self.setAttribute(const.ATTR_TIMESTAMP, int(utils.get_current_time()))

    def _get_title(self):
        return self.getFirstChildNodeByTagName(const.TAG_TITLE)

    def _get_markerrefs(self):
        return self.getFirstChildNodeByTagName(const.TAG_MARKERREFS)

    def _get_labels(self):
        return self.getFirstChildNodeByTagName(const.TAG_LABELS)

    def _get_notes(self):
        return self.getFirstChildNodeByTagName(const.TAG_NOTES)

    def _get_position(self):
        return self.getFirstChildNodeByTagName(const.TAG_POSITION)

    def _get_children(self):
        return self.getFirstChildNodeByTagName(const.TAG_CHILDREN)

    def _set_hyperlink(self, hyperlink):
        self.setAttribute(const.ATTR_HREF, hyperlink)
        # self.updateModifiedTime()

    def getOwnerSheet(self):
        parent = self.getParentNode()

        while parent and parent.tagName != const.TAG_SHEET:
            parent = parent.parentNode

        if not parent:
            return

        owner_workbook = self.getOwnerWorkbook()
        if not owner_workbook:
            return

        for sheet in owner_workbook.getSheets():
            if parent is sheet.getImplementation():
                return sheet

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

        # self.updateModifiedTime()

    def getMarkers(self):
        refs = self._get_markerrefs()
        if not refs:
            return []
        tmp = MarkerRefsElement(refs, self.getOwnerWorkbook())
        markers = tmp.getChildNodesByTagName(const.TAG_MARKERREF)
        marker_list = []
        if markers:
            for i in markers:
                marker_list.append(MarkerRefElement(i, self.getOwnerWorkbook()))
        return marker_list

    def addMarker(self, markerId):
        """
        Add a marker to this topic
        :param markerId: a markerId indicating the marker to add
        :return: a MarkerRefElement instance
        """
        if not markerId:
            return None
        if isinstance(markerId, str):
            markerId = MarkerId(markerId)

        refs = self._get_markerrefs()
        if not refs:
            tmp = MarkerRefsElement(None, self.getOwnerWorkbook())
            self.appendChild(tmp)
        else:
            tmp = MarkerRefsElement(refs, self.getOwnerWorkbook())
        markers = tmp.getChildNodesByTagName(const.TAG_MARKERREF)

        # If the same family marker exists, replace it
        if markers:
            for m in markers:
                mre = MarkerRefElement(m, self.getOwnerWorkbook())
                # look for a marker of same family
                if mre.getMarkerId().getFamily() == markerId.getFamily():
                    mre.setMarkerId(markerId)
                    return mre
        # not found so let's append it
        mre = MarkerRefElement(None, self.getOwnerWorkbook())
        mre.setMarkerId(markerId)
        tmp.appendChild(mre)
        return mre

    def getLabels(self):
        """
        Get lables content. One topic can set one label right now.
        """
        _labels = self._get_labels()
        if not _labels:
            return None
        tmp = LabelsElement(_labels, self)
        # labels = tmp.getChildNodesByTagName(const.TAG_LABEL)
        # label_list = []
        # if labels:
        #     for i in labels:
        #         label_list.append(LabelElement(i, self.getOwnerWorkbook()))
        # return label_list

        label = LabelElement(node=tmp.getFirstChildNodeByTagName(const.TAG_LABEL), ownerTopic=self)
        content = label.getLabel()
        return content

    def addLabel(self, content):
        _labels = self._get_labels()
        if not _labels:
            tmp = LabelsElement(None, self)
            self.appendChild(tmp)
        else:
            tmp = LabelsElement(_labels, self)
            old = tmp.getFirstChildNodeByTagName(const.TAG_LABEL)
            if old:
                tmp.getImplementation().removeChild(old)

        label = LabelElement(content, None, self)
        tmp.appendChild(label)
        return label

    def getComments(self):
        """
        Get comments content.
        """
        topic_id = self.getAttribute(const.ATTR_ID)
        workbook = self.getOwnerWorkbook()
        content = workbook.commentsbook.getComment(topic_id)
        return content

    def addComment(self, content, author=None):
        topic_id = self.getAttribute(const.ATTR_ID)
        workbook = self.getOwnerWorkbook()
        comment = workbook.commentsbook.addComment(content=content, topic_id=topic_id, author=author)
        return comment

    def getNotes(self):
        """
        Get notes content. One topic can set one note right now.
        """
        _notes = self._get_notes()
        if not _notes:
            return None
        tmp = NotesElement(_notes, self)
        # Only support plain text notes right now
        content = tmp.getContent(const.PLAIN_FORMAT_NOTE)
        return content

    def setPlainNotes(self, content):
        """ Set plain text notes to topic

        :param content: utf8 plain text
        """
        new = PlainNotes(content, None, self)
        _notes = self._get_notes()
        if not _notes:
            tmp = NotesElement(None, self)
            self.appendChild(tmp)
        else:
            tmp = NotesElement(_notes, self)
            old = tmp.getFirstChildNodeByTagName(new.getFormat())
            if old:
                tmp.getImplementation().removeChild(old)

        tmp.appendChild(new)
        return new

    def setFolded(self):
        self.setAttribute(const.ATTR_BRANCH, const.VAL_FOLDED)

        # self.updateModifiedTime()

    def getPosition(self):
        """ Get a pair of integer located topic position.

        return (x, y) indicate x and y
        """
        position = self._get_position()
        if position is None:
            return

        position = PositionElement(position, self.getOwnerWorkbook())

        x = position.getX()
        y = position.getY()

        if x is None and y is None:
            return

        x = x or 0
        y = y or 0

        return int(x), int(y)

    def setPosition(self, x, y):
        owner_workbook = self.getOwnerWorkbook()
        position = self._get_position()

        if not position:
            position = PositionElement(ownerWorkbook=owner_workbook)
            self.appendChild(position)
        else:
            position = PositionElement(position, owner_workbook)

        position.setX(x)
        position.setY(y)
        # self.updateModifiedTime()

    def removePosition(self):
        position = self._get_position()
        if position is not None:
            self.getImplementation().removeChild(position)
        # self.updateModifiedTime()

    def getType(self):
        """
        1、root
        2、attached、detached
        """
        parent = self.getParentNode()
        if not parent:
            return

        if parent.tagName == const.TAG_SHEET:
            return const.TOPIC_ROOT

        if parent.tagName == const.TAG_TOPICS:
            topics = TopicsElement(parent, self.getOwnerWorkbook())
            return topics.getType()

    def getTopics(self, topics_type=const.TOPIC_ATTACHED):
        topic_children = self._get_children()

        if topic_children:
            topic_children = ChildrenElement(topic_children, self.getOwnerWorkbook())

            return topic_children.getTopics(topics_type)

    def getSubTopics(self, topics_type=const.TOPIC_ATTACHED):
        """ List all sub topics under current topic, If not sub topics, return empty list.
        """
        topics = self.getTopics(topics_type)
        if not topics:
            return []

        return topics.getSubTopics()

    def getSubTopicByIndex(self, index, topics_type=const.TOPIC_ATTACHED):
        """ Get sub topic by speicifeid index
        """
        sub_topics = self.getSubTopics(topics_type)
        if sub_topics is None:
            return

        if index < 0 or index >= len(sub_topics):
            return sub_topics

        return sub_topics[index]

    def addSubTopic(self, topic=None, index=-1, topics_type=const.TOPIC_ATTACHED):
        """
        Add a sub topic to the current topic and return added sub topic

        :param topic:   `TopicElement` object. If not `TopicElement` object
                        passed then created new one automatically.
        :param index:   if index not given then passed topic will append to
                        sub topics list. Otherwise, index must be less than
                        length of sub topics list and insert passed topic
                        before given index.
        :param topics_type:   TOPIC_ATTACHED or TOPIC_DETACHED
        """
        owner_workbook = self.getOwnerWorkbook()
        topic = topic or self.__class__(None, owner_workbook)

        topic_children = self._get_children()
        if not topic_children:
            topic_children = ChildrenElement(ownerWorkbook=owner_workbook)
            self.appendChild(topic_children)
        else:
            topic_children = ChildrenElement(topic_children, owner_workbook)

        topics = topic_children.getTopics(topics_type)
        if not topics:
            topics = TopicsElement(ownerWorkbook=owner_workbook)
            topics.setAttribute(const.ATTR_TYPE, topics_type)
            topic_children.appendChild(topics)

        topic_list = []
        for i in topics.getChildNodesByTagName(const.TAG_TOPIC):
            topic_list.append(TopicElement(i, owner_workbook))

        if index < 0 or index >= len(topic_list):
            topics.appendChild(topic)
        else:
            topics.insertBefore(topic, topic_list[index])

        return topic

    def getIndex(self):
        parent = self.getParentNode()
        if parent and parent.tagName == const.TAG_TOPICS:
            index = 0
            for child in parent.childNodes:
                if self.getImplementation() == child:
                    return index
                index += 1
        return -1

    def getHyperlink(self):
        return self.getAttribute(const.ATTR_HREF)

    def setFileHyperlink(self, path):
        """ Set file as topic hyperlink

        :param path: path of specified file

        """
        protocol, content = split_hyperlink(path)
        if not protocol:
            path = const.FILE_PROTOCOL + utils.get_abs_path(path)

        self._set_hyperlink(path)

    def setTopicHyperlink(self, tid):
        """ Set topic as topic hyperlink

        :param tid: given topic's id

        """
        protocol, content = split_hyperlink(tid)
        if not protocol:
            if tid.startswith("#"):
                tid = tid[1:]

            tid = const.TOPIC_PROTOCOL + tid
        self._set_hyperlink(tid)

    def setURLHyperlink(self, url):
        """ Set URL as topic hyperlink

        :param url: HTTP URL to specified website

        """
        protocol, content = split_hyperlink(url)
        if not protocol:
            url = const.HTTP_PROTOCOL + content

        self._set_hyperlink(url)

    def getStructureClass(self):
        self.getAttribute(const.ATTR_STRUCTURE_CLASS)

    def setStructureClass(self, structure_class):
        """ Set topic's structure class attribute

        :param structure_class: such as structure-class="org.xmind.ui.map.floating"

        """
        self.setAttribute(const.ATTR_STRUCTURE_CLASS, structure_class)

    def getStyleId(self):
        """ Get topic's style id

        :return: such as <topic id="4i367dju3smik6p5tl7le3mb6d" style-id="4sfj39toumgj9tupqn113ck9kq">
        """
        return self.getAttribute(const.ATTR_STYLE_ID)

    def setStyleID(self):
        style_id = utils.generate_id()
        self.setAttribute(const.ATTR_STYLE_ID, style_id)

    def getData(self):
        """ Get topic's main content in the form of a dictionary.
            if subtopic exist, recursively get the subtopics content.
        """
        data = {
            'id': self.getAttribute(const.ATTR_ID),
            'link': self.getAttribute(const.ATTR_HREF),
            'title': self.getTitle(),
            'note': self.getNotes(),
            'label': self.getLabels(),
            'comment': self.getComments(),
            'markers': [marker.getMarkerId().name for marker in self.getMarkers() if marker],
        }

        if self.getSubTopics(topics_type=const.TOPIC_ATTACHED):
            data['topics'] = []
            for sub_topic in self.getSubTopics(topics_type=const.TOPIC_ATTACHED):
                data['topics'].append(sub_topic.getData())

        return data


class ChildrenElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_CHILDREN

    def __init__(self, node=None, ownerWorkbook=None):
        super(ChildrenElement, self).__init__(node, ownerWorkbook)

    def getTopics(self, topics_type):
        topics = self.iterChildNodesByTagName(const.TAG_TOPICS)
        for i in topics:
            t = TopicsElement(i, self.getOwnerWorkbook())
            if topics_type == t.getType():
                return t


class TopicsElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_TOPICS

    def __init__(self, node=None, ownerWorkbook=None):
        super(TopicsElement, self).__init__(node, ownerWorkbook)

    def getType(self):
        return self.getAttribute(const.ATTR_TYPE)

    def getSubTopics(self):
        """
        List all sub topics on the current topic
        """
        topics = []
        ownerWorkbook = self.getOwnerWorkbook()
        for t in self.getChildNodesByTagName(const.TAG_TOPIC):
            topics.append(TopicElement(t, ownerWorkbook))

        return topics

    def getSubTopicByIndex(self, index):
        """
        Get specified sub topic by index
        """
        sub_topics = self.getSubTopics()
        if index < 0 or index >= len(sub_topics):
            return sub_topics

        return sub_topics[index]

