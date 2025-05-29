# -*- coding: utf-8 -*-
'''
    描述：初始化参数 加载控制器
    作者: chinacsj@139.com
    日期: 2024-01-31
'''
import importlib
from pythonstyle.libs.result import Result
from pythonstyle.config.filter_config import FilterConfig
import pythonstyle.model.model

class Application(Result):

    @FilterConfig
    @staticmethod
    def init( m, c, a):
        module = "pythonstyle.modules."+m+".controller."+c
        try:
            controller = importlib.import_module(module)
        except Exception as error:
            return Result.error(404, "您访问的资源不存在1！"+ str(error))
        try:
            className = getattr(controller, c)
        except Exception as error:
            return Result.error(404, "您访问的资源不存在2！"+ str(error))
        try:
            classInstance = className()
        except Exception as error:
            return Result.error(404, "您访问的资源不存在3！"+ str(error))
        try:
            funcName = getattr(classInstance, a)
            return funcName()
        except Exception as error:
            return Result.error(403, "The page is Forbidden！"+ str(error))