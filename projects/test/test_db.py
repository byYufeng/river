#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-05 00:42:10
Last modify: 2018-08-05 00:54:10
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../..')

import os, time
import traceback, json


def test_mongo():
    from utils.db.mongo import Mongo
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


def main():
    test_mongo()
     

if __name__ == "__main__":
    main()
