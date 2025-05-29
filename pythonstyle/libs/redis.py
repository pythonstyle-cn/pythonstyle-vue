# -*- coding: utf-8 -*-
'''
    描述：操作redis数据库客户端
    作者: chinacsj@139.com
    日期: 2024-02-14
'''
import redis
from pythonstyle.app import create_app
app = create_app()

import redis
import logging


class Redis:
    _redis_pool = None

    def __init__(self):
        # 获取 Redis 配置
        self.redis_cfg = self.get_redis_config()

        # 确保连接池只创建一次
        if self._redis_pool is None:
            self._create_connection_pool()

        # 创建 Redis 连接客户端，使用连接池 默认为 1 数据库
        self.redis_conn = redis.Redis(connection_pool=self._redis_pool, db=self.redis_cfg.get('database', 1))

    def _create_connection_pool(self):
        """
        创建 Redis 连接池，支持密码等配置。
        """
        try:
            self._redis_pool = redis.ConnectionPool(
                host=self.redis_cfg['host'],
                port=self.redis_cfg['port'],
                password=self.redis_cfg.get('password', None),  # 如果有密码，传递
                max_connections=self.redis_cfg.get('max_connections', 50),  # 默认最大连接数
                decode_responses=False  # 默认关闭解码
            )
        except redis.exceptions.ConnectionError as e:
            logging.error(f"Redis connection error: {e}")
            raise  # 抛出异常让调用者处理
        except Exception as e:
            logging.error(f"Error creating Redis connection pool: {e}")
            raise


    def set(self, key, value, expire=None):
        '''
        描述：设置键值对，可以用于缓存数据、存储会话信息
        :param key (str): 键名
        :param value: 值
        :param expire: 过期时间（秒）. Defaults to None.
        '''
        self.redis_conn.set(key, value, ex=expire)

    def get(self, key):
        '''
        描述：用于获取键对应的值，可以用于获取缓存数据、读取会话信息
        :param key (str): 键名
        :return: 值
        '''
        ttl = self.redis_conn.ttl(key)
        if ttl == -2:
            return "已过期或不存在!"
        return self.redis_conn.get(key)

    def delete(self, key):
        '''
        描述：用于删除指定的键，可以用于删除缓存数据、清除会话信息
        :param key:键名
        :return:
        '''
        self.redis_conn.delete(key)

    def lpush(self, key, *values):
        '''
        描述：向列表的左侧插入一个或多个元素，可以用于构建消息队列、实现最近访问列表等
        :param key:列表键
        :param values:要插入的元素
        '''
        self.redis_conn.lpush(key, *values)

    def rpush(self, key, *values):
        '''
        描述：用于向列表的右侧插入一个或多个元素，同样适用于构建消息队列、实现最近访问列表等
        :param key:列表键
        :param values:要插入的元素
        '''
        self.redis_conn.rpush(key, *values)

    def lrange(self, key, start, end):
        '''
        描述：用于获取列表指定范围内的元素，可以用于获取分页数据、获取最近访问列表等
        :param key:列表键名
        :param start:起始索引
        :param end:结束索引
        :return:列表元素
        '''
        return self.redis_conn.lrange(key, start, end)

    def hset(self, key, field, value):
        '''
        描述：用于给哈希表中指定字段设置值，可以用于存储对象属性、存储用户信息等
        :param key:哈希表键名
        :param field:字段名
        :param value:字段值
        '''
        self.redis_conn.hset(key, field, value)

    def hget(self, key, field):
        '''
        描述：用于获取哈希表中指定字段的值，可以用于获取对象属性、获取用户信息等
        :param key:哈希表键名
        :param field:字段名
        :return:字段值
        '''
        return self.redis_conn.hget(key, field)

    def hdel(self, key, field):
        '''
        描述：用于删除哈希表中指定字段的值，可以用于获取对象属性、获取用户信息等
        :param key:哈希表键名
        :param field:字段名
        '''
        return self.redis_conn.hdel(key, field)

    def hdetall(self,key):
        '''
        描述：用于获取所有hset哈希表中指定字段的值，可以用于获取对象属性、获取用户信息等
        :param key:哈希表键名
        :return field:字段和值
        '''
        return self.redis_conn.hgetall(key)

    def hmset(self, key, mapping):
        '''
        描述：用于在哈希表中批量设置字段和值，可以用于一次性设置对象的多个属性、一次性存储用户的多个信息等
        :param key:哈希表键名
        :param mapping:字段和对应值的映射关系
        '''
        self.redis_conn.hmset(key, mapping)

    def hmget(self, key, fields):
        '''
        描述：用于在哈希表中批量获取字段的值，可以用于一次性获取对象的多个属性、一次性获取用户的多个信息等
        :param key:哈希表键名
        :param fields:字段列表
        :return: 字段值列表
        '''
        return self.redis_conn.hmget(key, fields)

    def sadd(self, key, *members):
        '''
        描述：用于向集合中添加一个或多个成员，可以用于存储用户标签、实现好友关系等
        :param key:集合键名
        :param members:要添加的成员
        '''
        self.redis_conn.sadd(key, *members)

    def smembers(self, key):
        '''
        描述：用于获取集合中的所有成员，可以用于获取用户的所有标签、获取好友列表等
        :param key:集合键名
        :return:成员集合
        '''
        return self.redis_conn.smembers(key)

    @staticmethod
    def get_redis_config():
        '''
        描述：获取yml中的redis配置文件内容
        :return: redis_config 字典
        '''
        redis_config = {}
        redis_config['host'] = app.config['runtime_config']['pythonstyle']['datasource']['redis']['host']
        redis_config['database'] = app.config['runtime_config']['pythonstyle']['datasource']['redis']['database']
        redis_config['password'] = app.config['runtime_config']['pythonstyle']['datasource']['redis']['password']
        redis_config['port'] = app.config['runtime_config']['pythonstyle']['datasource']['redis']['port']
        return redis_config