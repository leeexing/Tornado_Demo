# -*- coding: utf-8 -*-
"""首页"""

import json
import redis
import tornado.web
from tornado import gen
from tornado.httpclient  import AsyncHTTPClient


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)


async def test_async(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        if not self.get_secure_cookie('tornado_cookie'):
            self.set_secure_cookie('tornado_cookie', 'black_friday')
            self.write('Your cookie was not set yet~')
        else:
            data = yield [fetch_coroutine('http://www.leeing.cn:5280') for i in range(3)]
            data = [item.decode() for item in data]
            self.write(''.join(data))

    # - 或者
    async def post(self):
        data = await fetch_coroutine('http://www.leeing.cn:5280')
        self.write(data)


class FactorialService:
    def __init__(self):
        self.cache = redis.StrictRedis('localhost', 6379)
        self.key = 'factorials'

    def calc(self, n):
        s = self.cache.hget(self.key, str(n)) # 用hash结构保存计算结果
        if s:
            return int(s), True
        s = 1
        for item in range(1, n):
            s *= item
        self.cache.hset(self.key, str(n), str(s))
        return s, False


class FactorialHandler(tornado.web.RequestHandler):

    service = FactorialService()

    def get(self):
        n = int(self.get_argument('n') or 1)
        fact, cached = self.service.calc(n)
        result = {
            'n': n,
            'fact': fact,
            'cached': cached
        }
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(result))


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'name': 'nana', 'data': [1256,45, 89]})

    def post(self):
        self.write({'name': 'leeing', 'data': [12,45, 89]})