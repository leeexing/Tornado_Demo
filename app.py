# -*- coding: utf-8 -*-
"""项目主文件"""

import tornado
from app.main import make_app


if __name__ == "__main__":
    # 转换命令行参数
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
