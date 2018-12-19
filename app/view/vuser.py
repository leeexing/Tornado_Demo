# -*- coding: utf-8 -*-
"""client view"""

from app.util.base import BaseHandler


class UserViewer(BaseHandler):

    def get(self):
        self.render('user.html', title='用户')
