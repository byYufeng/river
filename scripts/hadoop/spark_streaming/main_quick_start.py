#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-05-08 11:07:50
Last modify: 2019-05-08 11:07:50
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
#https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html


def main():
    # init
    batch_interval = 1 
    #sc = SparkContext('local[2]', 'localtext')
    sc = SparkContext()
    ssc = StreamingContext(sc, batch_interval)

    lines = ssc.socketTextStream('localhost', 9999)
    # ssc.socketTextStream return RDD:[line...] instead of DStream:[RDD...] in kafka, flume...

    words = lines.flatMap(lambda line: line.split(' '))
    word_pairs = words.map(lambda word: (word, 1)) 
    word_counts = word_pairs.reduceByKey(lambda x, y: x+y)
    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    main()
    # shell:"nc -lk 9999"
