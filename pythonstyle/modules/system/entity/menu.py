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

class MenuEntity(db.Entity):
    _table_ = 'sys_menu'  # 设置表名
    menu_id = PrimaryKey(int, auto=True)
    menu_name = Required(str)
    parent_id = Required(int, default=0)
    listorder = Optional(int, default=0)
    path = Optional(str, default='')
    component = Optional(str)
    query = Optional(str)
    is_link = Required(int, default=0)
    is_cache = Optional(int, default=0)
    menu_type = Optional(str, default='')
    visible = Optional(str, default='0')
    status = Optional(str, default='0')
    perms = Optional(str)
    icon = Optional(str, default='#')
    create_user = Optional(str, default='')
    create_time = Optional(str, default='')
    update_user = Optional(str, default='')
    update_time = Optional(str)
    remark = Optional(str, default='')
    roles = Set('RoleMenuEntity')

    @db_session
    @staticmethod
    def get_menu_list():
        menuList = []
        for p in MenuEntity.select().order_by(MenuEntity.listorder):
            p = MenuEntity.formatDate(p)
            menuList.append(p.to_dict())
        return menuList

    @db_session
    @staticmethod
    def get_datainfo_by_id(primary_id):
        dataInfo = {}
        result = MenuEntity.get(menu_id=primary_id)
        if result:
            result = MenuEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo

    @db_session
    @staticmethod
    def get_role_menu_by_roleids(role_ids):
        #set_sql_debug(True)
        role_ids_str = ', '.join(str(id) for id in role_ids)
        # 如果是超级管理员 直接获取全部菜单
        if 1 in role_ids:
           return MenuEntity.get_menu_list()
        else:
            raw_sql('rm.role_id in ('+ role_ids_str +')')
        roleMenuInfo = []
        query = left_join(
            (menu)
            for menu in MenuEntity for rm in menu.roles
            if raw_sql('rm.role_id in ('+ role_ids_str +')'))[:]
        if len(query) > 0:
            for menu in query[:]:
                menu = MenuEntity.formatDate(menu)
                menu_dict = menu.to_dict()
                roleMenuInfo.append(menu_dict)

        return roleMenuInfo

    @db_session
    @staticmethod
    def get_role_menu_permission(role_id, perms):
        if len(role_id) > 1:
            where = raw_sql("rm.role_id in " + str(tuple(role_id)) + " and menu.perms = $perms")
        else:
            where = raw_sql("rm.role_id = " + str(role_id[0]) + " and menu.perms = $perms")
        query = left_join(
            (menu)
            for menu in MenuEntity for rm in menu.roles
            if where)[:]

        if len(query) > 0:
            return True
        return False

    @db_session
    @staticmethod
    def get_count():
        countData = count( e for e in MenuEntity)
        return countData

    @db_session
    @staticmethod
    def add_data(param):
        param['create_time'] = formatDate()
        last_id = db.insert(MenuEntity, **param, returning='menu_id')
        if last_id > 0:
            return last_id
        else:
            return False

    @db_session
    @staticmethod
    def edit_data(param):
        result = MenuEntity[param['menu_id']].set(**param)
        # 更新成功 返回None 更新失败返回错误
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def delete_by_id(id):
        result = MenuEntity[id].delete()
        # 删除成功返回None
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def has_children(menu_id):
        countData = count(e for e in MenuEntity if e.parent_id == menu_id)
        return countData

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result