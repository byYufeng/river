#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Blueprint
from db.db_sqlite import db_get_conn as get_db

blog = Blueprint('blog', __name__)

#首页展示
@blog.route('/show')
def show_articles():
    db = get_db()
    cur = db.execute('select title, text, author from articles order by id desc')
    articles = [dict(title=row[0], text=row[1], author=row[2]) for row in cur.fetchall()]
    return render_template('show_articles.html', articles=articles)

#检查登录状态并添加文章
@blog.route('/add', methods=['POST'])
def add_article():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    title, text, author = request.form['title'], request.form['text'], session.get('logged_in')
    db.execute('insert into articles (title, text, author) values (?, ?, ?)', [title, text, author])
    db.commit()
    flash('New article has been successfully published')
    return redirect(url_for('show_articles'))


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

