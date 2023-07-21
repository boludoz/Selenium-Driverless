# Copyright 2017 Robert Charles Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# modified by kaliiiiiiiiii | Aurin Aegerter

# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from ..helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from . import dom as DOM
from . import page as Page
from . import runtime as Runtime

# HighlightConfig: Configuration data for the highlighting of page elements.
class HighlightConfig(ChromeTypeBase):
    def __init__(self,
                 showInfo: Optional['bool'] = None,
                 showStyles: Optional['bool'] = None,
                 showRulers: Optional['bool'] = None,
                 showExtensionLines: Optional['bool'] = None,
                 contentColor: Optional['DOM.RGBA'] = None,
                 paddingColor: Optional['DOM.RGBA'] = None,
                 borderColor: Optional['DOM.RGBA'] = None,
                 marginColor: Optional['DOM.RGBA'] = None,
                 eventTargetColor: Optional['DOM.RGBA'] = None,
                 shapeColor: Optional['DOM.RGBA'] = None,
                 shapeMarginColor: Optional['DOM.RGBA'] = None,
                 cssGridColor: Optional['DOM.RGBA'] = None,
                 ):

        self.showInfo = showInfo
        self.showStyles = showStyles
        self.showRulers = showRulers
        self.showExtensionLines = showExtensionLines
        self.contentColor = contentColor
        self.paddingColor = paddingColor
        self.borderColor = borderColor
        self.marginColor = marginColor
        self.eventTargetColor = eventTargetColor
        self.shapeColor = shapeColor
        self.shapeMarginColor = shapeMarginColor
        self.cssGridColor = cssGridColor


# InspectMode: 
InspectMode = str

