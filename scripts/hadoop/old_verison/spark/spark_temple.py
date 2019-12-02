#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
reload(sys)
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/libs')
sys.path.append(os.getcwd() + '/../utils')

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from datetime import datetime, timedelta
import json

from common import *
from config import *
from rmq import *


def main():
    if date_str:
        run_daily(date_str)
    else:
        local_test()


def run_daily(date_str):
    input_base_uri_daily = "hdfs://" + "/input/%s"
    output_base_uri_daily = "hdfs://" + "/output/%s"
    run(input_base_uri_daily, output_base_uri_daily, date_str)


def local_test():
    date_str = '1999-12-01'
    input_base_uri_loacl_test = "/input_test/%s"
    output_base_uri_loacl_test = "/output_test/%s"
    run(input_base_uri_loacl_test, output_base_uri_loacl_test, date_str)


def run(input_base_uri, output_base_uri, date_str):
    input_uri = input_base_uri % date_str
    output_uri = output_base_uri % date_str

    rdd = sc.textFile(input_uri)
    df = sqlContext.read.json(rdd)

    print 'total count: %s' % df.count()

    # collect & output
    # filter
    filter_sql = ''

    # grouped for rdd
    df_filtered = df.filter(filter_sql)
    df_grouped = df_filtered.rdd.groupBy(lambda x : '%s,%s' % (x['field_a']['aa'], x['field_b']['bb']))
    grouped_res = df_grouped.collect()
    grouped_json_list = [json.dumps({k: [x.asDict(True) for x in vs]}) for (k, vs) in grouped_res]

    # group & count for df
    count_df = df.filter(filter_sql).groupBy(['field_a.aa', 'field_b.bb']).count()
    count_sorted_rows = count_df.sort("count", ascending=False).collect()
    grouped_json_list = [json.dumps(x.asDict(True)) for x in count_sorted_rows]


    output(grouped_json_list, output_uri)


def output(res_json_list, output_hdfs_path):   
    #stdout
    print res_json_list

    #rabbitmq
    walk(rmq_publish, res_json_list)

    #fs
    res_rdd = sc.parallelize(res_json_list)
    res_rdd.saveAsTextFile(output_hdfs_path)


def rmq_publish(msg):
    rmq_producer.publish(msg)


if __name__ == "__main__":
    date_str = sys.argv[1] if len(sys.argv) > 1 else ''

    spark_app_name = 'spark_%s' % date_str
    conf = SparkConf().setAppName(spark_app_name).set("spark.dynamicAllocation.enabled", "false")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    rmq_config = ''
    rmq_producer = RMQ_PRODUCER(rmq_config)

    main()
