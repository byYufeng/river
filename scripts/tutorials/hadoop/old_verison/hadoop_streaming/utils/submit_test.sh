#!/bin/bash
#Author: fsrm

date=$1
JOB_NAME=""

cwd=$(dirname `readlink -f $0`)
INPUT_PATH="$cwd/test_input/$date"
OUTPUT_PATH="$cwd/test_output/$date"

source ~/.bashrc
local_hadoop_path=""
local_hadoop_streaming_jar_path=""
alias hadoop="$local_hadoop_path/haoop/bin/hadoop"

hadoop fs -test -e $OUTPUT_PATH
if [ $? -eq 0 ]; then
    hadoop fs -rm -r ${OUTPUT_PATH}
fi

hadoop jar $local_hadoop_streaming_jar_path \
    -D mapred.job.name=${JOB_NAME} \
    -D mapred.reduce.tasks=10 \
    -D mapred.task.timeout=3600000 \
    -D mapred.compress.map.out=false \
    -D mapred.map.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapred.output.compress=false \
    -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapreduce.job.priority=HIGH \
    -input  ${INPUT_PATH} \
    -output ${OUTPUT_PATH} \
    -cmdenv DATA_DATE=${date} \
    -file map.py \
    -file reduce.py \
    -mapper 'python map.py' \
    -reducer 'python reduce.py' \
    -cacheArchive file://$cwd/kafka-python-1.4.4.tgz#kafka \

if [[ $? -ne 0 ]]; then
    echo "$JOB_NAME failed"
    exit 1
else
    echo "$JOB_NAME finished"
fi
