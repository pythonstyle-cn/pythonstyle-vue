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

class TestEntity(db.Entity):
    _table_ = 'sys_test'  # 设置表名
    id = PrimaryKey(int, auto=True) #auto=True表示自增
    title = Optional(str, default='')
    dynamic_fields = Optional(Json, default={})

    @db_session
    def create_test():
        user = TestEntity(
            title='johndoe',
            dynamic_fields={
                'age': 30,
                'preferences': {
                    'theme': 'dark',
                    'notifications': True
                },
                'tags': ['customer', 'vip'],
                'registration_date': '2023-01-15'
            }
        )
        commit()
        return []

