#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.getcwd())
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.functions import explode
from datetime import datetime, timedelta
import json, time


def main():
    HA = ""
    input_base_uri = ""
    output_base_uri = ""

    if not date_str: # test
        HA = ""
        input_base_uri = "test_data/input"
        output_base_uri = "test_data/output"

    run(HA + input_base_uri, HA + output_base_uri, date_str)


def run(input_base_uri, output_base_uri, date_str):
    input_rdd = sc.textFile(input_base_uri + os.sep + date_str)
    input_df = sqlContext.read.json(input_rdd)

    total_count = input_df.count()
    explode_df = df.select(explode("persons").alias("person"), "md5", "sha1")
    name_age_count = explode_df.groupby("person.name", "person.age").count().orderBy("name", "age") 

    # output
    statistic_res = {}
    statistic_res["summary"] = {"total": total_count, "k_pct": "%.2f" % (float(total_count)/total_count * 100) + "%" }
    statistic_res["name_age"] = name_age_count.rdd.map(lambda x:x.asDict()).collect()
    
    output(sc.parallelize([json.dumps(statistic_res)]), output_base_uri + os.sep + '%s/%s' % (date_str, 'statistic'), 1)
    output(input_parsed_json_rdd, output_base_uri + os.sep + '%s/%s' % (date_str, 'data'))


def output(res_rdd, output_uri, repartition_num=0):
    if repartition_num:
        res_rdd.repartition(repartition_num).saveAsTextFile(output_uri)
    else:
        res_rdd.saveAsTextFile(output_uri)


if __name__ == "__main__":
    conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    date_str = sys.argv[1] if len(sys.argv) > 1 else ""
    main()
