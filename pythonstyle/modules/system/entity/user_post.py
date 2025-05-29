# -*- coding: utf-8 -*-
'''
    描述：用户实体类
    作者: chinacsj@139.com
    日期: 2024-02-08
'''
from pony.orm import *
from pythonstyle.config.db_config import DbFactory
from pythonstyle.common.utils import formatDate
db = DbFactory.get_instance('mysql')
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.post import PostEntity

class UserPostEntity(db.Entity):
    _table_ = 'sys_user_post'  # 设置表名
    user_id = Required(UserEntity,column='user_id')
    post_id = Required(PostEntity,column='post_id')
    PrimaryKey(user_id,post_id)

    @db_session
    @staticmethod
    def get_user_post(user_id):
        '''
        描述：根据user_id获取用户的角色id
        param:user_id
        '''
        userPostList = []
        for p in UserPostEntity.select(lambda p: p.user_id == user_id):
            userPostList.append(p.to_dict())
        return userPostList

    @db_session
    @staticmethod
    def get_user_post(post_id):
        '''
        描述：根据post_id_id获取用户id
        param:post_id
        '''
        dataInfo = UserPostEntity.get(post_id=post_id)
        return dataInfo

    @db_session
    @staticmethod
    def add_data(user_id, post_ids):
        try:
            for post_id in post_ids:
                db.insert(UserPostEntity, user_id=user_id, post_id=int(post_id))
            return True
        except Exception as e:
            return False

    @db_session
    @staticmethod
    def edit_data(user_id, post_ids):
        try:
            #删除角色信息
            delete_roles = db.execute("delete from sys_user_post where user_id = "+ str(user_id))
            for post_id in post_ids:
                db.insert(UserPostEntity, user_id=user_id, post_id=int(post_id))
            return True
        except Exception as e:
            return False

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result