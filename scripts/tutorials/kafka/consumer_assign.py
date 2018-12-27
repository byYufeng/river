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
from kafka import TopicPartition


def main():
    kafka_configs = {
        'bootstrap_servers' : ['10.202.252.143:9092'], 
        'group_id' : 'g5'
    }
    consumer = KafkaConsumer(**kafka_configs)

    topics = ['rainwind_test', 'rainwind_test2', 'rainwind_test3']
    topic_partitions = [
            #TopicPartition(topics[0], 0),
            #TopicPartition(topics[1], 0),
            TopicPartition(topics[2], 1)
            ]

    #print 'current committed offset:', consumer.committed(topic_partitions[0])
    #print 'current offset:'consumer.position(topic_partitions[0])
    #print consumer.offsets_for_times({topic_partitions[0]:1545897787936})
    #print consumer.highwater(topic_partitions[0])
    consumer.assign(topic_partitions)

    #consumer.seek_to_beginning()
    #consumer.seek_to_end()
    #consumer.seek(topic_partitions[0], 0)

    #msg = next(consumer)
    #print msg
    print consumer.poll(100, max_records=3)
    #consumer.commit()

if __name__ == "__main__":
    main()
