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

# LayerId: Unique Layer identifier.
LayerId = str

# SnapshotId: Unique snapshot identifier.
SnapshotId = str

# ScrollRect: Rectangle where scrolling happens on the main thread.
class ScrollRect(ChromeTypeBase):
    def __init__(self,
                 rect: Union['DOM.Rect'],
                 type: Union['str'],
                 ):

        self.rect = rect
        self.type = type


# StickyPositionConstraint: Sticky position constraints.
class StickyPositionConstraint(ChromeTypeBase):
    def __init__(self,
                 stickyBoxRect: Union['DOM.Rect'],
                 containingBlockRect: Union['DOM.Rect'],
                 nearestLayerShiftingStickyBox: Optional['LayerId'] = None,
                 nearestLayerShiftingContainingBlock: Optional['LayerId'] = None,
                 ):

        self.stickyBoxRect = stickyBoxRect
        self.containingBlockRect = containingBlockRect
        self.nearestLayerShiftingStickyBox = nearestLayerShiftingStickyBox
        self.nearestLayerShiftingContainingBlock = nearestLayerShiftingContainingBlock


# PictureTile: Serialized fragment of layer picture along with its offset within the layer.
class PictureTile(ChromeTypeBase):
    def __init__(self,
                 x: Union['float'],
                 y: Union['float'],
                 picture: Union['str'],
                 ):

        self.x = x
        self.y = y
        self.picture = picture


# Layer: Information about a compositing layer.
class Layer(ChromeTypeBase):
    def __init__(self,
                 layerId: Union['LayerId'],
                 offsetX: Union['float'],
                 offsetY: Union['float'],
                 width: Union['float'],
                 height: Union['float'],
                 paintCount: Union['int'],
                 drawsContent: Union['bool'],
                 parentLayerId: Optional['LayerId'] = None,
                 backendNodeId: Optional['DOM.BackendNodeId'] = None,
                 transform: Optional['[]'] = None,
                 anchorX: Optional['float'] = None,
                 anchorY: Optional['float'] = None,
                 anchorZ: Optional['float'] = None,
                 invisible: Optional['bool'] = None,
                 scrollRects: Optional['[ScrollRect]'] = None,
                 stickyPositionConstraint: Optional['StickyPositionConstraint'] = None,
                 ):

        self.layerId = layerId
        self.parentLayerId = parentLayerId
        self.backendNodeId = backendNodeId
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.width = width
        self.height = height
        self.transform = transform
        self.anchorX = anchorX
        self.anchorY = anchorY
        self.anchorZ = anchorZ
        self.paintCount = paintCount
        self.drawsContent = drawsContent
        self.invisible = invisible
        self.scrollRects = scrollRects
        self.stickyPositionConstraint = stickyPositionConstraint


# PaintProfile: Array of timings, one per paint step.
PaintProfile = [float]

class LayerTree(PayloadMixin):
    """ 
    """
    @classmethod
    def compositingReasons(cls,
                           layerId: Union['LayerId'],
                           ):
        """Provides the reasons why the given layer was composited.
        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: LayerId
        """
        return (
            cls.build_send_payload("compositingReasons", {
                "layerId": layerId,
            }),
            cls.convert_payload({
                "compositingReasons": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def disable(cls):
        """Disables compositing tree inspection.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls):
        """Enables compositing tree inspection.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def loadSnapshot(cls,
                     tiles: Union['[PictureTile]'],
                     ):
        """Returns the snapshot identifier.
        :param tiles: An array of tiles composing the snapshot.
        :type tiles: [PictureTile]
        """
        return (
            cls.build_send_payload("loadSnapshot", {
                "tiles": tiles,
            }),
            cls.convert_payload({
                "snapshotId": {
                    "class": SnapshotId,
                    "optional": False
                },
            })
        )

    @classmethod
    def makeSnapshot(cls,
                     layerId: Union['LayerId'],
                     ):
        """Returns the layer snapshot identifier.
        :param layerId: The id of the layer.
        :type layerId: LayerId
        """
        return (
            cls.build_send_payload("makeSnapshot", {
                "layerId": layerId,
            }),
            cls.convert_payload({
                "snapshotId": {
                    "class": SnapshotId,
                    "optional": False
                },
            })
        )

    @classmethod
    def profileSnapshot(cls,
                        snapshotId: Union['SnapshotId'],
                        minRepeatCount: Optional['int'] = None,
                        minDuration: Optional['float'] = None,
                        clipRect: Optional['DOM.Rect'] = None,
                        ):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: SnapshotId
        :param minRepeatCount: The maximum number of times to replay the snapshot (1, if not specified).
        :type minRepeatCount: int
        :param minDuration: The minimum duration (in seconds) to replay the snapshot.
        :type minDuration: float
        :param clipRect: The clip rectangle to apply when replaying the snapshot.
        :type clipRect: DOM.Rect
        """
        return (
            cls.build_send_payload("profileSnapshot", {
                "snapshotId": snapshotId,
                "minRepeatCount": minRepeatCount,
                "minDuration": minDuration,
                "clipRect": clipRect,
            }),
            cls.convert_payload({
                "timings": {
                    "class": [PaintProfile],
                    "optional": False
                },
            })
        )

    @classmethod
    def releaseSnapshot(cls,
                        snapshotId: Union['SnapshotId'],
                        ):
        """Releases layer snapshot captured by the back-end.
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: SnapshotId
        """
        return (
            cls.build_send_payload("releaseSnapshot", {
                "snapshotId": snapshotId,
            }),
            None
        )

    @classmethod
    def replaySnapshot(cls,
                       snapshotId: Union['SnapshotId'],
                       fromStep: Optional['int'] = None,
                       toStep: Optional['int'] = None,
                       scale: Optional['float'] = None,
                       ):
        """Replays the layer snapshot and returns the resulting bitmap.
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: SnapshotId
        :param fromStep: The first step to replay from (replay from the very start if not specified).
        :type fromStep: int
        :param toStep: The last step to replay to (replay till the end if not specified).
        :type toStep: int
        :param scale: The scale to apply while replaying (defaults to 1).
        :type scale: float
        """
        return (
            cls.build_send_payload("replaySnapshot", {
                "snapshotId": snapshotId,
                "fromStep": fromStep,
                "toStep": toStep,
                "scale": scale,
            }),
            cls.convert_payload({
                "dataURL": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def snapshotCommandLog(cls,
                           snapshotId: Union['SnapshotId'],
                           ):
        """Replays the layer snapshot and returns canvas log.
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: SnapshotId
        """
        return (
            cls.build_send_payload("snapshotCommandLog", {
                "snapshotId": snapshotId,
            }),
            cls.convert_payload({
                "commandLog": {
                    "class": [],
                    "optional": False
                },
            })
        )



class LayerPaintedEvent(BaseEvent):

    js_name = 'Layertree.layerPainted'
    hashable = ['layerId']
    is_hashable = True

    def __init__(self,
                 layerId: Union['LayerId', dict],
                 clip: Union['DOM.Rect', dict],
                 ):
        if isinstance(layerId, dict):
            layerId = LayerId(**layerId)
        self.layerId = layerId
        if isinstance(clip, dict):
            clip = DOM.Rect(**clip)
        self.clip = clip

    @classmethod
    def build_hash(cls, layerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class LayerTreeDidChangeEvent(BaseEvent):

    js_name = 'Layertree.layerTreeDidChange'
    hashable = []
    is_hashable = False

    def __init__(self,
                 layers: Union['[Layer]', dict, None] = None,
                 ):
        if isinstance(layers, dict):
            layers = [Layer](**layers)
        self.layers = layers

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
