#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask
from flask_bootstrap import Bootstrap
from views.home import home
from views.login import login
from views.personal import personal

from flask import request
import logging


def create_app():
    #register app and blueprint
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(login, url_prefix='/login')
    app.register_blueprint(personal, url_prefix='/personal')

    #add logger
    handler = logging.FileHandler('site.log', encoding='UTF-8')
    logging_formatter = logging.Formatter(\
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_formatter)
    app.logger.addHandler(handler)
    @app.after_request
    def add_log_handler(response):
        app.logger.info('client IP:%s'%request.remote_addr)
        return response


    Bootstrap(app)

    app.config['SECRET_KEY'] = 'dev_yufeng'

    #CsrfProtect(app)
    #csrf = CsrfProtect()
    #csrf.init_app(app)
    return app


if __name__ == '__main__':
    debug = True
    host = '0.0.0.0'
    port = 6080#6080 if len(sys.argv) < 2 else sys.argv[1]
    create_app().run(debug=debug, port=port, host=host)
