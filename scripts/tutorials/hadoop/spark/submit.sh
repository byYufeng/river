#!/bin/bash

data_date=$1
job_name=$2
ldap_passwd=""
user=`whoami`

driver_memory_num=8
num_executors=4
executor_cores=4
executor_memory_num=4

driver_memory=${driver_memory_num}g
executor_memory=${executor_memory_num}g
let parallelism=${num_executors}*${executor_cores}*3

HADOOP_PATH=/usr/bin/hadoop/software/hadoop/bin:/usr/bin/hadoop/software/hadoop/etc/hadoop
export PATH=$PATH:$HADOOP_PATH
source ~/.bashrc

/usr/bin/hadoop/software/sparkonyarn/bin/spark-submit \
  --name $job_name \
  --master yarn \
  --deploy-mode cluster \
  --queue root.default \
  --driver-memory ${driver_memory} \
  --num-executors ${num_executors} \
  --executor-cores ${executor_cores} \
  --executor-memory ${executor_memory} \
  --conf spark.default.parallelism=${parallelism} \
  --conf spark.shuffle.service.enabled=true \
  --conf spark.dynamicAllocation.enabled=true \
  --conf spark.dynamicAllocation.maxExecutors=${num_executors} \
  --conf spark.dynamicAllocation.schedulerBacklogTimeout=1s \
  --conf spark.dynamicAllocation.executorIdleTimeout=300s \
  --conf spark.sql.warehouse.dir=hdfs:///home/hive/warehouse \
  --archives hdfs:///home/$user/job_dependices/${job_name}/dependices.zip \
  main.py $data_date
