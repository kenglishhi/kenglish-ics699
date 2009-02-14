"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
from webhelpers import *
from webhelpers.date import *
from webhelpers.text import *
from webhelpers.html.converters import *
from webhelpers.html.tools import *
from webhelpers.util import *
from webhelpers.rails.wrapped import *
from pylons.controllers.util import url_for

class Flash(object):
    def __call__(self, message):
        session = self._get_session()
        session["flash"] = message
        session.save()

    def pop_message(self):
        session = self._get_session()
        message = session.pop("flash", None)
        if not message:
            return None
        session.save()
        return message

    def _get_session(self):
        from pylons import session
        return session

flash = Flash()

