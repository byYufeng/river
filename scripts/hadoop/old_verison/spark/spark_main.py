#! /usr/bin/env python
# coding:utf-8
"""
Author: fsrm
Create Time: 2019-06-21 10:37:20
Last modify: 2019-06-21 10:37:20
"""

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import json, time, traceback
from datetime import datetime

def main():
    default_date = "2019-06-15"

    date_str = sys.argv[1] if len(sys.argv) > 1 else default_date
    input_base_uri = "/home/%s"
    output_base_uri = "/home/%s" % time.time()
    run(input_base_uri, output_base_uri, date_str)


def run(input_base_uri, output_base_uri, date_str):
    date_format = '%Y-%m-%d'
    last_days = 30

    # load data
    time_dt = datetime.strptime(date_str, date_format)
    uri_list = [input_base_uri.strip() % datetime.strftime(time_dt - timedelta(days=day), date_format) for day in range(last_days)]
    input_uri = ','.join(uri_list)
    shixianzhuji_rdd = sc.textFile(input_uri)
    shixianzhuji_df = sqlContext.read.json(shixianzhuji_rdd)
    print 'total count: %s' % shixianzhuji_df.count()

    #sql_filter = 'remote_geo_detail.global_country_code != "CN" and remote_geo_detail.global_country_code != ""'
    # query
    sql_filter = ''
    res_df = shixianzhuji_df.filter(sql_filter)
        
    # trans df type result to json type result
    res_dict_list = [x.asDict(True) for x in res_df.collect()]
    res_json_list = [json.dumps(x) for x in res_dict_list]

    # output
    res_json_rdd = sc.parallelize(res_json_list)
    res_json_rdd.saveAsTextFile(output_base_uri)


if __name__ == "__main__":
    from pyspark import SparkConf, SparkContext, SparkFiles
    from pyspark.sql import SQLContext, Row

    spark_app_name = ''
    conf = SparkConf().setAppName(spark_app_name).set("spark.dynamicAllocation.enabled", "false")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    main()
