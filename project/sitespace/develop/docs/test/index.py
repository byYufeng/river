#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask
from flask_bootstrap import Bootstrap

from flask import render_template

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app
     

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=6680)

