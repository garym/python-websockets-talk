#!/usr/bin/env python

import redis

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url

db = redis.StrictRedis('db', 6379, 0)
db.set('connections', 0)

class ConnectionsHandler(RequestHandler):
    def get(self):
        connections = db.incr('connections')
        self.render("templates/connections.html", connections=connections)

def make_app():
    return Application([url(r"/", ConnectionsHandler),
                       ], autoreload=True)
  
def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
