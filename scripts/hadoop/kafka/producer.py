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
    topic = 'rainwind_test'
    kafka_configs = { 
        'bootstrap_servers' : ['127.0.0.1:9092'], 
        'linger_ms' : 0
    } 
    producer = KafkaProducer(**kafka_configs)
    
    #print 'topic partitions:', topic, producer.partitions_for(topic)
    for _ in range(3):
        producer.send(topic, value='hahah', key='20181226')
        #producer.send(topic, value='hahah', key='20181226', headers=[('name','test'), ('author','rainwind')])
        #producer.send(topic, value='hahah')
        #producer.send(topic, key='20181226')
    producer.flush()


if __name__ == "__main__":
    main()
