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


personal = Blueprint('personal', __name__)
#---------------上传、下载模块-------------------------
class UploadForm(Form):
    file = FileField('Please select a file')
    submit = SubmitField('确定上传')
 

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def folder_check(UPLOAD_FOLDER):
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

def file_check(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = os.path.join(os.getcwd(),'temp')
ALLOWED_EXTENSIONS = set(['txt','doc'])

folder_check(UPLOAD_FOLDER)

#上传页面和上传文件处理
@personal.route('/upload', methods=['GET', 'POST'])
def upload_file():
    upload_form = UploadForm()
    if upload_form.validate_on_submit():
        file = upload_form.file.data
        if file and file_check(file.filename):
            #secure_filename不支持中文
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return "Upload Success!</br></br>\
                   <a href=\"%s\">Click here to view download list</a>" %(url_for('personal.downloads'))
        return "Upload Failed!Sorry!Not supported font!"
    return render_template('personal.html', upload_form=upload_form)

#上传的文件列表
@personal.route('/downloads/')
def downloads():
    l = ['<li><a href="%s">%s</a></br>'%(url_for('personal.download', filename=filename), filename)\
            for filename in os.listdir(UPLOAD_FOLDER)]
    return '<html>%s</br></br>%s</html>'%(''.join(l), '<a href="%s">Click here to return</a>'%(url_for('personal.upload_file')))

#下载和浏览文件
@personal.route('/download/<filename>/')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ =='__main__':
    print os.getcwd()
