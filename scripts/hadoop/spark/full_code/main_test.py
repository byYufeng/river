#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
#reload(sys)
#sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd())

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row 
from datetime import datetime, timedelta
import json, time


def main():
    job_name = ''
    user = ''
    input_uri = "/home/{user}".format(user=user)
    output_uri = "/home/{user}/{path}".format(user=user, path=job_name + str(time.time()))
    run(input_uri, output_uri)


def run(input_uri='', output_uri=''):
    rdd = sc.textFile(input_uri)

    # rdd map&filter
    rdd = rdd.map(lambda x: x)
    #target = ''
    #df_res = rdd_map.filter(lambda x: target in x[0])
    #res_json_rdd = sc.parallelize(res_json_list)
    output(rdd)


def output(rdd, output_uri):
    rdd.saveAsTextFile(output_uri)
    #rdd.repartition(1).saveAsTextFile(output_uri)


def statistic():
    # query: sql_filter = 'remote_geo_detail.global_country_code != "CN" and remote_geo_detail.global_country_code != ""'
    df = sqlContext.read.json(rdd)
    print('total count: %s' % df.count())
    sql_filter = 'lower(url) like "%{0}%"'.format(target.lower())
    res_df = df.filter(sql_filter)
    print('res count: %s' % res_df.count())


    # trans df type result to json type result
    res_dict_list = [x.asDict(True) for x in res_df.collect()]
    res_json_list = [json.dumps(x) for x in res_dict_list]


if __name__ == "__main__":
    conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    main()
