# -*- coding: utf-8 -*-
'''
    描述：Html类用于渲染html模板
    作者: chinacsj@139.com
    日期: 2024-02-04
'''
from flask import render_template, redirect, make_response

class Html:
    @classmethod
    def render(cls, name, *args, **kwargs):
        return render_template(name, *args, **kwargs)

    @classmethod
    def redirect(cls, url, headers = {}):
        goto = make_response(redirect(url))
        goto.headers = headers
        return goto

