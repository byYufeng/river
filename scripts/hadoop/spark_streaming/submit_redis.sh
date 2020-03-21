#!/bin/bash

data_date=${1:-"0"}
job_name=${2:-"fsrm_test"}
user=`whoami`
input_path="/home/${user}/${job_name}/input/${data_date}"
output_path="/home/${user}/${job_name}/output/${data_date}"
#input_path="./submit.sh"
#output_path="./submit.sh.out"

driver_memory=512m
driver_memory_overhead=64m
num_executors=1
executor_cores=1
executor_memory=512m
executor_memory_ouverhead=64m
ldap_passwd=""

let parallelism=${num_executors}*${executor_cores}*3

pass_success_job=0
hadoop fs -test -e $output_path
if [ $? -eq 1 ]; then
    hadoop fs -mkdir -p ${output_path}
else
    if [ $pass_success_job -eq 1 ]; then
        SUCCESS_FLAG=`hadoop fs -stat ${output_path}/_SUCCESS`
        if [ -z "$SUCCESS_FLAG" ]; then
            echo ""
        else
            echo "[*] `date` JOB $JOB_NAME has been completed!"
            exit 0
        fi  
    fi
fi
hadoop fs -rm -r ${output_path}


a="/home/$user/libs/spark-redis/target/spark-redis-2.4.1-SNAPSHOT-jar-with-dependencies.jar"
source ~/.bashrc
export HADOOP_CONF_DIR="$(dirname `which hadoop`)/../etc/hadoop"
/usr/lib/spark/bin/spark-submit \
  --name $job_name \
  --master yarn \
  --deploy-mode cluster \
  --num-executors ${num_executors} \
  --executor-cores ${executor_cores} \
  --conf spark.yarn.archive="hdfs:///libs/spark_jars.zip" \
  --conf spark.driver.memory=$driver_memory \
  --conf spark.driver.memoryOverhead=$driver_memory_overhead \
  --conf spark.executor.memory=$executor_memory \
  --conf spark.executor.memoryOverhead=$executor_memory_ouverhead \
  --conf spark.default.parallelism=${parallelism} \
  main.py $data_date $input_path $output_path

  #--queue root.default \
  #--archives hdfs:///home/$user/job_dependices/${job_name}/dependices.zip \
  #driver_memory=${driver_memory_num}m
  #executor_memory=${executor_memory_num}m
  #--conf spark.shuffle.service.enabled=true \
  #--conf spark.dynamicAllocation.enabled=true \
  #--conf spark.dynamicAllocation.maxExecutors=${num_executors} \
  #--conf spark.dynamicAllocation.schedulerBacklogTimeout=1s \
  #--conf spark.dynamicAllocation.executorIdleTimeout=300s \
  #--conf spark.sql.warehouse.dir=hdfs:///home/hive/warehouse \
