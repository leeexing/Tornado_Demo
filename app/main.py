# -*- coding:utf-8 -*-
"""
author： leeing
date：2018-12-18
"""

import tornado.web
from app.urls import URLS
from app.conf import SETTINGS


## 系统入口app 及 路由层
def make_app():
    return tornado.web.Application(URLS, **SETTINGS)
