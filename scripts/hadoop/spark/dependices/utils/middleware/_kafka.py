#! /usr/bin/env python
# coding:utf-8
"""
Author: fsrm
Create Time: 2019-06-13 17:24:29
Last modify: 2019-06-13 17:24:29
"""

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import json, time, traceback
from datetime import datetime

from kafka import KafkaProducer, KafkaConsumer 


class KAFKA_PRODUCER(object):
    def __init__(self, config):
        servers = config.get('servers', ['127.0.0.1:9092'])
        topic = config.get('topic', 'rainwind_topic_test')

        kafka_configs = { 
            'bootstrap_servers': servers,
            'linger_ms' : 0 
        }   
        self.producer = KafkaProducer(**kafka_configs)
    
    def publish(self, message, key=None, **kwargs)
        self.producer.send(topic, value=message, key=key)
        self.producer.flush()

    def get_partitions(self):
        return self.producer.partitions_for(topic)


class KAFKA_COMSUMER(object):
    def __init__(self, config):
        servers = config.get('servers', ['127.0.0.1:9092'])
        topics = config.get('topic', 'rainwind_topic_test')
        group_id = config.get('group_id', 'rainwind_group_01')

        kafka_configs = { 
            'bootstrap_servers': servers,
            'group_id' : group_id,
        }   

        self.consumer = KafkaConsumer(**kafka_configs)

        subscribe_pattern = config.get('subscribe_pattern')
        if subscribe_pattern:
            consumer.subscribe(pattern=subscribe_pattern)

    def consumer(self, deal_func=default_deal_func):
        for msg in self.consumer:
            #content = msg.value
            deal_func(msg)

    def default_deal_func(msg):
        print msg


if __name__ == "__main__":
    main()
