#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-05-08 11:07:50
Last modify: 2019-05-08 11:07:50
#https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("~/riven/utils/db")
sys.path.append("~/riven/libs/python")


import os, time
import traceback, json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from _redis import *


# https://spark.apache.org/docs/2.4.4/api/python/index.html
# 貌似kafka0.10起不支持python了？
def main():
    socket_port = 8888
    socket_host = 'localhost'
    batch_interval = 3
    #sc = SparkContext('local[*]', 'localtext')
    sc = SparkContext()
    sc.addPyFile('~/riven/utils/db/_redis.py')
    sc.addPyFile('~/libs/python/redis2.zip')
    ssc = StreamingContext(sc, batch_interval)

    # 从socket接收数据（字符串），分词做word count
    lines = ssc.socketTextStream(socket_host, socket_port)
    words = lines.flatMap(lambda line: line.split(' '))
    word_pairs = words.map(lambda word: (word, 1)) 
    word_counts = word_pairs.reduceByKey(lambda x, y: x+y)

    # 处理dsteam：每次获取的dstream其实是一个 包含多个RDD元素的List ==> dstream: [RDD1, RDD2]
    #deal_by_record(word_counts)
    #deal_by_rdd(word_counts)
    deal_by_partition(word_counts)
    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()

# deal by partition: 为每个partition创建一个连接，最优
def deal_by_partition(dstream):
    dstream.foreachRDD(lambda rdd: rdd.foreachPartition(wc_incr_by_partition))

def wc_incr_by_partition(rdd_partition):
    redis_client = REDIS_CLIENT()
    def _deal(record):
        print record
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
        print record
        word, count = record
        redis_client = REDIS_CLIENT()
        redis_client.incr(word, count)
    rdd.foreach(_deal) #等价于 rdd.foreach(lambda x: _deal(x))


if __name__ == "__main__":
    main()
    # shell:"nc -lk 9999"
