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

class OperationLogEntity(db.Entity):
    _table_ = 'sys_operation_log'  # 设置表名
    id = PrimaryKey(int, auto=True) #auto=True表示自增
    title = Required(str)
    business_type = Optional(str, default='0')
    method = Optional(str, default='')
    request_method = Optional(str, default='')
    op_type = Optional(str, default='')
    op_name = Optional(str, default='')
    dept_name = Optional(str, default='')
    op_url = Optional(str, default='0')
    op_ip = Optional(str, default='')
    op_location = Optional(str, default='')
    op_param = Optional(str, default='')
    json_result = Optional(str, default='')
    status = Optional(str, default='')
    error_msg = Optional(str, default='')
    create_time = Optional(str, default='')

    @db_session
    @staticmethod
    def get_data_list(param):
        dataList = []
        where = raw_sql(" 1 = 1 ")
        if param['status']:
            where = raw_sql("p.status = " + param['status'])
        result = select(p for p in OperationLogEntity if param['title'] in p.title and where).order_by(
            desc(OperationLogEntity.id)).page(int(param['pageNum']), int(param['pageSize']))
        for p in result:
            p = OperationLogEntity.formatDate(p)
            dataList.append(p.to_dict())
        return dataList


    @db_session
    @staticmethod
    def get_count(param):
        where = raw_sql('1 = 1')
        if param['status']:
            where = raw_sql("e.status = " + param['status'])
        countData = count(e for e in OperationLogEntity if where)
        return countData

    @db_session
    @staticmethod
    def get_datainfo_by_id(primary_id):
        dataInfo = {}
        result = OperationLogEntity.get(id=primary_id)
        if result:
            result = OperationLogEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo

    @db_session
    @staticmethod
    def add_data(param):

        param['create_time'] = formatDate()
        last_id = db.insert(OperationLogEntity, **param, returning='id')
        if last_id > 0:
            return last_id
        else:
            return False

    @staticmethod
    def formatDate(result):
        if result.create_time != None and type(result.create_time) != str:
            result.create_time = formatDate(result.create_time)
        return result