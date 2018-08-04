#!/usr/bin/env python
#coding:utf-8
#Created by fsrm at 16/6/16

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../../libs')

import pymongo
import traceback


class Mongo(object):

    def __init__(self, config):
        # connect mongo_client
        # 由于mongo客户端本身是个连接池 所以直接返回client是更好的选择
        mongo_host, mongo_port, mongo_user, mongo_pass = \
            config['host'], config['port'], config['username'], config['password']
        self.conn = pymongo.MongoClient(mongo_host, mongo_port)
        #self.conn = pymongo.MongoClient("mongodb://%s:%s@%s:%s" % (mongo_user, mongo_pass, mongo_host, mongo_port))
        if mongo_user and mongo_pass:
            self.connected = self.conn.authenticate(mongo_user, mongo_pass)
        else:
            self.connected = True


    def get_db_names(self):
        return self.conn.database_names()


    def get_coll_names(self, db_name):
        return self.conn[db_name].collection_names()


    def find(self, db_name, coll_name, query):
        return self.conn[db_name][coll_name].find(query)


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
    }
    mongo_client_local = Mongo(conf_local)
#   res = mongo_client_local.conn['test']['test'].find({})

    print mongo_client_local.get_db_names()
    print mongo_client_local.get_coll_names('local')

    res = mongo_client_local.find('local', 'startup_log', {})
    print res.count()
    for result in res:
        print result
