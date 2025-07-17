# -*- coding: utf-8 -*-
'''
    描述：默认过滤器配置,默认只允许登录，注册，验证码，可以访问
    作者: chinacsj@139.com
    日期: 2024-02-18
'''
import json
from flask import redirect,session
import itertools
from pythonstyle.libs.param import Param
from pythonstyle.libs.redis import Redis
from pythonstyle.common import utils
from pythonstyle.libs.jwt_manager import JWTManager
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.menu import MenuEntity
from pythonstyle.libs.result import Result

def FilterConfig(func):
    '''
    描述：定义配置文件装饰器 当配置有['pythonstyle']['profiles']['active'] 这个值时，合并两个配置文件
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        params = Param()
        # 获取默认的路由模块
        _M = params.get_m()
        # 获取默认的路由控制器名称
        _C = params.get_c()
        # 获取默认的路由控制器d 的方法名称 注意默认名称是 init()
        _A = params.get_a()
        # 配置默认模块过滤器
        m = ['system']
        # 配置默认控制器过滤器
        c = ['admin','captcha','menu']
        # 配置默认方法过滤器
        a = ['redirect','login','register','captcha_image','login_out']
        #默认拦截所有的
        is_passed = False
        #判断是否已经认证
        is_auth = False
        #预留一个模块作为WEB CMS前端模块不受拦截器限制

        for item in itertools.product(m, c, a):
            #print(f"{item[0]}-{item[1]}-{item[2]}")
            if _M == item[0] and _C == item[1] and _A == item[2]:
                is_passed = True
                break

        # 如果不在白名单里面就进行校验认证
        if is_passed == False:
            user_id = check_author()
            if user_id == False:
                return Result.error(401,'接口认证失败，请登录后重试')
            permission = f"{_M}:{_C}:{_A}"
            # 如果方法是public_开头，定义为是公共方法可以被外面调用
            # 主要用于一些选择数据接口
            if _A.startswith('public_'):
                is_passed = True
            else:
                is_passed = check_permission(user_id, permission)

        if is_passed:
            # 如果在默认配置中就往下执行
            rst = func(_M, _C, _A)
            return rst
        else:
            #否则，重定向到提示界面
            return Result.error(201,'您没有操作权限！请联系管理员')
    return wrapper

def check_author():
    '''
    描述：用于检测是否登录,前后端分离项目校验token 需要用header中的Authorization来判断
         第一步：先判断请求头是否有token
         第二步：如果有，解析token，获取userid和uuid
         第三步：判断数据库该用户是否存在
         第四步：判断redis是否缓存有数据 其实就是判断redis是否存在user:id这个key
    '''
    # 第一步：
    try:
        if utils.getHttpHeaders('Authorization') == None:
            return False
    except Exception as error:
        return False
    token = utils.getHttpHeaders('Authorization').replace('Bearer ','')

    decoded_payload = JWTManager().verify_token(token)
    if(type(decoded_payload) != dict):
        return False
    userinfo = UserEntity.get_datainfo_by_id(decoded_payload['user_id'])
    user_uuid = Redis().hget('login_data', userinfo['user_id']).decode()
    if userinfo['user_id'] > 0 and user_uuid !=None:
        return userinfo['user_id']
    else:
        return False

def check_permission(user_id, permission):
    user_data = UserEntity.get_user_roleinfo_by_id(user_id)
    if 1 in user_data['role_id']:
        return True
    return MenuEntity.get_role_menu_permission(user_data['role_id'],permission)