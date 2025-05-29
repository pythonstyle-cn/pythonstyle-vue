# -*- coding: utf-8 -*-
'''
    描述：框架入口
    作者: chinacsj@139.com
    日期: 2024-01-31
'''
from pythonstyle.libs.application import Application
from pythonstyle.app import create_app
from flask_cors import CORS
app = create_app()
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index(path):
    return Application.init()

if __name__ == '__main__':
    app.run(
        host = app.config['server']['host'],
        port = app.config['server']['port'],
        debug = app.config['server']['debug']
    )


