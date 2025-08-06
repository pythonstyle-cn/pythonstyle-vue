# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.libs.param import Param
from pythonstyle.common import utils
from pythonstyle.config.log_config import Log
from pythonstyle.libs.jwt_manager import JWTManager
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.user_role import UserRoleEntity
from pythonstyle.modules.system.entity.user_post import UserPostEntity

class user(Result):
    def get_list(self):
        '''
        描述：获取用户列表
        '''
        params = utils.getRequestJson()
        # 获取用户列表
        user_list = UserEntity.get_user_list(params)
        user_count = UserEntity.get_count(params)
        total_page = utils.getCeil(user_count/int(params['pageSize']))
        data = {
            'list': user_list,
            'total': user_count,
            'pageNum': int(params['pageNum']),
            'pageSize': int(params['pageSize']),
            'totalPage': total_page
        }
        return Result.success(msg='操作成功', data = data)

    def public_get_info(self):
        '''
        描述：获取用户单条信息
        参数：user_id 用户id
        '''
        id = utils.getRequest('user_id')
        dataInfo = UserEntity.get_datainfo_by_id(id)
        return Result.success(msg='操作成功', data=dataInfo)

    def add(self):
        '''
        描述：添加用户信息
        参数：用户表字段
        '''
        params = utils.postRequestJson()
        params = utils.dictNullToempty(params)
        # 用户所属角色
        role_ids =  params.pop('role_ids')
        # 用户所属部门
        try:
            post_ids = params.pop('post_ids')
        except Exception as e:
            post_ids = []
        # 如果传过来密码则加密
        password = params['password'] + 'edsdkjjhnsdf'
        md5_password = utils.md5_encrypt(password)
        params['password'] = md5_password
        #添加
        user_id = UserRoleEntity.add_data(params, role_ids)

        if user_id > 0:
            if len(post_ids) > 0:
                r = UserPostEntity.add_data(user_id, post_ids)
                if(r == False):
                    return Result.error(code=202, msg='操作失败')
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')
    @Log
    def update(self):
        '''
        描述：修改用户信息
        参数：用户表字段，必须包含user_id
        '''
        params = utils.postRequestJson()
        if params['user_id'] == None:
            return Result.error(code=201, msg='修改失败，缺少主键参数！')
        redis_userinfo = self.get_redis_userinfo_id()
        password = utils.filter_xss(params['password'])+'edsdkjjhnsdf'
        md5_password = utils.md5_encrypt(password)
        params['password'] = md5_password
        # 不允许非超级管理员修改其他人信息
        if 1 not in redis_userinfo['role_id']:
            if params['user_id'] != redis_userinfo['user_id']:
                return Result.error(code=206, msg='操作失败，非超级管理员不能修改别人的信息！')
            password = params.pop('password')
        else:
            if params['user_id'] == redis_userinfo['user_id']:
                password = params.pop('password')

        params['update_time'] = utils.formatDate()

        create_time = params.pop('create_time')
        role_ids = params.pop('role_ids')
        try:
            post_ids = params.pop('post_ids')
        except Exception as e:
            post_ids = []
        result = UserRoleEntity.edit_data(params, role_ids)
        if result:
            if len(post_ids) > 0:
                r = UserPostEntity.edit_data(params['user_id'], post_ids)
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def updateStatus(self):
        '''
        描述：修改用户状态
        参数：用户表字段，必须包含user_id和status字段
        '''
        params = utils.postRequestJson()
        param = {'user_id':params['user_id'],'status':params['status']}
        result = UserEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    def user_delete(self):
        '''
        描述：添加用户信息
        参数：用户表字段
        '''
        params = utils.getRequestJson()
        if int(params['user_id']) == 1:
            return Result.error(code=202, msg='操作失败,系统默认超级管理员不允许删除')
        rst = UserEntity.delete_by_id(params)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def public_get_user_roleids(self):
        '''
        描述：根据user_id 获取所属的角色ids
        '''
        params = utils.postRequestJson()
        if params['user_id'] == None:
            return Result.error(code=201, msg='修改失败，缺少主键参数！')
        user_id = params['user_id']
        data = UserEntity.get_user_roleinfo_by_id(user_id)
        if data:
            return Result.success(msg='操作成功',data=data['role_id'])

        return Result.error(msg='操作失败')

    def public_get_user_postids(self):
        '''
        描述：根据user_id 获取所属的角色ids
        '''
        params = utils.postRequestJson()
        if params['user_id'] == None:
            return Result.error(code=201, msg='修改失败，缺少主键参数！')
        user_id = params['user_id']
        data = UserEntity.get_user_postinfo_by_id(user_id)
        if data:
            return Result.success(msg='操作成功',data=data['post_id'])

        return Result.error(msg='操作失败')

    def get_redis_userinfo_id(self):
        token = utils.getHttpHeaders('Authorization').replace('Bearer ', '')
        decoded_payload = JWTManager().verify_token(token)
        userinfo = UserEntity.get_user_roleinfo_by_id(decoded_payload['user_id'])
        return userinfo