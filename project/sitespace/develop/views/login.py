#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Blueprint, session, flash, redirect, url_for
from flask import request, render_template
from db.db_sqlite import db_get_conn as get_db

login = Blueprint('login', __name__)
#登录
@login.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        db = get_db()
        username = request.form['username'] 
        password = request.form['password'] 
        cur = db.execute('select username, password from users where username=?', [username])
        result = cur.fetchall()
        if result:
            PASSWORD = result[0][0]
            if password == PASSWORD:
                session['logged_in'] = username
                flash('Logged in...')
                return redirect(url_for('home.index'))
            else:
                error = 'Invalid password'
                return render_template('sign_in.html', error=error)
        else:
            error = 'Invalid username'
            return render_template('sign_in.html', error=error)
    return render_template('sign_in.html', error=error)

#注册
@login.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        db = get_db()
        username = request.form['username'] 
        password = request.form['password'] 
        REpassword = request.form['REpassword']
        if password != REpassword:
            error = "The password you typed twice is different!"
            return render_template('sign_up.html', error=error)

        cur = db.execute('select username, password from users where username=?', [username])
        result = cur.fetchall()
        if result:
            error = 'The username has been signed!'
            return render_template('sign_up.html', error=error)
        else:
            db.execute('insert into users (username, password) values (?, ?)', [username, password])
            db.commit()
            session['logged_in'] = username
            #flash('Sign up successfully and auto logged in...')
            return redirect(url_for('home.homepage'))
    return render_template('sign_up.html', error=error)

#登出
@login.route('/sign_out', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home.homepage'))

if __name__ == "__main__":
    #app.config.from_envvar('aa', silent=True)
    app.config.update(
        DATABASE = 'baiyufff.db',
        USERNAME = 'baiyufff',
        PASSWORD = 'baiyufff'
    )
    #若使用session(cookie) 必须设置secret_key
    app.secret_key = os.urandom(24)
    #init_db()
    app.debug = True
    app.run('0.0.0.0')

