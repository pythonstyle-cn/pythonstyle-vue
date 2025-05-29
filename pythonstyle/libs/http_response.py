# -*- coding: utf-8 -*-
'''
    描述： 响应http请求类，用于动态响应请求
    作者: chinacsj@139.com
    日期: 2024-02-01
'''
from flask import make_response,jsonify
import json

class HttpResponse:

    @staticmethod
    def setResponse(data, code, headers=None, mimetype="application/json", jsonify=jsonify, ensure_ascii=False):
        '''
        描述：设置GET请求响应参数
        :param data: 响应数据
        :param code: 响应状态码
        :param headers: 自定义响应头
        :param mimetype: 默认为application/json
        :param ensure_ascii: 是否保证响应内容为ASCII编码
        :return: 返回一个响应对象
        '''
        # 如果是4xx或5xx错误码，直接返回错误响应
        if 403 <= code < 600:
            return HttpResponse._generate_error_response(code, headers, mimetype)

        # 正常响应数据
        data = json.dumps(data, ensure_ascii=ensure_ascii)
        response = make_response(data)
        response.status_code = code
        if headers:
            response.headers = headers
        response.mimetype = mimetype

        return response

    @staticmethod
    def setHtmlResponse(data, code, headers=None, mimetype="text/html", jsonify=jsonify, ensure_ascii=False):
        '''
        描述：设置HTML响应，适用于网页内容
        :param data: 响应数据
        :param code: 响应状态码
        :param headers: 自定义响应头
        :param mimetype: 默认为text/html
        :param ensure_ascii: 是否保证响应内容为ASCII编码
        :return: 返回一个HTML响应对象
        '''
        # 如果是4xx或5xx错误码，直接返回错误响应
        if 403 <= code < 600:
            return HttpResponse._generate_error_response(code, headers, mimetype)

        # 正常响应数据
        response = make_response(data)
        response.status_code = code
        if headers:
            response.headers = headers
        response.mimetype = mimetype

        return response

    @staticmethod
    def setTextResponse(data, code, headers=None, mimetype="text/plain", jsonify=jsonify, ensure_ascii=False):
        '''
        描述：设置纯文本响应，适用于显示 .txt 文件的内容
        :param data: 响应数据
        :param code: 响应状态码
        :param headers: 自定义响应头
        :param mimetype: 默认为text/plain
        :param ensure_ascii: 是否保证响应内容为ASCII编码
        :return: 返回一个纯文本响应对象
        '''
        # 如果是4xx或5xx错误码，直接返回错误响应
        if 403 <= code < 600:
            return HttpResponse._generate_error_response(code, headers, mimetype)

        # 正常响应数据
        if isinstance(data, str):
            response_data = data
        else:
            response_data = json.dumps(data, ensure_ascii=ensure_ascii)

        # 创建响应对象
        response = make_response(response_data)
        response.status_code = code
        if headers:
            response.headers = headers
        response.mimetype = mimetype

        return response

    @staticmethod
    def getResponseStatus():
        '''
        描述：返回请求响应状态码
        :return: status_code
        '''
        response = make_response()
        return response.status_code

    @staticmethod
    def _generate_error_response(code, headers=None, mimetype="text/html"):
        '''
        描述：生成错误响应，返回真实的 HTTP 错误状态码
        :param code: 错误状态码
        :param headers: 自定义响应头
        :param mimetype: 响应内容的MIME类型
        :return: 返回一个错误响应对象
        '''
        # 这里不返回 JSON 错误消息，而是通过 Nginx 或 Web 服务器来处理错误页面
        response = make_response('')  # 空内容，交给 Nginx 处理
        response.status_code = code
        if headers:
            response.headers = headers
        response.mimetype = mimetype

        return response