# -*- coding: utf-8 -*-
"""
    spacepaste.controllers.json
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The JSON controller

    :copyright: 2008 by Armin Ronacher.
    :license: BSD
"""
from spacepaste import local
from spacepaste.lib.webapi import json
from spacepaste.utils import render_to_response


class JSONController(object):

    def handle_request(self):
        if local.request.args.get('method'):
            return json.handle_request()
        return render_to_response('json.html')


controller = JSONController
