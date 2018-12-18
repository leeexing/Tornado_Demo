# -*- coding: utf-8 -*-
"""项目主文件
author： leeing
date：2018-12-18
"""

import tornado
import tornado.web
from app.util.base import Application
from app.urls import URLS
from app.conf import SETTINGS


if __name__ == "__main__":
    # 转换命令行参数
    # tornado.options.parse_command_line()
    app = Application(URLS, **SETTINGS)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
