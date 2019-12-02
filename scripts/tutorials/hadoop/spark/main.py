#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd())

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row 
from datetime import datetime, timedelta
import json, time


def main():
    job_name = ''
    user = ''
    input_uri = "/home/{user}".format(user=user)
    output_uri = "/home/{user}/{path}".format(user=user, path=job_name + time.time())
    run(output_uri)


def run(input_uri='', output_uri=''):
    uri_list = []
    input_uri = ','.join(uri_list)
    rdd = sc.textFile(input_uri)

    # rdd map&filter
    target = ''
    rdd_map = rdd.map(lambda x: x)
    rdd_res = rdd_map.filter(lambda x: target in x[0])
    print rdd_res.take(10)


    ''' 
    # query: sql_filter = 'remote_geo_detail.global_country_code != "CN" and remote_geo_detail.global_country_code != ""'
    df = sqlContext.read.json(rdd)
    print 'total count: %s' % df.count()
    sql_filter = 'lower(url) like "%{0}%"'.format(target.lower())
    res_df = df.filter(sql_filter)
    print 'res count: %s' % res_df.count()


    # trans df type result to json type result
    res_dict_list = [x.asDict(True) for x in res_df.collect()]
    res_json_list = [json.dumps(x) for x in res_dict_list]
    '''

    # output
    print res_json_list
    res_json_rdd = sc.parallelize(res_json_list)
    res_json_rdd.saveAsTextFile(output_uri)


if __name__ == "__main__":
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    main()
