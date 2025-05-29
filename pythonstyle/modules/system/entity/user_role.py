# -*- coding: utf-8 -*-
'''
    描述：用户实体类
    作者: chinacsj@139.com
    日期: 2024-02-08
'''
from pony.orm import *
from pythonstyle.config.db_config import DbFactory
from pythonstyle.common.utils import formatDate
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.role import RoleEntity

db = DbFactory.get_instance('mysql')

class UserRoleEntity(db.Entity):
    _table_ = 'sys_user_role'  # 设置表名
    user_id = Required(UserEntity,column='user_id')
    role_id = Required(RoleEntity,column='role_id')
    PrimaryKey(user_id,role_id)


    @db_session
    @staticmethod
    def get_user_role(user_id):
        '''
        描述：根据user_id获取用户的角色id
        param:user_id
        '''
        userRoleList = []
        for p in UserRoleEntity.select(lambda p: p.user_id == user_id):
            user_role = {'role_id': p.role_id, 'user_id': p.user_id}
            userRoleList.append(user_role)
        return userRoleList

    @db_session
    @staticmethod
    def get_role_user(role_id):
        '''
        描述：根据role_id获取用户id
        param:role_id
        '''
        roleUserInfo = UserRoleEntity.get(role_id=role_id)
        return roleUserInfo

    @db_session
    @staticmethod
    def add_data(param, role_ids):
        param['create_time'] = formatDate()
        try:
            last_id = db.insert(UserEntity, **param, returning='user_id')
            if len(role_ids) > 0 and last_id:
                for role_id in role_ids:
                    db.insert(UserRoleEntity, user_id=last_id, role_id=int(role_id))
            commit()
            return last_id
        except Exception as e:
            # 出现异常时回滚事务
            rollback()
            raise e
            return False

    @db_session
    @staticmethod
    def edit_data(param, role_ids):
        try:
            #先更新用户信息
            result = UserEntity[param['user_id']].set(**param)
            #删除角色信息
            delete_roles = db.execute("delete from sys_user_role where user_id = "+ str(param['user_id']))
            for role_id in role_ids:
                db.insert(UserRoleEntity, user_id=param['user_id'], role_id=int(role_id))
            commit()
            return True
        except Exception as e:
            # 出现异常时回滚事务
            rollback()
            raise e
            return False

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result