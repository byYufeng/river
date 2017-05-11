#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, sqlite3

database = 'mysitespace.db'

def db_get_conn(database=database):
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    conn.text_factory = str
    return conn

def init_db(database):
    db = db_get_conn(database)
    with open('schema.sql', mode='r') as fin:
        cursor = db.cursor()
        cursor.executescript(fin.read())
    db.commit()

if __name__ == "__main__":
    init_db(database)
    #模块使用的db其实是在..下 需修正
    print 'init db ok!'

