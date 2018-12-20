# -*- coding: utf-8 -*-
"""权限认证"""

import json
import tornado
from app.util.base import BaseHandler


class RegisterHandler(BaseHandler):

    def post(self):
        pass


class LoginHandler(BaseHandler):

    def get(self):
        if self.get_current_user():
            self.redirect(self.get_argument('next', '/'))
            return
        self.render('login.html')

    def post(self):
        postData = json.loads(self.request.body)
        print(postData, '-- auth : login')
        username = postData.get('username')
        password = postData.get('password')
        self.set_current_user(username)
        self.write({'result': True})
        # self.redirect(self.get_argument('next', u'/api/home'))
        return

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie('user')


class LogoutHandler(BaseHandler):

    def post(self):
        pass


class ImageCodeHandler(BaseHandler):

    def get(self):
        pass


class SMSCodeHandler(BaseHandler):

    def get(self):
        pass
