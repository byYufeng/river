#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask
from flask_bootstrap import Bootstrap

from flask import url_for, send_from_directory, render_template, flash, redirect, request
from werkzeug import secure_filename
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required
#from flask_wtf.csrf import CsrfProtect

class CustomModuleForm(Form):
    name = TextField('Name', [validators.required()])
    url = TextField('Url', [validators.required()])
    params = TextField('Params')
    submit = SubmitField('Add')

google_image='https://g.starmoe.xyz/search?q='
class GoogleImageForm(Form):
    name = TextField('Name', [validators.required()], default='Google Image')
    url = TextField('Url', [validators.required()], default=google_image)
    params = TextField('Params')
    submit = SubmitField('Search')

lagou='https://www.lagou.com'
class LagouForm(Form):
    name = TextField('Name', [validators.required()], default='拉勾')
    url = TextField('Url', [validators.required()], default=lagou)
    params = TextField('')
    submit = SubmitField('Enter')

douban='https://www.douban.com'
class DoubanForm(Form):
    name = TextField('Name', [validators.required()], default='豆瓣')
    url = TextField('Url', [validators.required()], default=douban)
    params = TextField('')
    submit = SubmitField('Enter')


class UploadForm(Form):
    file = FileField('Please select a file')
    submit = SubmitField('确定上传')

class CustomForm(Form):
    google = FormField(GoogleImageForm)
    lagou = FormField(LagouForm)
    douban = FormField(DoubanForm)

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = 'dev_yufeng'

    #CsrfProtect(app)
    #csrf = CsrfProtect()
    #csrf.init_app(app)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        custom_form = CustomForm()
        #custom_form.validate_on_submit()  # to get error messages to the browser
        #flash('error message', 'error')
        #flash('info message', 'info')
        #flash('debug message', 'debug')
        #flash('different message', 'different')
        #flash('uncategorized message')
        return render_template('index.html', custom_form=custom_form)

    @app.route('/matters', methods=('GET', 'POST'))
    def matters():
        return redirect('/upload')

    @app.route('/deal', methods=('GET', 'POST'))
    def deal():
        params = {}
        for k, v in request.form.items():
            print k, v
            params[''.join(k.split('-', 1)[1:]) if '-' in k else k] = v
        url = params.get('url','bad_url') + params.get('params','bad_parms')
        return redirect(url)

    #---------------上传、下载模块-------------------------


    UPLOAD_FOLDER = './upload_files'
    ALLOWED_EXTENSIONS = set(['txt','doc'])

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

    def file_check(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        upload_form = UploadForm()
        if upload_form.validate_on_submit():
            file = upload_form.file.data
            if file and file_check(file.filename):
                #secure_filename不支持中文
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return "Upload Success!"
            return "Upload Failed!Sorry!Not supported font!"
        return render_template('matters.html', upload_form=upload_form)

    @app.route('/downloads/')
    def downloads():
        l = ['<li><a href="/download/%s/">%s</a></br>'%(filename, filename) for filename in os.listdir(UPLOAD_FOLDER)]
        return '<html>%s</html>'%''.join(l)

    @app.route('/download/<filename>/')
    def download(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    '''
    @csrf.error_handler
    def csrf_error(reason):
        return str(reason)
    '''

    return app


if __name__ == '__main__':
    debug = False#True
    host = '0.0.0.0'
    port= 6080 if len(sys.argv) < 2 else sys.argv[1]
    create_app().run(debug=debug, port=port, host=host)
