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

import os, time, json
from kafka import KafkaProducer, KafkaConsumer, TopicPartition


def main():
    kafka_configs = {
        'bootstrap_servers' : ['10.202.252.143:9092'], 
    }
    #topics = ['rainwind_test', 'rainwind_test2', 'rainwind_test3']
    #consumer = KafkaConsumer(*topics, **kafka_configs)
    consumer = KafkaConsumer(**kafka_configs)

    all_topics = consumer.topics()
    #print 'All topics:', all_topics, '\n'

    all_topic_partitions = {}
    for topic in all_topics:
        topic_partitions = []
        partitions = consumer.partitions_for_topic(topic)
        for partition in partitions:
            topic_partitions.append(TopicPartition(topic, partition))
        all_topic_partitions[topic] = topic_partitions
    #print 'Topic partitions:', all_topic_partitions, '\n'

    all_partition_offsets = {}
    for topic in all_topic_partitions:
        partition_offsets = {}
        for partition in all_topic_partitions.get(topic):
            start = consumer.beginning_offsets([partition]).values()[0]
            end = consumer.end_offsets([partition]).values()[0]
            partition_offsets[partition.partition] = {'start':start, 'end':end}
        all_partition_offsets[topic] = partition_offsets
    print 'All partition offsets:\n\n%s' % all_partition_offsets

    #print 'Subscription:', consumer.subscription()
    #print 'Assignment:', consumer.assignment()
    #print 'Metrics:', consumer.metrics()

    #consumer.subscribe([])
    #consumer.assign([])
    #for msg in consumer:
    #    print msg
    #print next(consumer)
    #print consumer.poll()


if __name__ == "__main__":
    main()
