# -*- coding: utf-8 -*-
'''
    描述：数据库工厂类
    作者: chinacsj@139.com
    日期: 2024-02-04
'''
from pythonstyle.common import utils
from pony.orm import Database as DB
from pythonstyle.app import create_app
app = create_app()
class DbFactory:
    #数据库
    _database = {}

    @staticmethod
    def get_instance(datasource, sourcename = 'master'):
        '''
        描述：获取数据库对象
        :param datasource: 配置文件的数据库 目前只支持 mysql、oracle、postgre、sqlite
        :param sourcename: 配置文件的数据库分支 比如一个数据库有主从配置等也可能有多个数据库
        :return: 返回实例化的数据库对象
        '''
        datasource_config = DbFactory.get_datasource_config(datasource, sourcename)
        key = DbFactory.get_instance_key(datasource, sourcename, datasource_config)

        #print(key)
        if key not in DbFactory._database:
            db = DB()
            if datasource == 'mysql':
                #print(f"配置文件",datasource_config)
                db.bind(provider='mysql', host=datasource_config['host'], port=datasource_config['port'], user=datasource_config['user'], passwd=datasource_config['password'], db=datasource_config['db'])
            if datasource == 'sqlite':
                pos = datasource_config['filename'].find(":")
                if pos != -1:
                    db.bind(provider='sqlite', filename=datasource_config['filename'],create_db=datasource_config['create_db'])
                else:
                    db.bind(provider='sqlite', filename=datasource_config['filename'])
            if datasource == 'postgres':
                db.bind(provider='postgres', user=datasource_config['user'], password=datasource_config['password'], host=datasource_config['host'], database=datasource_config['database'])
            if datasource == 'oracle':
                db.bind(provider='oracle', user=datasource_config['user'], password=datasource_config['password'], dsn=datasource_config['dsn'])

            DbFactory._database[key] = db
        #print(DbFactory._database[key])
        return DbFactory._database[key]

    @staticmethod
    def get_datasource_config(datasource, sourcename = 'master'):
        '''
        描述：获取数据库配置文件信息并返回不同的数据库配置
        :param datasource: 配置文件的数据库 目前只支持 mysql、oracle、postgre、sqlite
        :param sourcename: 配置文件的数据库分支 比如一个数据库有主从配置等也可能有多个数据库
        :return: 返回datasource_config字典
        '''
        datasource_config = {}
        if datasource =='mysql':
            datasource_config['host'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['host']
            datasource_config['user'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['user']
            datasource_config['db'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['db']
            datasource_config['password'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['password']
            datasource_config['port'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['port']

        if datasource =='sqlite':
            datasource_config['filename'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['filename']
            pos = datasource_config['filename'].find(":")
            if pos != -1:
                datasource_config['create_db'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['create_db']

        if datasource =='postgres':
            datasource_config['host'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['host']
            datasource_config['user'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['user']
            datasource_config['database'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['database']
            datasource_config['password'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['password']
            datasource_config['port'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['port']

        if datasource =='oracle':
            datasource_config['dsn'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['dsn']
            datasource_config['user'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['user']
            datasource_config['password'] = app.config['runtime_config']['pythonstyle']['datasource'][datasource][sourcename]['password']

        return datasource_config

    @staticmethod
    def get_instance_key(datasource,sourcename,datasource_config):
        '''
        描述：返回数据库单例实例化的Key
        :param datasource: 配置文件的数据库 目前只支持 mysql、oracle、postgre、sqlite
        :param sourcename: 配置文件的数据库分支 比如一个数据库有主从配置等也可能有多个数据库
        :return key:返回key-MYSQL_127.0.0.1_master_db_student 表示唯一值
        '''
        key = ''
        if datasource == 'mysql':
            key = f"{utils.strToUper(datasource)}_{datasource_config['host']}_{sourcename}_{datasource_config['db']}"
        if datasource == 'sqlite':
            key = f"{utils.strToUper(datasource)}_{datasource_config['filename']}"
        if datasource == 'postgres':
            key = f"{utils.strToUper(datasource)}_{datasource_config['host']}_{sourcename}_{datasource_config['database']}"
        if datasource == 'oracle':
            key = f"{utils.strToUper(datasource)}_{datasource_config['dsn']}"
        return key

