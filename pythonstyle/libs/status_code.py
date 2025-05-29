# -*- coding: utf-8 -*-
'''
    描述：http请求状态码枚举类
    作者: chinacsj@139.com
    日期: 2024-02-01
'''
from enum import Enum
class StatusCode(Enum):
    OK = 200            #请求成功。服务器成功处理了客户端请求。
    CREATED = 201       #请求已经被实现，并且有一个新的资源已经依据请求的需要而创建
    NOCONTENT = 204     #服务器成功处理了请求，但没有返回任何内容。
    BADREQUEST = 400    #请求错误。服务器不理解或无法处理客户端发送的请求。
    UNAUTHORIZED = 401  #未授权。需要身份验证或认证失败。
    FORBIDDEN = 403     #禁止访问。服务器拒绝执行请求。
    NOTFOUND = 404      #资源不存在。服务器未找到请求的资源。
    SERVERERROR = 500   #服务器内部错误。服务器遇到了一个意料不到的条件，导致无法完成请求。