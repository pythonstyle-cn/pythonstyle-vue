# -*- coding: utf-8 -*-
'''
    描述：用户实体类
    作者: chinacsj@139.com
    日期: 2024-02-08
'''
from pony.orm import *
from pythonstyle.common.utils import formatDate
from pythonstyle.config.db_config import create_db
db = create_db('mysql')

from pythonstyle.modules.system.entity.role import RoleEntity

class UserEntity(db.Entity):
    _table_ = 'sys_user'  # 设置表名
    user_id = PrimaryKey(int, auto=True)
    dept_id = Optional(int,default=1)
    username = Required(str)
    password = Required(str)
    nick_name = Optional(str)
    user_type = Optional(str, default='0')
    email = Optional(str)
    phone = Optional(str)
    sex = Optional(str, default='0')
    avatar = Optional(str)
    status = Optional(str,default='0')
    del_flag = Optional(str)
    login_ip = Optional(str)
    login_date = Optional(str)
    create_user = Optional(str, default='')
    create_time = Optional(str, default='')
    update_user = Optional(str, default='')
    update_time = Optional(str)
    remark = Optional(str, default='')
    roles = Set('UserRoleEntity')
    posts = Set('UserPostEntity')

    @db_session
    @staticmethod
    def get_user_list(param):
        '''
        描述：获取用户列表
        param：参数是一个字典，可以包含page用于分页
        '''
        userList = []
        where = raw_sql("1 = 1")
        if param['status']:
            where = raw_sql("p.status = " + param['status'])
        users = select(p for p in UserEntity if p.del_flag != 1  and
                       param['username'] in p.username and where).order_by(desc(UserEntity.user_id)).page(int(param['pageNum']), int(param['pageSize']))
        for p in users:
            p = UserEntity.formatDate(p)
            userList.append(p.to_dict(exclude='password'))
        return userList

    @db_session
    @staticmethod
    def get_count(param):
        where = raw_sql("1 = 1")
        if param['status']:
            where = raw_sql("e.status = " + param['status'])
        if param['dept_id']:
            where += raw_sql(" and e.dept_id = " + param['dept_id'])
        userCount = count(e for e in UserEntity if e.del_flag == 0 and where)
        return userCount

    @db_session
    @staticmethod
    def edit_data(param):
        #开启调试
        #set_sql_debug(True)
        result = UserEntity[param['user_id']].set(**param)
        # 更新成功 返回None 更新失败返回错误
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def get_login_info(username, password):
        '''
        描述：登录查询
        param：username 用户名  password 密码
        '''
        result = UserEntity.get(username=username, password=password,del_flag='0',status='0')
        if result:
            result = UserEntity.formatDate(result)
        return result

    @db_session
    @staticmethod
    def get_datainfo_by_id(primary_id):
        '''
            描述：根据用户id获取用户信息（除密码）
            param：primary_id 用户名  主键
        '''
        dataInfo = {}
        result = UserEntity.get(user_id=primary_id, del_flag='0')
        if result:
            result = UserEntity.formatDate(result)
            dataInfo = result.to_dict(exclude=['password'])
        return dataInfo

    @db_session
    @staticmethod
    def get_user_roleinfo_by_id(user_id):
        '''
        根据用户id获取用户信息 包含角色信息
        '''
        query = left_join(
            (user,ur)
            for user in UserEntity for ur in user.roles
            if raw_sql('user.user_id = $user_id'))[:]

        user_dict = {}
        user_role = []
        if len(query) > 0:
            for user, role in query[:]:
                user_dict = user.to_dict(exclude=['create_time','update_time','password'])
                if role != None:
                    role_dict = role.to_dict()
                    user_role.append(role_dict['role_id'])

        user_dict['role_id'] = user_role
        return user_dict

    @db_session
    @staticmethod
    def delete_by_id(param):
        result = UserEntity[param['user_id']].set(del_flag='1')
        if result == None:
            return True
        else:
            return False

    @db_session
    @staticmethod
    def get_user_postinfo_by_id(user_id):
        '''
        根据用户id获取用户信息 包含岗位信息
        '''
        query = left_join(
            (user, up)
            for user in UserEntity for up in user.posts
            if raw_sql('user.user_id = $user_id'))[:]

        user_dict = {}
        user_post = []
        if len(query) > 0:
            for user, post in query[:]:
                user_dict = user.to_dict(exclude=['create_time','update_time','password'])
                if post != None:
                    post_dict = post.to_dict()
                    user_post.append(post_dict['post_id'])
        user_dict['post_id'] = user_post
        return user_dict

    @db_session
    @staticmethod
    def get_userinfo_by_id(primary_id):
        '''
            描述：根据用户id获取用户信息（包括密码）
            param：primary_id 用户名  主键
        '''
        dataInfo = {}
        result = UserEntity.get(user_id=primary_id, del_flag='0')
        if result:
            result = UserEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo



    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result