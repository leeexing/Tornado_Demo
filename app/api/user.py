# -*- coding: utf-8 -*-
"""用户"""

import os
from app.util.base import BaseHandler


class UserHandler(BaseHandler):
    def get_template_path(self):
        return os.path.join(os.path.dirname(__file__), 'template/user')

    def get(self):
        items = ['item1', 'item2', 'item3']
        self.render('base.html', title='Tornado', items=items)


class ProfileHandler(BaseHandler):

    def get(self):
        pass


class AvatarHandler(BaseHandler):

    def post(self):
        pass


class NameHandler(BaseHandler):

    def post(self, *args, **kwargs):
        pass
