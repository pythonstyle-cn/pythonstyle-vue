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
from pythonstyle.modules.system.entity.role import RoleEntity
from pythonstyle.modules.system.entity.menu import MenuEntity

class RoleMenuEntity(db.Entity):
    _table_ = 'sys_role_menu'  # 设置表名
    role_id = Required(RoleEntity,column='role_id')
    menu_id = Required(MenuEntity,column='menu_id')
    PrimaryKey(role_id, menu_id)

    @db_session
    @staticmethod
    def get_role_menu_list(param):
        roleMenuList = []
        for p in RoleMenuEntity.select(lambda p: p.role_id == param['role_id']).order_by(desc(RoleMenuEntity.role_id)):
            roleMenuList.append(p.to_dict(only=['role_id', 'menu_id']))
        return roleMenuList

    @db_session
    @staticmethod
    def add_data(param, menu_ids):
        try:
            param['create_time'] = formatDate()
            last_id = db.insert(RoleEntity, **param, returning='role_id')
            if len(menu_ids) > 0 and last_id:
                for menu_id in menu_ids:
                    db.insert(RoleMenuEntity, role_id=last_id, menu_id=int(menu_id))
            commit()
            return last_id
        except Exception as e:
            # 出现异常时回滚事务
            rollback()
            raise e
            return False

    @db_session
    @staticmethod
    def edit_data(param, menu_ids):
        try:
            #先更新用户信息
            result = RoleEntity[param['role_id']].set(**param)
            #删除角色信息
            delete_menus = db.execute("delete from sys_role_menu where role_id = "+ str(param['role_id']))
            for menu_id in menu_ids:
                db.insert(RoleMenuEntity, role_id=param['role_id'], menu_id=int(menu_id))
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



