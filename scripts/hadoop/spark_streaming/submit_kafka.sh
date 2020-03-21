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


source ~/.bashrc
#export HADOOP_CONF_DIR="$(dirname `which hadoop`)/../etc/hadoop"
/usr/lib/spark/bin/spark-submit \
  --name $job_name \
  --conf spark.driver.memory=$driver_memory \
  --conf spark.driver.memoryOverhead=$driver_memory_overhead \
  --conf spark.executor.memory=$executor_memory \
  --conf spark.executor.memoryOverhead=$executor_memory_ouverhead \
  --conf spark.default.parallelism=${parallelism} \
  --jars /home/fgg/libs/jars/spark-streaming-kafka-0-8-assembly_2.11-2.1.0.jar \
  kafka_main.py $data_date $input_path $output_path
