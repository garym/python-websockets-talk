#!/usr/bin/env python

import redis

from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url
from tornado.websocket import WebSocketHandler

db = redis.StrictRedis('db', 6379, 0)
db.set('connections', 0)

class ConnectionsPageHandler(RequestHandler):
    def get(self):
        connections = db.get('connections')
        self.render("templates/connections.html", connections=connections)


class ConnectionsHandler(WebSocketHandler):
    handlers = []

    def open(self):
        self.handlers.append(self)
        connections = db.incr('connections')
        self.broadcast_data({'connections': connections})

    def on_close(self):
        self.handlers.remove(self)
        connections = db.decr('connections')
        self.broadcast_data({'connections': connections})

    def broadcast_data(self, data):
        for handler in self.handlers:
            handler.write_message(data)


def make_app():
    return Application([url(r"/", ConnectionsPageHandler),
                        url(r"/socket/", ConnectionsHandler),
                       ], autoreload=True)
  
def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
