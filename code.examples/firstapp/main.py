#!/usr/bin/env python
# coding: utf-8
#
# はじめての Pyramid アプリケーション
#
#
#

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def _index(request):

	return Response('<html>Hello!</html>')
	
def _hello_world(request):

	return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':

	config = Configurator()
	config.add_route('index', '/')
	config.add_route('hello', '/hello/{name}')
	config.add_view(_index, route_name='index')
	config.add_view(_hello_world, route_name='hello')
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 80, app)
	server.serve_forever()
