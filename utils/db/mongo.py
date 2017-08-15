#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng at 16/6/16

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pymongo
import traceback

class Mongo(object):

    def __init__(self, config):
        # connect mongo_
        mongo_host, mongo_port, mongo_user, mongo_pass , mongo_db, mongo_coll = 
        config['host'], config['port'], config['username'], config['password'], config.get('db', ''), config.get('collection', '')
        try:
            self.conn = pymongo.MongoClient(mongo_host, mongo_port)
            #self.conn = pymongo.MongoClient("mongodb://%s:%s@%s" % mongo_user, mongo_pass, mongo_host+":"+mongo_port)
            if mongo_user and mongo_pass:
                self.connected = self.conn.authenticate(mongo_user, mongo_pass)
            else:
                self.connected = True

            if mongo_name:
                self.db = self.conn[mongo_name]  # connect mongo_
            if mongo_coll:
                self.coll = self.db[mongo_coll]
        except Exception:
            print mongo_host, mongo_port, mongo_user, mongo_pass, mongo_db, mongo_coll
            print traceback.format_exc()
            print 'Connect Database Fail.'
            sys.exit(1)

    def get_db_names(self):
        return self.conn.database_names()

    def get_coll_names(self, db):
        return self.conn[db].collection_names()

    def bulk(self, db, coll, data, bulk_size, op="insert"):
        try:
            bulk = self.conn[db][coll].initialize_unordered_bulk_op()
            for _data in data:
                bulk.insert(_data)
            bulk.execute()
        except pymongo.errors.BulkWriteError as e :
            print e.details
        except OverflowError as e :
            print e

    def __del__(self):
        # disconnect mongo_
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
