#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-05-08 11:07:50
Last modify: 2019-05-08 11:07:50
#https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html
"""

import sys, os
#reload(sys)
#sys.setdefaultencoding("utf-8")
sys.path.append(os.path.join(os.getenv("HOME"),"riven/utils"))
sys.path.append(os.path.join(os.getenv("HOME"),"riven/libs/python"))


import time, traceback, json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils, TopicAndPartition
from pprint import pprint


# https://spark.apache.org/docs/2.4.4/api/python/index.html
def main():
    batch_interval = 3
    sc = SparkContext()
    ssc = StreamingContext(sc, batch_interval)

    kafka_zk = "localhost:2181"
    kafka_server = "localhost:9092"
    groupid = "flume_log_group_1"
    topic_patitions = {"flume_log": 0}

    topics = [k for k in topic_patitions]
    params = {"metadata.broker.list": kafka_server}
    #topicPartion = TopicAndPartition(*[i for i in topic_patitions.items()])
    #topicPartion = TopicAndPartition("flume_log", 0)
    #offset_start = 0
    #fromOffset = {topicPartion: long(offset_start)}


    # ssc产生的DStream可以视作一个包含多个RDD（每个为一条数据）的RDD
    # 从kafka接收的每条数据为KafkaMessageAndMetadata：（key, message）
    def deal_by_reciver():
        rkds = KafkaUtils.createStream(ssc, kafka_zk, groupid, topic_patitions)
        return rkds

    def deal_by_direct():
        dkds = KafkaUtils.createDirectStream(ssc, topics, params)
        #dks = KafkaUtils.createDirectStream(ssc, topics, params, fromOffsets=fromOffset)
        #报了半天org.apache.spark.SparkException: ArrayBuffer(java.io.EOFException: Received -1 when reading from channel, socket has likely been closed.) 的错。不是因为从末尾开始读没数据就报错了，而是因为params里写的是9092的kafka端口而不能是2181 zookeeper端口。不然找不到数据

        def storeOffsetRanges(rdd):
            offsetRanges = rdd.offsetRanges()
            # store: 可存到spark-checkpoint, hbase, zookeeper, kafka中。其中后两者是比较好的（因为可以用kafka监控工具）
            for o in offsetRanges:
                print("%s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset))
            return rdd

        dkds = dkds.transform(storeOffsetRanges)
        return dkds

    def kds_wc(kds):
        lines = kds.map(lambda x: x[1])

        words = lines.flatMap(lambda line: line.split(' '))
        word_pairs = words.map(lambda word: (word, 1)) 
        word_counts = word_pairs.reduceByKey(lambda x, y: x+y)
        return word_counts

    #kafka_dstream = deal_by_reciver()
    kafka_dstream = deal_by_direct()

    word_counts = kafka_dstream.transform(kds_wc)
    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()


# deal by partition: 为每个partition创建一个连接，最优
def deal_by_partition(dstream):
    dstream.foreachRDD(lambda rdd: rdd.foreachPartition(wc_incr_by_partition))

def wc_incr_by_partition(rdd_partition):
    redis_client = REDIS_CLIENT()
    def _deal(record):
        print(record)
        word, count = record
        redis_client.incr(word, count)
    #rdd_partition.foreach(lambda rdd_partition: deal_partition(rdd_partition))
    for r in rdd_partition:
        _deal(r)


# deal by each rdd: 使用collect代替foreach，相当于单进程操作。并发降低，连接压力也降低
def deal_by_record(dstream):
    dstream.foreachRDD(wc_incr_by_rdd)

def wc_incr_by_rdd(rdd):
    redis_client = REDIS_CLIENT()
    res = rdd.collect()
    for element in res:
        word, count = element
        redis_client.incr(word, count)


# deal by each record：效率最差
def deal_by_record(dstream):
    dstream.foreachRDD(wc_incr_by_record)

def wc_incr_by_record(rdd):
    def _deal(record):
        print(record)
        word, count = record
        redis_client = REDIS_CLIENT()
        redis_client.incr(word, count)
    rdd.foreach(_deal) #等价于 rdd.foreach(lambda x: _deal(x))


if __name__ == "__main__":
    main()
