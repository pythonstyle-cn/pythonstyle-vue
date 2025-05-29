# -*- coding: utf-8 -*-
import os
from flask import Flask,session

from pythonstyle.config.configure import Configure
from pythonstyle.common import utils

@Configure
def create_app(cfg):
    '''
    描述：创建应用app对象
    :param cfg:读取application.yml配置文件
    :return: 返回Flask对象app
    '''
    #项目根目录
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    #静态文件目录
    static_folder_dir = root_dir+'/static'
    #模板目录
    template_folder_dir = root_dir+'/resources/templates'

    app = Flask(__name__, root_path = root_dir, static_folder = static_folder_dir, template_folder = template_folder_dir)

    app.config['server'] = cfg['server']
    app.config['captchaEnabled'] = cfg['captcha']['captchaEnabled']
    app.config['log'] = cfg['log']
    app.config['runtime_config'] = cfg

    # 开启session
    app.secret_key = 'pythonstyle-vue3'
    return app

