#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = './upload_files'
ALLOWED_EXTENSIONS = set(['txt','doc'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

def file_check(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

html = '''
<!doctype html>
<form action="" method=post enctype=multipart/form-data>
    <input type=file name=file> 
    <input type=submit value=Upload>
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print file_check(file.filename)
        if file and file_check(file.filename):
            #secure_filename不支持中文
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Success!"
        return "Sorry!Do not support this file font!"
    return html

@app.route('/downloads')
def downloads():
    l = ['<a href="/download/%s">%s</a><br>'%(filename, filename) for filename in os.listdir(UPLOAD_FOLDER)]
    return '''
        <html>
            %s
        <html>
    '''%''.join(l)

#redirect(url_for('uploaded_file', filename=filename))
@app.route('/download/<filename>')
def preview_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
