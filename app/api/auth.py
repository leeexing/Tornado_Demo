# -*- coding: utf-8 -*-
"""权限认证"""

from app.util.base import BaseHandler


class RegisterHandler(BaseHandler):

    def post(self):
        pass


class LoginHandler(BaseHandler):

    def get(self):
        items = ['item1', 'item2', 'item3']
        self.render('base.html', title='Tornado', items=items)

    def post(self):
        pass


class LogoutHandler(BaseHandler):

    def post(self):
        pass


class ImageCodeHandler(BaseHandler):

    def get(self):
        pass


class SMSCodeHandler(BaseHandler):

    def get(self):
        pass
