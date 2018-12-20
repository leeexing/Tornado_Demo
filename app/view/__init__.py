# -*- coding: utf-8 -*-
"""client view"""

from .vuser import *
from .vmain import *

CLIENT_URLS = [
    (r'^/register$', RegisterViewer),
    (r'^/login$', LoginViewer),
    (r'^/image$', ImageViewer),
    (r'^/about$', AboutMeViewer),
    (r'^/user$', UserViewer),
    (r'^/user/add$', UserAddViewer),
    (r'^/$', IndexViewer),
]
