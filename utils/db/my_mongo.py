#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng at 16/6/16

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pymongo
import traceback

class Mongo(object):

    def __init__(self,config):
        # connect db
        dbhost, dbport, dbuser, dbpass , dbname, dbcoll= config['host'], config['port'], config['username'], config['password'], config.get('db', ''), config.get('collection', '')
        try:
            self.conn = pymongo.MongoClient(dbhost, dbport)
            if dbuser and dbpass:
                self.connected = self.db.authenticate(dbuser, dbpass)
            else:
                self.connected = True
            if dbname:
                self.db = self.conn[dbname]  # connect db
            if dbcoll:
                self.coll = self.db[dbcoll]
        except Exception:
            print dbhost, dbport, dbuser, dbpass, dbname, dbcoll
            print traceback.format_exc()
            print 'Connect Statics Database Fail.'
            sys.exit(1)

    def __del__(self):
        # disconnect db
        self.conn.close()

if __name__ == "__main__":
    conf_local = {
        'host':'localhost',
        'port':27017,
        'username':None,
        'password':None,
        #'db':'test',
        #'collection':'test'
    }
    mongo_local = Mongo(conf_local)
    results = mongo_local.conn['test']['test'].find({})
    for result in results:
        print result
    
