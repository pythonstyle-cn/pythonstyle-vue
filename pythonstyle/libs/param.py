# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-01-31
'''
from urllib.parse import urlparse, parse_qs
from pythonstyle.common import utils
from pythonstyle.config.route import router
from pythonstyle.libs.result import Result

class Param(Result):

    def __init__(self):
        self._m = router.get('m')
        self._c = router.get('c')
        self._a = router.get('a')
        self._params = {}
        self._url = ''

        url = utils.http_uri()
        parsed_url = urlparse(url)
        path_params = parsed_url.path.split("/")
        self._url = url
        self.get_default_uri(path_params)

        if len(path_params) >= 4:
            self._m, self._c, self._a = path_params[1:4]
            try:
                self._params = {path_params[i]: path_params[i + 1] for i in range(4, len(path_params), 2)}
            except Exception as error:
                return None


    def get_m(self):
        '''
        描述：获取模块名称
        :return:
        '''
        if utils.getRequest('m') != None:
            self._m = utils.getRequest('m')
        return self._m

    def get_c(self):
        '''
        描述：获取控制器名称
        :return:_c
        '''
        if utils.getRequest('c') != None:
            self._c = utils.getRequest('c')
        return self._c

    def get_a(self):
        '''
        描述：获取控制器方法名称
        :return:_a
        '''
        if utils.getRequest('a') != None:
            self._a = utils.getRequest('a')
        return self._a

    def get_params(self,name):
        '''
        描述：获取get参数
        :return:p_value
        '''
        if utils.getRequest(name) != None:
            return utils.getRequest(name)
        if len(self._params) > 0 and self._params[name] != None:
            return self._params[name]
        return None

    def get_url(self):
        return self._url

    def get_default_uri(self, path):
        if len(path) == 2:
            self._m = path[1] if path[1] != '' else router.get('m')
        if len(path) == 3:
            self._m = path[1] if path[1] != '' else router.get('m')
            self._c = path[2] if path[2] != '' else router.get('c')

