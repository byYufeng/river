#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from flask import Blueprint
from flask import url_for, send_from_directory, render_template, flash, redirect, request
from werkzeug import secure_filename
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required
#from flask_wtf.csrf import CsrfProtect

home = Blueprint('home', __name__)


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

@home.route('/', methods=('GET', 'POST'))
def homepage():
    custom_form = CustomForm()
    #custom_form.validate_on_submit()  # to get error messages to the browser
    #flash('error message', 'error')
    #flash('info message', 'info')
    #flash('debug message', 'debug')
    #flash('different message', 'different')
    #flash('uncategorized message')
    return render_template('home.html', custom_form=custom_form)

@home.route('/personal', methods=('GET', 'POST'))
def personal():
    return redirect('/personal/upload')

@home.route('/deal', methods=('GET', 'POST'))
def deal():
    params = {}
    for k, v in request.form.items():
        print k, v
        params[''.join(k.split('-', 1)[1:]) if '-' in k else k] = v
    url = params.get('url','bad_url') + params.get('params','bad_parms')
    return redirect(url)
