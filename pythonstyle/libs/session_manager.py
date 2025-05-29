# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-25
'''
from flask import session

class SessionManager:
    @staticmethod
    def set(key, value):
        session[key] = value

    @staticmethod
    def get(key, default=None):
        return session.get(key, default)

    @staticmethod
    def delete(key):
        session.pop(key, None)
