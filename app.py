# -*- coding: utf-8 -*-
"""很简单的一个demo"""

import os
import tornado.wsgi
import tornado.web
import tornado.options
import tornado.ioloop


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user = self.current_user)

class LoginHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.redirect('/')
            return
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("username"))
        self.redirect(self.get_argument('next', '/'))

class LogoutHandler(BaseHandler):
    def get(self):
        if not self.get_current_user():
            self.redirect('/')
            return
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))

class TestHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write("Testing!")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "login_url": "/login",
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "gzip": True,
    "debug": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/test", TestHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()