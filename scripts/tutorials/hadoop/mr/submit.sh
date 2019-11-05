#!/bin/bash

date=$1
date2=`date -d "$date" +%Y%m%d`
JOB_NAME=$2

INPUT_PATH=""
OUTPUT_PATH=""

cwd=$(dirname `readlink -f $0`)
source ~/.bashrc

hadoop fs -test -e $OUTPUT_PATH
if [ $? -eq 1 ]; then
    hadoop fs -mkdir -p ${OUTPUT_PATH}
fi
hadoop fs -rm -r ${OUTPUT_PATH}

hadoop streaming \
    -D mapred.job.name=${JOB_NAME} \
    -D mapred.job.queue.name=root.default \
    -D mapreduce.success.file.status=true \
    -D mapred.map.tasks=1000 \
    -D mapred.reduce.tasks=100 \
    -D mapreduce.map.memory.mb=2048 \
    -D mapred.child.java.opts=-Xmx2048m \
    -D mapreduce.jobtracker.split.metainfo.maxsize=-1 \
    -D mapreduce.reduce.memory.mb=4096 \
    -D mapred.task.timeout=3600000 \
    -D mapred.compress.map.out=false \
    -D mapred.map.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapred.output.compress=false \
    -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
    -D mapreduce.job.priority=HIGH \
    -archives hdfs://HACluster/home/fsrm/job_dependices/${JOB_NAME}.tgz#dependices \
    -file 'map.py' \
    -file 'reduce.py' \
    -input  ${INPUT_PATH} \
    -output ${OUTPUT_PATH} \
    -cmdenv DATA_DATE=${date} \
    -mapper 'python map.py' \
    -reducer 'python reduce.py' \

if [[ $? -ne 0 ]]; then
    echo "$JOB_NAME failed"
    exit 1
else
    echo "$JOB_NAME finished"
fi
