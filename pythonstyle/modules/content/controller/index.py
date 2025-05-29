# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-01-31
'''
from pythonstyle.libs.result import Result
from pythonstyle.libs.html import Html

class index(Result):

    def init(self):
        data = [{'init':'欢迎来到网站首页'}]
        result = {
            'data': data
        }
        title = "网站标题"
        headers= {
            'Token':'sdfsdfsdgsfdgsdfgsdfgsdfg'
        }
        #print(utils.getHttpHeaders("Host"))
        #print(utils.http_uri())

        return  Html.render("content/index.html",headers=headers, title=title, result=result)
