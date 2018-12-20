# -*- coding: utf-8 -*-
"""client view"""

from app.util.base import BaseHandler


class UserViewer(BaseHandler):
    def get(self):
        self.render('user/user.html', title='用户列表')


class UserAddViewer(BaseHandler):
    def get(self):
        items = ['用户添加', '用户删除']
        self.render('user/userAdd.html', title='用户添加', items=items)
