#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
#reload(sys)
#sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'dependices'))

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row 
from datetime import datetime, timedelta
import json, time

from utils import common


def main():
    user = 'fgg'
    project = "hadoop_test"
    input_uri = "/home/{user}/{project}/input".format(user=user, project=project)
    output_uri = "/home/{user}/{project}/output".format(user=user, project=project)

    rdd = sc.textFile(input_uri)
    rdd = rdd.map(lambda x: x)
    rdd.saveAsTextFile(output_uri)

    # test third
    text_data = ""
    with open("dependices/text_data") as fin:
        text_data = fin.read().strip()
    rdd2 = sc.parallelize([text_data, common.formatter_string_to_timestamp("2020-01-01 00:00:00")])
    rdd2.saveAsTextFile(output_uri+"2")


if __name__ == "__main__":
    conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    main()
