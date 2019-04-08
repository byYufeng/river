#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2018-12-24 15:47:31
Last modify: 2018-12-24 16:00:02
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../../riven/libs/python')
sys.path.append('../../riven/utils')

import os, time
from kafka import KafkaProducer, KafkaConsumer 
from db._redis import *
from common import multi_async


def main():
    # 经测试虽然用多进程打出的是同一个对象的地址 但速度的确快了很多
    multi_async(process, [None] * 4, 4)
    #process()
    

def process():
    kafka_configs = {
        'bootstrap_servers' : ['127.0.0.1:9092'], 
        'group_id' : 'g1',
    }
    consumer = KafkaConsumer(**kafka_configs)

    pika_config = {
        'host': '127.0.0.1',
        'port': '9221',
        'password': '',
        'db' : '0'
    }
    pika_client = REDIS_CLIENT(pika_config)

    consumer.subscribe(pattern='*')
    for msg in consumer:
        content = msg.value
        k, v = content.split('\t')
        pika_client.set(k, v)
        #print 'Assignment:', consumer.assignment()
        #print consumer, k
        print k


if __name__ == "__main__":
    main()
