#coding: utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append(os.getcwd()+'/../utils')
import pymysql


def main():
    m = Mysql()
    #sql = sys.argv[1]
    #result = search(sql)
    #pprint(result) if len(result) > 0 else None
    #pprint(search(sys.argv[1]))

    # 备份指定的表，并将备份表的两份数据合回原表之一
    pass


class Mysql(object):
    # https://hub.docker.com/_/mysql
    # https://pymysql.readthedocs.io/en/latest/user/examples.html
    def __init__(self, config={}):
        host = config.get('host', 'localhost')
        port = config.get('port', '3306')
        user = config.get('user', 'root')
        passwd = config.get('passwd', '123456')
        db = config.get('db', 'mysql')
        charset = config.get('charset', 'utf8')
        self.conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def search(self, sql):
        count = self.cursor.execute(sql)
        result = self.cursor.fetchall()
        #return count, self.cursor
        return count, result

    def execute(self, sql):
        count = self.cursor.execute(sql)
        self.conn.commit()
        return count

    def close(self):
        self.cursor.close()
        self.conn.close()


def backup_tables():
    tables = search('show tables')[1]
    tables_list = [x[0] for x in tables]

    for table in tables_list:
        if '_bak' in table:
            continue

        new_table = table + '_bak'
        print execute('create table IF NOT EXISTS %s like %s' % (new_table, table))
        print execute('insert into %s (select * from %s)' % (new_table, table))


def restore_tables():
    tables = search('show tables')[1]
    tables_list = [x[0] for x in filter(lambda x: 'bak' in x[0], tables)]

    for table in tables_list:
        if 'new' not in table:
            new_table = table.replace('_bak', '').replace('_new', '') + '_new'
            copy_table(table, new_table)
            #print table, new_table, search('select count(*) from %s' % table), search('select count(*) from %s' % new_table)


def copy_table(original_table_name, new_table_name):
    fields = [x[0] for x in search('desc %s' % original_table_name)[1]][1:]
    return execute('insert ignore into %s (%s) select %s from %s' % (new_table_name, ','.join(fields), ','.join(fields), original_table_name))


if __name__ == '__main__':
    main()
