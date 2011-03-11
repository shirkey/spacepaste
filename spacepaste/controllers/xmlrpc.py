# -*- coding: utf-8 -*-
"""
    spacepaste.controllers.xmlrpc
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The XMLRPC controller

    :copyright: 2007-2008 by Armin Ronacher, Georg Brandl, Christopher Grebs.
    :license: BSD
"""
from spacepaste import local
from spacepaste.utils import render_to_response
from spacepaste.lib.webapi import xmlrpc


class XMLRPCController(object):

    def handle_request(self):
        if local.request.method == 'POST':
            return xmlrpc.handle_request()
        return render_to_response('xmlrpc.html')


controller = XMLRPCController
