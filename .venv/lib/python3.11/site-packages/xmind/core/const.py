#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.const
"""

XMIND_EXT = ".xmind"
VERSION = "2.0"
# Namespace
NAMESPACE = "xmlns"
XMLNS_CONTENT = "urn:xmind:xmap:xmlns:content:2.0"
XMLNS_COMMENTS = "urn:xmind:xmap:xmlns:comments:2.0"
XMLNS_STYLE = "urn:xmind:xmap:xmlns:style:2.0"
NS_URI = "http://www.w3.org/1999/xhtml"
NS_FO = (NS_URI, "fo", "http://www.w3.org/1999/XSL/Format")
NS_SVG = (NS_URI, "svg", "http://www.w3.org/2000/svg")
NS_XHTML = (NS_URI, "xhtml", "http://www.w3.org/1999/xhtml")
NS_XLINK = (NS_URI, "xlink", "http://www.w3.org/1999/xlink")
# Dir
ATTACHMENTS_DIR = "attachments/"
MARKERS_DIR = "markers/"
META_INF_DIR = "META-INF/"
REVISIONS_DIR = "Revisions/"
# File
CONTENT_XML = "content.xml"
COMMENTS_XML = "comments.xml"
STYLES_XML = "styles.xml"
META_XML = "meta.xml"
MANIFEST_XML = "META-INF/manifest.xml"
MARKER_SHEET_XML = "markerSheet.xml"
MARKER_SHEET = MARKERS_DIR + MARKER_SHEET_XML
REVISIONS_XML = "revisions.xml"
# Tag
TAG_WORKBOOK = "xmap-content"
TAG_TOPIC = "topic"
TAG_TOPICS = "topics"
TAG_SHEET = "sheet"
TAG_TITLE = "title"
TAG_POSITION = "position"
TAG_CHILDREN = "children"
TAG_NOTES = "notes"
TAG_LABEL = "label"
TAG_LABELS = "labels"
TAG_RELATIONSHIP = "relationship"
TAG_RELATIONSHIPS = "relationships"
TAG_MARKERREFS = "marker-refs"
TAG_MARKERREF = "marker-ref"
TAG_STYLESBOOK = "xmap-styles"
TAG_STYLES = "styles"
TAG_STYLE = "style"
TAG_TOPIC_PROPERTIES = "topic-properties"
TAG_COMMENTSBOOK = "comments"
TAG_COMMENT = "comment"
TAG_CONTENT = "content"
# Attr
ATTR_VERSION = "version"
ATTR_ID = "id"
ATTR_STYLE_ID = "style-id"
ATTR_STRUCTURE_CLASS = "structure-class"
ATTR_TIMESTAMP = "timestamp"
ATTR_THEME = "theme"
ATTR_X = "svg:x"  # 自由主题X坐标
ATTR_Y = "svg:y"  # 自由主题Y坐标
ATTR_HREF = "xlink:href"
ATTR_BRANCH = "branch"
ATTR_TYPE = "type"
ATTR_END1 = "end1"  # relationship: start topic id
ATTR_END2 = "end2"  # relationship: end topic id
ATTR_MARKERID = "marker-id"
ATTR_SHAPE_CLASS = "shape-class"
ATTR_LINE_CLASS = "line-class"
ATTR_STYLE_COLOR = "svg:fill"
ATTR_AUTHOR = "author"
ATTR_OBJECT_ID = "object-id"
ATTR_TIME = "time"
# Topic Type
VAL_FOLDED = "folded"
TOPIC_ROOT = "root"
TOPIC_ATTACHED = "attached"
TOPIC_DETACHED = "detached"
# Hyperlink Type
FILE_PROTOCOL = "file://"  # file hyperlink
TOPIC_PROTOCOL = "xmind:#"  # topic hyperlink
HTTP_PROTOCOL = "http://"  # hyperlink
HTTPS_PROTOCOL = "https://"  # hyperlink
# Note Type
HTML_FORMAT_NOTE = "html"
PLAIN_FORMAT_NOTE = "plain"
