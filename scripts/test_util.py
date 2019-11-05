#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-31 19:35:21
Last modify: 2018-12-09 02:54:02
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../libs/python')
sys.path.append('..')


import os, time
import traceback, json


def test_mq():
    from utils.middleware._rabbitmq import RMQ_PRODUCER
    from utils.middleware._rabbitmq import RMQ_CONSUMER
    
    rmq_config = { 
        'host' : '127.0.0.1',
        'port' : '5672', 
        'username' : 'guest', 
        'password' : 'guest',
        'vhost' : '/',
        'exchange_name' : '', 
        'exchange_type' : '', 
        'queue_name' : 'fsrm_test',
        'routing_key' : 'fsrm_test'
    }  

    rmq_producer = RMQ_PRODUCER(rmq_config)
    rmq_producer.publish('hahaha\t gogogo')

    rmq_consumer = RMQ_CONSUMER(rmq_config)
    def callback(msg):
        print msg
    rmq_consumer.consume(callback)


def test_redis():
    from utils.db._redis import REDIS_CLIENT
    redis_config = { 
        'host':'127.0.0.1',
        'port':9221,
        'db': 0,
        'connections':100
    }   
    
    redis_client = REDIS_CLIENT(redis_config)
    redis_client.set('name', 'laozhang')
    print redis_client.get('name')
    print redis_client.delete('name')
    print redis_client.get('name') 


def test_mongo():
    from utils.db._mongo import Mongo
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


def test_batch():
    from utils.common import batch
    l = [x for x in range(95)] 

    def printt(data):
        print data

    batch(printt, l, 10)
    #batch(printt, sys.stdin, 10)


def main():
    test_batch()
    #test_redis()


if __name__ == "__main__":
    main()
