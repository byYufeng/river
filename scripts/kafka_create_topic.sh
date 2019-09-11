#!/bin/bash
#Author: fsrm

# 下述参数必须都要有
bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic azkaban-logging --partitions 1 --replication-factor 2

