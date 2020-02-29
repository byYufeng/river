#! coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import MySQLdb

class Mysql(object):
    def __init__(self,host='localhost',port=3306,user='',passwd='',db_name=''):
        #super(mysql, self).__init__()
        self.conn = MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=db_name,charset='utf8')
        self.cursor =self.conn.cursor()

    def get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def select(self,sql):
        count=self.cursor.execute(sql)
        return count,self.cursor

    def update(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
