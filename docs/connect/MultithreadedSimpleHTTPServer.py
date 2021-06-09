#!/usr/bin/env python

# This simple web server was downloaded from this GitHub Repository:
# https://github.com/Nakiami/MultithreadedSimpleHTTPServer
# Credits to: Nakiami, JCBird1012, bugaevc, and Qu4tro

try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

import sys
import os

if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        interface = address.split(':')[0]
        port = int(address.split(':')[1])
    else:
        interface = '0.0.0.0'
        port = int(address)
else:
    port = 80
    interface = '0.0.0.0'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

print('Started HTTP server on ' +  interface + ':' + str(port))

server = ThreadingSimpleServer((interface, port), SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print('Finished.')
