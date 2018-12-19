# -*- coding: utf-8 -*-
"""路由映射"""

import os

from tornado.web import StaticFileHandler
from app.api import auth, home, image, user
from app.view import CLIENT_URLS


API_URLS = [
    # 权限管理
    (r'^/api/imagecode?', auth.ImageCodeHandler),  # 图片验证码
    (r'^/api/smscode?', auth.SMSCodeHandler),  # 短信验证码
    (r'^/api/login$', auth.LoginHandler),
    (r'^/api/logout$', auth.LogoutHandler),
    (r'^/api/register$', auth.RegisterHandler),
    (r'^/api/profile$', user.ProfileHandler),
    (r'^/api/profile/avatar$', user.AvatarHandler),
    (r'^/api/profile/name$', user.NameHandler),

    # 用户管理
    (r'^/api/user$', user.UserHandler),

    # 图像
    (r'^/api/image$', image.ImageHandler),

    # 其他
    (r'^/api/home$', home.MainHandler),
    (r'^/api/factorial$', home.FactorialHandler),
    (r'^/api/test$', home.TestHandler),

]

URLS = []
URLS.extend(API_URLS)
URLS.extend(CLIENT_URLS)
URLS.extend([
    (r"^/(.*?)$", StaticFileHandler,
      {'path': os.path.join(os.path.dirname(__file__), 'template'), 'default_filename': 'index.html'})
])
