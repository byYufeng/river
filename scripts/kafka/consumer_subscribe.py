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
sys.path.append('./kafka-python-1.4.4')

import os, time
from kafka import KafkaProducer, KafkaConsumer


def main():
    topics = ['rainwind_test', 'rainwind_test2', 'rainwind_test3']
    kafka_configs = {
        'bootstrap_servers' : ['127.0.0.1:9092'], 
        'group_id' : 'g3'
    }
    consumer = KafkaConsumer(*topics, **kafka_configs)

    for msg in consumer:
        print 'Assignment:', consumer.assignment()
        print msg


if __name__ == "__main__":
    main()
