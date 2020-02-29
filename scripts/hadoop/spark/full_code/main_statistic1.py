#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/dependices.zip/dependices')
#for x in os.walk('.', followlinks=True): print x

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from datetime import datetime, timedelta
import json, time

from utils.common import *
from utils.config import *
from utils.middleware._rabbitmq import *


def main():
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
    rdd = sc.textFile(input_uri)
    df = sqlContext.read.json(rdd)
    print 'total count: %s' % df.count()

    # query
    # sql_filter = 'remote_geo_detail.global_country_code != "CN" and remote_geo_detail.global_country_code != ""'
    sql_filter = ''
    res_df = df.filter(sql_filter)
    
    # trans df type result to json type result
    res_dict_list = [x.asDict(True) for x in res_df.collect()]
    res_json_list = [json.dumps(x) for x in res_dict_list]

    # output
    res_json_rdd = sc.parallelize(res_json_list)
    res_json_rdd.saveAsTextFile(output_base_uri)


if __name__ == "__main__":
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    rmq_producer = RMQ_PRODUCER(rmq_config_local)
    default_date = "2019-06-15"
    date_str = sys.argv[1] if len(sys.argv) > 1 else default_date
    main()
