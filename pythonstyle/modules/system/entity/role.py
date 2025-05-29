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

class RoleEntity(db.Entity):
    _table_ = 'sys_role'  # 设置表名
    role_id = PrimaryKey(int, auto=True) #auto=True表示自增
    role_name = Required(str)
    listorder = Optional(int,default=1)
    data_scope = Optional(str, default='1')
    menu_check_strictly = Optional(int, default=1)
    dept_check_strictly = Optional(int, default=1)
    status = Required(str, default='0')
    del_flag = Optional(str, default='0')
    create_user = Optional(str, default='')
    create_time = Optional(str, default='')
    update_user = Optional(str, default='')
    update_time = Optional(str, default='')
    remark = Optional(str, default='')
    users = Set('UserRoleEntity')
    menus = Set('RoleMenuEntity')

    @db_session
    @staticmethod
    def get_role_list(param):
        roleList = []
        where = raw_sql("1 = 1")
        if param['status']:
            where = raw_sql("p.status = " + param['status'])
        roles = select(p for p in RoleEntity if p.del_flag != 1 and
                       param['role_name'] in p.role_name and where).order_by(desc(RoleEntity.listorder)).page(int(param['pageNum']), int(param['pageSize']))
        for p in roles:
            p = RoleEntity.formatDate(p)
            roleList.append(p.to_dict())
        return roleList

    @db_session
    @staticmethod
    def get_role_all_list():
        roleList = []
        roles = select(p for p in RoleEntity if p.del_flag != 1 and p.status != 1).order_by(desc(RoleEntity.listorder))
        for p in roles:
            p = RoleEntity.formatDate(p)
            roleList.append(p.to_dict())
        return roleList

    @db_session
    @staticmethod
    def get_roleinfo_by_id(primary_id):
        dataInfo = {}
        result = RoleEntity.get(role_id=primary_id, del_flag='0')
        if result:
            result = RoleEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo

    @db_session
    @staticmethod
    def get_rolelist_by_ids(role_ids):
        if len(role_ids) > 1:
            where = raw_sql("r.role_id in " + str(tuple(role_ids)))
        else:
            where = raw_sql("r.role_id = " + str(role_ids[0]))
        query = select(r for r in RoleEntity if where and r.del_flag == 0)[:]
        roleInfoList = []
        if roleInfoList != None:
            for role in query[:]:
                role = RoleEntity.formatDate(role)
                role_dict = role.to_dict(only=['role_id', 'role_name', 'data_scope'])
                roleInfoList.append(role_dict)
        return roleInfoList

    @db_session
    @staticmethod
    def get_count():
        countData = count(e for e in RoleEntity if e.del_flag == 0)
        return countData

    @db_session
    @staticmethod
    def edit_data(param):
        result = RoleEntity[param['role_id']].set(**param)
        # 更新成功 返回None 更新失败返回错误
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def get_role_menu_by_roleid(role_id):
        roleMenuIds = []
        query = left_join(
            (role.menus)
            for role in RoleEntity for rm in role.menus
            if raw_sql('rm.role_id = $role_id'))[:]

        if len(query) > 0:
            for role_menu_id in query[:]:
                data_list = role_menu_id.to_dict()
                roleMenuIds.append(data_list['menu_id'])

        return roleMenuIds


    @db_session
    @staticmethod
    def delete_by_id(role_id):
        if role_id == 1:
            return False
        result = RoleEntity[role_id].set(del_flag = '1')
        if result == None:
            return True
        else:
            return False

    @db_session
    @staticmethod
    def delete_by_ids(role_ids):
        for role_id in role_ids:
            result = RoleEntity[role_id].set(del_flag = '1')
        if result == None:
            return True
        else:
            return False

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result