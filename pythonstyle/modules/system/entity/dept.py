# -*- coding: utf-8 -*-
'''
    描述：岗位实体类
    作者: chinacsj@139.com
    日期: 2024-02-08
'''
from pony.orm import *
from pythonstyle.common.utils import formatDate
from pythonstyle.config.db_config import DbFactory
db = DbFactory.get_instance('mysql')

class DeptEntity(db.Entity):
    _table_ = 'sys_dept'  # 设置表名
    dept_id = PrimaryKey(int, auto=True) #auto=True表示自增
    parent_id = Required(int)
    path = Optional(str, default='')
    dept_name = Optional(str, default='')
    leader = Optional(str)
    phone = Optional(str)
    email = Optional(str)
    status = Optional(str, default='0')
    del_flag = Optional(str, default='0')
    listorder = Optional(int, default=0)
    create_user = Optional(str, default='')
    create_time = Optional(str, default='')
    update_user = Optional(str, default='')
    update_time = Optional(str, default='')

    @db_session
    @staticmethod
    def get_data_list():
        dataList = []
        result = select(p for p in DeptEntity if p.del_flag =='0')
        for p in result:
            p = DeptEntity.formatDate(p)
            dataList.append(p.to_dict())
        return dataList

    @db_session
    @staticmethod
    def get_datainfo_by_id(primary_id):
        dataInfo = {}
        result = DeptEntity.get(dept_id=primary_id, del_flag='0')
        if result:
            result = DeptEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo

    @db_session
    @staticmethod
    def get_datalist_by_ids(primary_ids):
        if len(primary_ids) > 1:
            where = raw_sql("r.dept_id in " + str(tuple(primary_ids)))
        else:
            where = raw_sql("r.dept_id = " + str(primary_ids[0]))
        result = select(r for r in DeptEntity if where and  r.del_flag == 0)[:]
        dataList = []
        if dataList != None:
            for item in result[:]:
                data_dict = item.to_dict()
                dataList.append(data_dict)
        return dataList

    @db_session
    @staticmethod
    def get_count():
        countData = count(e for e in DeptEntity if e.del_flag == 0)
        return countData

    @db_session
    @staticmethod
    def add_data(param):
        param['create_time'] = formatDate()
        last_id = db.insert(DeptEntity, **param, returning='dept_id')
        if last_id > 0:
            return last_id
        else:
            return False

    @db_session
    @staticmethod
    def edit_data(param):
        result = DeptEntity[param['dept_id']].set(**param)
        # 更新成功 返回None 更新失败返回错误
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def delete_by_id(id):
        result = DeptEntity[id].set(del_flag = '1')
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def delete_by_ids(post_ids):
        for id in post_ids:
            result = DeptEntity[id].set(del_flag = '1')
        if result:
            return False
        else:
            return True

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        if result.update_time != None and type(result.update_time) != str:
            result.update_time = formatDate(result.update_time)
        return result

    @db_session
    @staticmethod
    def has_children(dept_id):
        countData = count(e for e in DeptEntity if e.parent_id == dept_id and e.del_flag != '1')
        return countData