class Overlay(PayloadMixin):
    """ This domain provides various functionality related to drawing atop the inspected page.
    """
    @classmethod
    def disable(cls):
        """Disables domain notifications.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls):
        """Enables domain notifications.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def getHighlightObjectForTest(cls,
                                  nodeId: Union['DOM.NodeId'],
                                  includeDistance: Optional['bool'] = None,
                                  includeStyle: Optional['bool'] = None,
                                  ):
        """For testing.
        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: DOM.NodeId
        :param includeDistance: Whether to include distance info.
        :type includeDistance: bool
        :param includeStyle: Whether to include style info.
        :type includeStyle: bool
        """
        return (
            cls.build_send_payload("getHighlightObjectForTest", {
                "nodeId": nodeId,
                "includeDistance": includeDistance,
                "includeStyle": includeStyle,
            }),
            cls.convert_payload({
                "highlight": {
                    "class": dict,
                    "optional": False
                },
            })
        )

    @classmethod
    def hideHighlight(cls):
        """Hides any highlight.
        """
        return (
            cls.build_send_payload("hideHighlight", {
            }),
            None
        )

    @classmethod
    def highlightFrame(cls,
                       frameId: Union['Page.FrameId'],
                       contentColor: Optional['DOM.RGBA'] = None,
                       contentOutlineColor: Optional['DOM.RGBA'] = None,
                       ):
        """Highlights owner element of the frame with given id.
        :param frameId: Identifier of the frame to highlight.
        :type frameId: Page.FrameId
        :param contentColor: The content box highlight fill color (default: transparent).
        :type contentColor: DOM.RGBA
        :param contentOutlineColor: The content box highlight outline color (default: transparent).
        :type contentOutlineColor: DOM.RGBA
        """
        return (
            cls.build_send_payload("highlightFrame", {
                "frameId": frameId,
                "contentColor": contentColor,
                "contentOutlineColor": contentOutlineColor,
            }),
            None
        )

    @classmethod
    def highlightNode(cls,
                      highlightConfig: Union['HighlightConfig'],
                      nodeId: Optional['DOM.NodeId'] = None,
                      backendNodeId: Optional['DOM.BackendNodeId'] = None,
                      objectId: Optional['Runtime.RemoteObjectId'] = None,
                      selector: Optional['str'] = None,
                      ):
        """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
objectId must be specified.
        :param highlightConfig: A descriptor for the highlight appearance.
        :type highlightConfig: HighlightConfig
        :param nodeId: Identifier of the node to highlight.
        :type nodeId: DOM.NodeId
        :param backendNodeId: Identifier of the backend node to highlight.
        :type backendNodeId: DOM.BackendNodeId
        :param objectId: JavaScript object id of the node to be highlighted.
        :type objectId: Runtime.RemoteObjectId
        :param selector: Selectors to highlight relevant nodes.
        :type selector: str
        """
        return (
            cls.build_send_payload("highlightNode", {
                "highlightConfig": highlightConfig,
                "nodeId": nodeId,
                "backendNodeId": backendNodeId,
                "objectId": objectId,
                "selector": selector,
            }),
            None
        )

    @classmethod
    def highlightQuad(cls,
                      quad: Union['DOM.Quad'],
                      color: Optional['DOM.RGBA'] = None,
                      outlineColor: Optional['DOM.RGBA'] = None,
                      ):
        """Highlights given quad. Coordinates are absolute with respect to the main frame viewport.
        :param quad: Quad to highlight
        :type quad: DOM.Quad
        :param color: The highlight fill color (default: transparent).
        :type color: DOM.RGBA
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: DOM.RGBA
        """
        return (
            cls.build_send_payload("highlightQuad", {
                "quad": quad,
                "color": color,
                "outlineColor": outlineColor,
            }),
            None
        )

    @classmethod
    def highlightRect(cls,
                      x: Union['int'],
                      y: Union['int'],
                      width: Union['int'],
                      height: Union['int'],
                      color: Optional['DOM.RGBA'] = None,
                      outlineColor: Optional['DOM.RGBA'] = None,
                      ):
        """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.
        :param x: X coordinate
        :type x: int
        :param y: Y coordinate
        :type y: int
        :param width: Rectangle width
        :type width: int
        :param height: Rectangle height
        :type height: int
        :param color: The highlight fill color (default: transparent).
        :type color: DOM.RGBA
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: DOM.RGBA
        """
        return (
            cls.build_send_payload("highlightRect", {
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
                "outlineColor": outlineColor,
            }),
            None
        )

    @classmethod
    def setInspectMode(cls,
                       mode: Union['InspectMode'],
                       highlightConfig: Optional['HighlightConfig'] = None,
                       ):
        """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
Backend then generates 'inspectNodeRequested' event upon element selection.
        :param mode: Set an inspection mode.
        :type mode: InspectMode
        :param highlightConfig: A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled
== false`.
        :type highlightConfig: HighlightConfig
        """
        return (
            cls.build_send_payload("setInspectMode", {
                "mode": mode,
                "highlightConfig": highlightConfig,
            }),
            None
        )

    @classmethod
    def setShowAdHighlights(cls,
                            show: Union['bool'],
                            ):
        """Highlights owner element of all frames detected to be ads.
        :param show: True for showing ad highlights
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowAdHighlights", {
                "show": show,
            }),
            None
        )

    @classmethod
    def setPausedInDebuggerMessage(cls,
                                   message: Optional['str'] = None,
                                   ):
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: str
        """
        return (
            cls.build_send_payload("setPausedInDebuggerMessage", {
                "message": message,
            }),
            None
        )

    @classmethod
    def setShowDebugBorders(cls,
                            show: Union['bool'],
                            ):
        """Requests that backend shows debug borders on layers
        :param show: True for showing debug borders
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowDebugBorders", {
                "show": show,
            }),
            None
        )

    @classmethod
    def setShowFPSCounter(cls,
                          show: Union['bool'],
                          ):
        """Requests that backend shows the FPS counter
        :param show: True for showing the FPS counter
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowFPSCounter", {
                "show": show,
            }),
            None
        )

    @classmethod
    def setShowPaintRects(cls,
                          result: Union['bool'],
                          ):
        """Requests that backend shows paint rectangles
        :param result: True for showing paint rectangles
        :type result: bool
        """
        return (
            cls.build_send_payload("setShowPaintRects", {
                "result": result,
            }),
            None
        )

    @classmethod
    def setShowLayoutShiftRegions(cls,
                                  result: Union['bool'],
                                  ):
        """Requests that backend shows layout shift regions
        :param result: True for showing layout shift regions
        :type result: bool
        """
        return (
            cls.build_send_payload("setShowLayoutShiftRegions", {
                "result": result,
            }),
            None
        )

    @classmethod
    def setShowScrollBottleneckRects(cls,
                                     show: Union['bool'],
                                     ):
        """Requests that backend shows scroll bottleneck rects
        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowScrollBottleneckRects", {
                "show": show,
            }),
            None
        )

    @classmethod
    def setShowHitTestBorders(cls,
                              show: Union['bool'],
                              ):
        """Requests that backend shows hit-test borders on layers
        :param show: True for showing hit-test borders
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowHitTestBorders", {
                "show": show,
            }),
            None
        )

    @classmethod
    def setShowViewportSizeOnResize(cls,
                                    show: Union['bool'],
                                    ):
        """Paints viewport size upon main frame resize.
        :param show: Whether to paint size or not.
        :type show: bool
        """
        return (
            cls.build_send_payload("setShowViewportSizeOnResize", {
                "show": show,
            }),
            None
        )



class InspectNodeRequestedEvent(BaseEvent):

    js_name = 'Overlay.inspectNodeRequested'
    hashable = ['backendNodeId']
    is_hashable = True

    def __init__(self,
                 backendNodeId: Union['DOM.BackendNodeId', dict],
                 ):
        if isinstance(backendNodeId, dict):
            backendNodeId = DOM.BackendNodeId(**backendNodeId)
        self.backendNodeId = backendNodeId

    @classmethod
    def build_hash(cls, backendNodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NodeHighlightRequestedEvent(BaseEvent):

    js_name = 'Overlay.nodeHighlightRequested'
    hashable = ['nodeId']
    is_hashable = True

    def __init__(self,
                 nodeId: Union['DOM.NodeId', dict],
                 ):
        if isinstance(nodeId, dict):
            nodeId = DOM.NodeId(**nodeId)
        self.nodeId = nodeId

    @classmethod
    def build_hash(cls, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ScreenshotRequestedEvent(BaseEvent):

    js_name = 'Overlay.screenshotRequested'
    hashable = []
    is_hashable = False

    def __init__(self,
                 viewport: Union['Page.Viewport', dict],
                 ):
        if isinstance(viewport, dict):
            viewport = Page.Viewport(**viewport)
        self.viewport = viewport

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class InspectModeCanceledEvent(BaseEvent):

    js_name = 'Overlay.inspectModeCanceled'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
