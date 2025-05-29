# -*- coding: utf-8 -*-
'''
    描述：数据库实例对象返回
    作者: chinacsj@139.com
    日期: 2024-02-08
'''
from pythonstyle.libs.db_factory import DbFactory

def create_db(type):
    db = DbFactory.get_instance(type)
    return db
