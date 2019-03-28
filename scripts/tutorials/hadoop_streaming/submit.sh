#!/bin/bash

date=$1
INPUT_PATH=""
OUTPUT_PATH=""
JOB_NAME=""

hadoop fs -test -e $OUTPUT_PATH
if [ $? -eq 0  ]; then
    hadoop fs -rm -r ${OUTPUT_PATH}
fi

hadoop streaming \
    -D mapred.job.name=${JOB_NAME} \
    -D mapred.reduce.tasks=100 \
    -D mapred.task.timeout=3600000 \
    -D mapred.compress.map.out=false \
    -D mapred.map.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapred.output.compress=false \
    -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapreduce.job.priority=HIGH \
    -cacheArchive hdfs:///home/test_archive.tgz#test_archive \
    -input  ${INPUT_PATH} \
    -output ${OUTPUT_PATH} \
    -cmdenv DATA_DATE=${date} \
    -file map.py \
    -file reduce.py \
    -mapper 'python map.py' \
    -reducer 'python reduce.py'

if [[ $? -ne 0 ]]; then
    echo "$JOB_NAME failed"
    exit 1
else
    echo "$JOB_NAME finished"
fi
