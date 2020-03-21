#!/bin/bash
#Author: fsrm

./bin/flink run -m yarn-cluster -p 1 -yjm 128m -ytm 512m ./examples/batch/WordCount.jar
