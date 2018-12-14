# -*- coding: utf-8 -*-
"""Seesion"""

import logging
import json
import uuid
import constants


class Session(object):
    """session类"""

    def __init__(self, request_handler):
        self.request_handler = request_handler
        # 从请求中读取cookie获取session_id
        self.sid = request_handler.get_secure_cookie("session_id")
        if self.sid:
            try:
                session_data = request_handler.redis.get("sess_{}".format(self.sid))
            except Exception as e:
                logging.error(e)
                raise e

            # session_data已过期，返回None
            if session_data:
                self.data = json.loads(session_data)
            else:
                self.data = {}

        # 如用户无session_id，需要生成新的对应该用户的session_id
        else:
            self.sid = uuid.uuid4().get_hex()
            self.data = {}
            self.request_handler.set_secure_cookie("session_id", self.sid)

    def save(self):
        """保存"""
        # 将session_data序列化为json字符串
        json_data = json.dumps(self.data)
        try:
            self.request_handler.redis.setex("sess_{}".format(self.sid), constants.SESSION_REDIS_EXPIRES, json_data)
        except Exception as e:
            logging.error(e)
            raise e

    def clear(self):
        """清除"""
        self.request_handler.clear_cookie("session_id")
        try:
            self.request_handler.redis.delete("sess_{}".format(self.sid))
        except Exception as e:
            logging.error(e)
            raise e
