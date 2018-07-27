#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import subprocess

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("tijiao.html")

    def post(self, *args, **kwargs):
        self.write("finish")


class pushHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.render("push.html")
#settings = {
#    'static_path': 'st',
#}

application = tornado.web.Application([
    (r"/", LoginHandler),
    (r'/index',pushHandler)
],)#**settings)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()