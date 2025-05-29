# -*- coding: utf-8 -*-
import yaml
import os
from pythonstyle.common.utils import merge_configs
'''
    描述：配置文件装饰器 用于启动到时候读取配置文件
    作者: <insert author name here>
    日期: 2024-01-31
'''

def Configure(func):
    '''
    描述：定义配置文件装饰器 当配置有['pythonstyle']['profiles']['active'] 这个值时，合并两个配置文件
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        sep = os.sep
        #项目根路径
        root_path = os.getcwd()
        #项目框架路径
        thinkpython_path = os.getcwd() + sep + 'pythonstyle'
        with open(file=root_path + sep + 'resources'+ sep +'application.yml', mode="r", encoding='utf-8') as file:
            cfg = yaml.safe_load(file)

        cfg['sep'] = sep
        cfg['root_path'] = root_path
        cfg['thinkpython_path'] = thinkpython_path

        if cfg['pythonstyle']['profiles']['active'] != None:
            config_env = f"application-{cfg['pythonstyle']['profiles']['active']}.yml"
            with open(file=root_path + sep + 'resources'+ sep + config_env, mode='r', encoding='utf-8') as config_env_file:
                runtime_config = yaml.safe_load(config_env_file)
                cfg = merge_configs(cfg, runtime_config)

        #print(f"读取的配置文件--》{cfg}")
        return func(cfg, *args, **kwargs)
    return wrapper

