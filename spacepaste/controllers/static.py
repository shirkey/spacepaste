# -*- coding: utf-8 -*-
"""
    spacepaste.controllers.static
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Static stuff.

    :copyright: 2007-2008 by Armin Ronacher, Christopher Grebs.
    :license: BSD
"""
from werkzeug.exceptions import NotFound
from spacepaste import local
from spacepaste.i18n import lazy_gettext
from spacepaste.utils import render_to_response
from spacepaste.lib.webapi import get_public_methods
from spacepaste.lib.highlighting import LANGUAGES


HELP_PAGES = [
    ('pasting',         lazy_gettext('Pasting')),
    ('advanced',        lazy_gettext('Advanced Features')),
    ('api',             lazy_gettext('Using the LodgeIt API')),
    ('integration',     lazy_gettext('Scripts and Editor Integration'))
]

known_help_pages = set(x[0] for x in HELP_PAGES)


class StaticController(object):

    def not_found(self):
        return render_to_response('not_found.html')

    def removal(self):
        return render_to_response('removal.html')

controller = StaticController
