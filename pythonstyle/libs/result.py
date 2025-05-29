# -*- coding: utf-8 -*-
'''
    描述：基础类
    作者: chinacsj
    日期: 2024-01-30
'''
from pythonstyle.libs.http_response import HttpResponse
from pythonstyle.libs.status_code import StatusCode

class Result(HttpResponse):
    @staticmethod
    def success(code=StatusCode.OK.value, msg='操作成功', data=[], mimetype="application/json", headers=None, ensure_ascii = False):
        '''
        描述 该方法返回200 带头信息的响应和带数据类型的返回
        :param msg:
        :param data:
        :param mimetype:
        :param headers:
        :return:
        '''
        result = {
            'code': code,
            'msg': msg,
            'data': data
        }

        return HttpResponse.setResponse(data=result, code=HttpResponse.getResponseStatus(), mimetype=mimetype, headers=headers, ensure_ascii = ensure_ascii)

    @staticmethod
    def error(code = 0, msg='操作失败', data=[],  mimetype="application/json", headers=None, ensure_ascii = False):
        '''
        描述：返回错误信息 带头信息，带返回数据
        :param msg:
        :param headers:
        :return:
        '''
        result = {
            'code': code,
            'msg': msg,
            'data':data
        }
        return HttpResponse.setResponse(data=result, code=HttpResponse.getResponseStatus(), mimetype=mimetype, headers=headers, ensure_ascii=ensure_ascii)

    @staticmethod
    def http_error(code, msg='操作失败', data=[]):
        '''
        描述：返回错误信息 带头信息，带返回数据
        :param msg:
        :param headers:
        :return:
        '''
        result = {
            'code': code,
            'msg': msg,
            'data':data
        }
        return HttpResponse.setHtmlResponse(data=result, code=code)

    @staticmethod
    def upload_success(code=0, msg='操作成功', data=[], mimetype="application/json", headers=None, ensure_ascii = False):
        '''
        描述 该方法返回0 带头信息的响应和带数据类型的返回 主要用于WangEditor编辑器上传图片和视频、附件等
        :param msg:
        :param data:{url，alt，href,poster} poster 视频封面图片
        :param mimetype:
        :param headers:
        :return:
        '''
        result = {
            'errno': code,
            'message': msg,
            'data': data
        }
        return HttpResponse.setResponse(data=result, code=HttpResponse.getResponseStatus(), mimetype=mimetype, headers=headers, ensure_ascii = ensure_ascii)

    @staticmethod
    def upload_error(code=1, msg='操作失败', data=[], headers=None, ensure_ascii = False):
        '''
        描述：返回错误信息 带头信息，带返回数据
        :param msg:
        :param headers:
        :return:
        '''
        result = {
            'errno': code,
            'message': msg,
            'data':data
        }
        return HttpResponse.setResponse(data=result, code=HttpResponse.getResponseStatus(), headers=headers, ensure_ascii=ensure_ascii)

    @staticmethod
    def text_success(code=StatusCode.OK.value, data='', mimetype="text/plain", headers=None, ensure_ascii = False):
        '''
        描述 该方法返回200 带头信息的响应和带数据类型的返回
        :param msg:
        :param data:
        :param mimetype:
        :param headers:
        :return:
        '''
        return HttpResponse.setTextResponse(data=data, code=HttpResponse.getResponseStatus(), mimetype=mimetype, headers=headers, ensure_ascii = ensure_ascii)