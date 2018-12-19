# -*- coding: utf-8 -*-
"""main view"""

from app.util.base import BaseHandler


class RegisterViewer(BaseHandler):
    def get(self):
        self.render('register.html')


class LoginViewer(BaseHandler):
    def get(self):
        items = ['item1', 'item2', 'item3']
        self.render('login.html', title='Tornado', items=items)


class IndexViewer(BaseHandler):
    def get(self):
        self.render('index.html')


class ImageViewer(BaseHandler):
    def get(self):
        self.render('image.html')


class AboutMeViewer(BaseHandler):
    def get(self):
        self.render('about.html')
