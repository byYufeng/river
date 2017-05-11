#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_yufeng'

    @app.route('/')
    def hello():
        return 'hello thank you for votes! please enter your number:<input></input>'

    return app

if __name__ == '__main__':
    debug = True
    host = '0.0.0.0'
    port = 4321#6080 if len(sys.argv) < 2 else sys.argv[1]
    create_app().run(debug=debug, port=port, host=host)
