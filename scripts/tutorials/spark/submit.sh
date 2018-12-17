#!/bin/sh
data_date=$1
job_name=""

num_executors=5
executor_memory=2g
executor_cores=4
driver_memory=8g
memory_fraction=0.6
memory_storageFraction=0.5
let parallelism=${num_executors}*${executor_cores}*3

echo $job_name
#echo "num_executors is ${num_executors}"
#echo "executor_memory is ${executor_memory}"
#echo "driver_memory is ${driver_memory}"
#echo "executor_cores is ${executor_cores}"
#echo "memory_fraction is ${memory_fraction}"
#echo "memory_storageFraction is ${memory_storageFraction}"
#echo "executorcores is ${executor_cores}"
#echo "parallelism is ${parallelism}"

local_path=""
spark_log_dir=$local_path/logs/spark
mkdir -p $spark_log_dir
 
/usr/bin/hadoop/software/sparkonyarn/bin/spark-submit \
  --name $job_name \
  --master yarn \
  --deploy-mode client \
  --queue root.tic \
  --num-executors ${num_executors} \
  --executor-memory ${executor_memory} \
  --executor-cores ${executor_cores} \
  --driver-memory ${driver_memory} \
  --conf spark.default.parallelism=${parallelism} \
  --conf spark.memory.fraction=${memory_fraction} \
  --conf spark.memory.storageFraction=${memory_storageFraction} \
  --conf spark.shuffle.sort.bypassMergeThreshold=40 \
  --conf spark.local.dir=${spark_log_dir} \
  --conf spark.eventLog.dir=${spark_log_dir} \
  --conf spark.eventLog.enabled=true \
  --conf spark.sql.warehouse.dir=hdfs://~/hive/warehouse \
  --archives hdfs://~/libs/python/pika.tgz#pika \
  main.py $data_date
