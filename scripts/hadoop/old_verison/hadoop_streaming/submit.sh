#!/bin/bash
#Author: fsrm

date=$1
date2=`date -d "$date" +%Y%m%d`
JOB_NAME=$2

INPUT_PATH=""
OUTPUT_PATH=""

cwd=$(dirname `readlink -f $0`)
source ~/.bashrc

hadoop fs -mkdir -p ${OUTPUT_PATH}
hadoop fs -rm -r ${OUTPUT_PATH}

#hadoop fs -test -e $OUTPUT_PATH
#if [ $? -eq 0 ]; then
#    hadoop fs -rm -r ${OUTPUT_PATH}
#else
#    hadoop fs -mkdir -p ${OUTPUT_PATH}
#fi

hadoop streaming \
    -D mapred.job.name=${JOB_NAME} \
    -D mapred.job.queue.name=root.default \
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
    -mapper 'python map.py' \
    -reducer 'python reduce.py' \
    -file 'map.py' \
    -file 'reduce.py' \
    -cacheArchive hdfs:///home/test_archive.tgz#test_archive \

if [[ $? -ne 0 ]]; then
    echo "[*] $JOB_NAME failed"
    exit 1
else
    echo "[*] $JOB_NAME successed"
fi
