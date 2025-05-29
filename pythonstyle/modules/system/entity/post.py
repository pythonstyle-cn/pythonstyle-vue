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

class PostEntity(db.Entity):
    _table_ = 'sys_post'  # 设置表名
    post_id = PrimaryKey(int, auto=True) #auto=True表示自增
    post_code = Required(str)
    post_name = Required(str)
    listorder = Optional(int,default=1)
    status = Required(str, default='0')
    create_user = Optional(str, default='')
    create_time = Optional(str, default='')
    update_user = Optional(str, default='')
    update_time = Optional(str, default='')
    remark = Optional(str, default='')
    posts = Set('UserPostEntity')

    @db_session
    @staticmethod
    def get_data_list(param):
        dataList = []
        where = raw_sql("1 = 1")
        if param['status']:
            where = raw_sql("p.status = "+param['status'])
        result = select(p for p in PostEntity if
                       param['post_name'] in p.post_name and where).order_by(desc(PostEntity.listorder)).page(int(param['pageNum']), int(param['pageSize']))
        for p in result:
            if p.create_time != None or p.update_time != None:
                p = PostEntity.formatDate(p)
            dataList.append(p.to_dict())
        return dataList

    @db_session
    @staticmethod
    def get_post_all_list():
        dataList = []
        result = select(p for p in PostEntity if p.status != '1').order_by(desc(PostEntity.listorder))
        for p in result:
            dataList.append(p.to_dict(exclude=['create_time','update_time']))
        return dataList

    @db_session
    @staticmethod
    def get_datainfo_by_id(primary_id):
        dataInfo = {}
        result = PostEntity.get(post_id=primary_id)
        if result:
            result = PostEntity.formatDate(result)
            dataInfo = result.to_dict()
        return dataInfo

    @db_session
    @staticmethod
    def get_datalist_by_ids(primary_ids):
        if len(primary_ids) > 1:
            where = raw_sql("r.post_id in " + str(tuple(primary_ids)))
        else:
            where = raw_sql("r.post_id = " + str(primary_ids[0]))
        result = select(r for r in PostEntity if where)[:]
        dataList = []
        if dataList != None:
            for item in result[:]:
                data_dict = item.to_dict()
                dataList.append(data_dict)
        return dataList

    @db_session
    @staticmethod
    def get_count():
        countData = count(e for e in PostEntity)
        return countData

    @db_session
    @staticmethod
    def add_data(param):
        param['create_time'] = formatDate()
        last_id = db.insert(PostEntity, **param, returning='post_id')
        if last_id > 0:
            return last_id
        else:
            return False

    @db_session
    @staticmethod
    def edit_data(param):

        result = PostEntity[int(param['post_id'])].set(**param)
        # 更新成功 返回None 更新失败返回错误
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def delete_by_id(id):
        result = PostEntity[id].delete()
        # 删除成功返回None
        if result:
            return False
        else:
            return True

    @db_session
    @staticmethod
    def delete_by_ids(ids):
        for id in ids:
            result = PostEntity[id].delete()
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