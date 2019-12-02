#!/bin/bash

date=$1; date2=`date -d "$date" +%Y%m%d`
JOB_NAME=$2

INPUT_PATH=""
OUTPUT_PATH=""

cwd=$(dirname `readlink -f $0`)
source ~/.bashrc

# 检查输出目录。若存在，检查是否有任务完成的FLAG，完成则退出。若不存在，则新建以保证父目录可用，然后删除该目录
hadoop fs -test -e $OUTPUT_PATH
if [ $? -eq 1 ]; then
    hadoop fs -mkdir -p ${OUTPUT_PATH}
else
    SUCCESS_FLAG=`hadoop fs -stat ${OUTPUT}/_SUCCESS`
    if [ -z "$SUCCESS_FLAG" ]; then
        echo ""
    else
        echo "[*] `date` JOB $JOB_NAME has been completed!"
        exit 0
    fi
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
    echo "[*] `date` $JOB_NAME failed"
    exit 1
else
    echo "[*] `date` $JOB_NAME finished"
fi
