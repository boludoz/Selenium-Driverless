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
from . import runtime as Runtime

# ConsoleMessage: Console message.
class ConsoleMessage(ChromeTypeBase):
    def __init__(self,
                 source: Union['str'],
                 level: Union['str'],
                 text: Union['str'],
                 url: Optional['str'] = None,
                 line: Optional['int'] = None,
                 column: Optional['int'] = None,
                 ):

        self.source = source
        self.level = level
        self.text = text
        self.url = url
        self.line = line
        self.column = column


class Console(PayloadMixin):
    """ This domain is deprecated - use Runtime or Log instead.
    """
    @classmethod
    def clearMessages(cls):
        """Does nothing.
        """
        return (
            cls.build_send_payload("clearMessages", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables console domain, prevents further console messages from being reported to the client.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls):
        """Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )



class MessageAddedEvent(BaseEvent):

    js_name = 'Console.messageAdded'
    hashable = []
    is_hashable = False

    def __init__(self,
                 message: Union['ConsoleMessage', dict],
                 ):
        if isinstance(message, dict):
            message = ConsoleMessage(**message)
        self.message = message

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
