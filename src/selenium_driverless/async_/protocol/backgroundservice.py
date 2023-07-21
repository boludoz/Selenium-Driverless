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

# ServiceName: The Background Service that will be associated with the commands/events.Every Background Service operates independently, but they share the sameAPI.
ServiceName = str

# EventMetadata: A key-value pair for additional event information to pass along.
class EventMetadata(ChromeTypeBase):
    def __init__(self,
                 key: Union['str'],
                 value: Union['str'],
                 ):

        self.key = key
        self.value = value


# BackgroundServiceEvent: 
class BackgroundServiceEvent(ChromeTypeBase):
    def __init__(self,
                 timestamp: Union['Network.TimeSinceEpoch'],
                 origin: Union['str'],
                 serviceWorkerRegistrationId: Union['ServiceWorker.RegistrationID'],
                 service: Union['ServiceName'],
                 eventName: Union['str'],
                 instanceId: Union['str'],
                 eventMetadata: Union['[EventMetadata]'],
                 ):

        self.timestamp = timestamp
        self.origin = origin
        self.serviceWorkerRegistrationId = serviceWorkerRegistrationId
        self.service = service
        self.eventName = eventName
        self.instanceId = instanceId
        self.eventMetadata = eventMetadata


class BackgroundService(PayloadMixin):
    """ Defines events for background web platform features.
    """
    @classmethod
    def startObserving(cls,
                       service: Union['ServiceName'],
                       ):
        """Enables event updates for the service.
        :param service: 
        :type service: ServiceName
        """
        return (
            cls.build_send_payload("startObserving", {
                "service": service,
            }),
            None
        )

    @classmethod
    def stopObserving(cls,
                      service: Union['ServiceName'],
                      ):
        """Disables event updates for the service.
        :param service: 
        :type service: ServiceName
        """
        return (
            cls.build_send_payload("stopObserving", {
                "service": service,
            }),
            None
        )

    @classmethod
    def setRecording(cls,
                     shouldRecord: Union['bool'],
                     service: Union['ServiceName'],
                     ):
        """Set the recording state for the service.
        :param shouldRecord: 
        :type shouldRecord: bool
        :param service: 
        :type service: ServiceName
        """
        return (
            cls.build_send_payload("setRecording", {
                "shouldRecord": shouldRecord,
                "service": service,
            }),
            None
        )

    @classmethod
    def clearEvents(cls,
                    service: Union['ServiceName'],
                    ):
        """Clears all stored data for the service.
        :param service: 
        :type service: ServiceName
        """
        return (
            cls.build_send_payload("clearEvents", {
                "service": service,
            }),
            None
        )



class RecordingStateChangedEvent(BaseEvent):

    js_name = 'Backgroundservice.recordingStateChanged'
    hashable = []
    is_hashable = False

    def __init__(self,
                 isRecording: Union['bool', dict],
                 service: Union['ServiceName', dict],
                 ):
        if isinstance(isRecording, dict):
            isRecording = bool(**isRecording)
        self.isRecording = isRecording
        if isinstance(service, dict):
            service = ServiceName(**service)
        self.service = service

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class BackgroundServiceEventReceivedEvent(BaseEvent):

    js_name = 'Backgroundservice.backgroundServiceEventReceived'
    hashable = []
    is_hashable = False

    def __init__(self,
                 backgroundServiceEvent: Union['BackgroundServiceEvent', dict],
                 ):
        if isinstance(backgroundServiceEvent, dict):
            backgroundServiceEvent = BackgroundServiceEvent(**backgroundServiceEvent)
        self.backgroundServiceEvent = backgroundServiceEvent

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
