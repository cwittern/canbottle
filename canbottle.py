#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bottle import route, run
from bottle import static_file

@route('/css/:filename')
def server_css(filename):
    return static_file(filename, root='css')
@route('/images/:filename')
def server_images(filename):
    return static_file(filename, root='images')
@route('/js/:filename')
def server_js(filename):
    return static_file(filename, root='js')

@route('/lib/:filename')
def server_lib(filename):
    return static_file(filename, root='lib')

@route('/lib/xsltforms/:filename')
def server_xsltforms(filename):
    return static_file(filename, root='xsltforms')

@route('/:filename')
def server_root(filename):
    return static_file(filename, root='.')


run(host='localhost', port=8976)
