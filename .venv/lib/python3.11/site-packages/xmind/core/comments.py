#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
xmind.core.comments implements encapsulation of the XMind comments.xml.
"""
import random

from xmind import utils
from xmind.core import Document, const, Element


class CommentsBookDocument(Document):
    """ `CommentsBookDocument` as central object correspond XMind comment file.

    such as:
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <comments version="2.0" xmlns="urn:xmind:xmap:xmlns:comments:2.0">
        <comment author="zhangchuzhao" object-id="75sr1n3r5aia1b7p15df4d77r6" time="1543655624230">
            <content>批注demo</content>
        </comment>
    </comments>
    """

    def __init__(self, node=None, path=None):
        """Construct new `CommentsBookDocument` object

        :param node: pass DOM node object and parse as `CommentsBookDocument` object.
                     if node not given then created new one.
        :param path: set workbook will to be placed.
        """
        super(CommentsBookDocument, self).__init__(node)
        self._path = path

        _commentsbook_element = self.getFirstChildNodeByTagName(const.TAG_COMMENTSBOOK)
        self._commentsbook_element = CommentsBookElement(_commentsbook_element, self)

        if not _commentsbook_element:
            self.appendChild(self._commentsbook_element)

        self.setVersion(const.VERSION)

    def getCommentsBookElement(self):
        return self._commentsbook_element

    def getComments(self):
        return self._commentsbook_element.getComments()

    def addComment(self, content, topic_id, author=None):
        return self._commentsbook_element.addComment(content, topic_id, author)

    def getComment(self, topic_id):
        mapping = self.getData()
        if topic_id in mapping.keys():
            return mapping[topic_id]
        else:
            return None

    def getData(self):
        data = {}
        for comment in self.getComments():
            object_id = comment.getObjectId()
            content = comment.getContent()
            if object_id in data.keys():
                exist_content = data[object_id]
                data[object_id] = exist_content + '\n' + content
            else:
                data[object_id] = content
        return data


class CommentsBookElement(Element):
    """`CommentsBookElement` as the one and only root element of the comments book document

    such as:
    <comments version="2.0" xmlns="urn:xmind:xmap:xmlns:comments:2.0">
        <comment author="zhangchuzhao" object-id="75sr1n3r5aia1b7p15df4d77r6" time="1543655624230">
            <content>批注demo</content>
        </comment>
    </comments>
    """
    TAG_NAME = const.TAG_COMMENTSBOOK

    def __init__(self, node=None, ownerCommentsBook=None):
        super(CommentsBookElement, self).__init__(node)
        self._owner_commentsbook = ownerCommentsBook
        self.registerOwnerCommmentsBook()
        self.setAttribute(const.NAMESPACE, const.XMLNS_COMMENTS)

    def registerOwnerCommmentsBook(self):
        if self._owner_commentsbook:
            self.setOwnerDocument(self._owner_commentsbook.getOwnerDocument())

    def getOwnerCommentsBook(self):
        return self._owner_commentsbook

    def getComments(self):
        comments = self.getChildNodesByTagName(const.TAG_COMMENT)
        owner_commentsbook = self.getOwnerCommentsBook()
        comments = [CommentElement(node=comment, ownerCommentsBook=owner_commentsbook) for comment in comments]
        return comments

    def addComment(self, content, topic_id, author=None):
        comment = CommentElement(content=content, node=None, ownerCommentsBook=self.getOwnerCommentsBook())
        comment.setObjectId(topic_id)
        comment.setAuthor(author)
        self.appendChild(comment)
        return comment


class CommentElement(Element):
    """`CommentElement` as element of the comments book document

    such as:
    <comment author="zhangchuzhao" object-id="75sr1n3r5aia1b7p15df4d77r6" time="1543655624230">
        <content>批注demo</content>
    </comment>
    """
    TAG_NAME = const.TAG_COMMENT

    def __init__(self, content=None, node=None, ownerCommentsBook=None):
        super(CommentElement, self).__init__(node)
        self._owner_commentsbook = ownerCommentsBook
        self.registerOwnerCommentsbook()

        if not self.getAttribute(const.ATTR_TIME):
            # XMind BUG: comments generated in the same second only show the first one, so add a random number here
            self.setAttribute(const.ATTR_TIME, int(utils.get_current_time()) + random.randint(1, 10))

        if content:
            self._content_element = ContentElement(content=content, ownerCommentsBook=ownerCommentsBook)
            self.appendChild(self._content_element)
        else:
            content_element = self.getFirstChildNodeByTagName(const.TAG_CONTENT)
            self._content_element = ContentElement(node=content_element, ownerCommentsBook=ownerCommentsBook)

    def registerOwnerCommentsbook(self):
        if self._owner_commentsbook:
            self.setOwnerDocument(self._owner_commentsbook.getOwnerDocument())

    def getObjectId(self):
        return self.getAttribute(const.ATTR_OBJECT_ID)

    def setObjectId(self, topipc_id):
        if topipc_id and len(topipc_id) == 26:
            self.setAttribute(const.ATTR_OBJECT_ID, topipc_id)
        else:
            raise ValueError('Invalid comment object id: %s' % topipc_id)

    def getAuthor(self):
        return self.getAttribute(const.ATTR_AUTHOR)

    def setAuthor(self, author):
        if author:
            self.setAttribute(const.ATTR_AUTHOR, author)
        else:
            self.setAttribute(const.ATTR_AUTHOR, 'admin')

    def getContent(self):
        return self._content_element.getTextContent()

    def setContent(self, content):
        self._content_element.setTextContent(content)


class ContentElement(Element):
    """`ContentElement` as sub element of the comment element
    such as:
    <comment author="zhangchuzhao" object-id="75sr1n3r5aia1b7p15df4d77r6" time="1543655624230">
        <content>批注demo</content>
    </comment>
    """
    TAG_NAME = const.TAG_CONTENT

    def __init__(self, content=None, node=None, ownerCommentsBook=None):
        super(ContentElement, self).__init__(node)
        self._owner_commentsbook = ownerCommentsBook
        if content:
            self.setTextContent(content)

    def getContent(self):
        return self.getTextContent()

    def setContent(self, content):
        self.setTextContent(content)

