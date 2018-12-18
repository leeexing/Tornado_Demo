# -*- coding: utf-8 -*-
"""配置文件"""

import os


SETTINGS = {
    # 'debug': True, # 在debug模式下, 某些错误(例如import的时候有语法错误)会导致服务 关闭, 并且无法自动恢复.
    'autoreload': True, # 应用程序将会观察它的源文件是否改变, 并且当任何 文件改变的时候便重载它自己. 这减少了在开发中需要手动重启服务的需求
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'compiled_template_cache': False,
    'cookie_secret': '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o',
    'xsrf_cookies': True,
    'login_url': 'login'
}

# mysql配置
MYSQL_OPTIONS = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'flask'
}

# redis配置
REDIS_OPTIONS = {
    'host': '127.0.0.1',
    'port': 6379
}

# 日志文件
LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs/log')

# 日志等级
LOG_LEVEL = 'debug'

# 密码加密密钥
PASSWD_HASH_KEY = 'F3fv87mzTI6fKbP13gUNZI+eZrL1VEzguyX1+AVsRdI='

# 七牛空间域名
# IMAGE_URL_PREFIX = 'http://xxxx.bkt.clouddn.com/'
