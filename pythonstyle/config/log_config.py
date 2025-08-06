# -*- coding: utf-8 -*-
import json
from pythonstyle.libs.param import Param
from pythonstyle.common import utils
from pythonstyle.libs.jwt_manager import JWTManager
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.dept import DeptEntity
from pythonstyle.libs.async_log_service import AsyncLogService
from pythonstyle.app import create_app
app = create_app()
def Log(func):
    '''
    描述：日志文件装饰器 用于记录操作日志
    作者: <insert author name here>
    日期: 2024-01-31
    '''
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        if app.config['log']['operationEnabled']:
            params = Param()
            m_name = params.get_m()
            c_name = params.get_c()
            a_name = params.get_a()
            url = params.get_url()

            is_post = utils.isPost()
            req_ip = utils.getRequestIp()

            status = '0'
            error_msg = ''
            headers = utils.getHttpAllHeaders()
            os = headers.get('Sec-Ch-Ua-Platform','Windows')

            browser = headers.get('Sec-Ch-Ua','')
            #登录日志特殊处理
            if is_post and a_name == 'login':
                param_data = utils.postRequestJson()
                request_method = 'POST'
                return_data = get_return_data(result)
                if return_data['code'] != 200:
                    status = '1'
                param = {
                    'username': param_data['username'],
                    'status': status,
                    'os': os,
                    'browser': browser,
                    'ip_address': req_ip,
                    'login_location': '',
                    'return_code': return_data['code']
                }
                AsyncLogService().add_login_log(param)
            #其他访问日志
            elif utils.getHttpHeaders('Authorization') != False:
                token = headers['Authorization'].replace('Bearer ', '')

                userinfo = get_userinfo(token)

                if utils.isGet():
                    param_data = utils.getRequestJson()
                    request_method = 'GET'
                elif utils.isPost():
                    param_data = utils.postRequestJson()
                    request_method = 'POST'

                business_type = get_business_type(a_name)
                op_type = 0
                if 'Windows' in os:
                    op_type = 1

                return_data = get_return_data(result)
                if return_data['code'] != 200:
                    status = '1'
                    error_msg = return_data['msg']
                param = {
                    'title': m_name,
                    'business_type': business_type,
                    'method': a_name,
                    'request_method': request_method,
                    'op_type': op_type,
                    'op_name': userinfo['username'],
                    'dept_name': userinfo['deptname'],
                    'op_url': url,
                    'op_ip': req_ip,
                    'op_location': '',
                    'op_param': str(param_data),
                    'json_result': str(return_data),
                    'status': status,
                    'error_msg': error_msg
                }
                AsyncLogService().add_action_log(param)

        return result
    return wrapper


def get_return_data(result):
    rst = result.__dict__
    data = rst['response'][0].decode('utf-8')
    return_data = json.loads(data)

    return return_data

def get_business_type(a_name):

    business_type = 0
    if 'add' in a_name:
        business_type = 1
    if 'update' in a_name or 'edit' in a_name:
        business_type = 2
    if 'delete' in a_name:
        business_type = 3
    return business_type

def get_userinfo(token):
    decoded_payload = JWTManager().verify_token(token)
    if (type(decoded_payload) != dict):
        return {'username':'','deptname':''}
    userinfo = UserEntity.get_datainfo_by_id(decoded_payload['user_id'])
    user_dept = DeptEntity.get_datainfo_by_id(userinfo['dept_id'])

    if userinfo['user_id'] > 0 and user_dept != None:
        return {'username':userinfo['username'],'deptname':user_dept['dept_name']}
    else:
        return {'username':'','deptname':''}
