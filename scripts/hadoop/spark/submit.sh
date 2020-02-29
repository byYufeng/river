#!/bin/bash

data_date=$1
job_name=$2
ldap_passwd=""
user=`whoami`

driver_memory_num=512
num_executors=1
executor_cores=1
executor_memory_num=512

driver_memory=${driver_memory_num}m
executor_memory=${executor_memory_num}m
let parallelism=${num_executors}*${executor_cores}*3

#HADOOP_PATH=/usr/bin/hadoop/software/hadoop/bin:/usr/bin/hadoop/software/hadoop/etc/hadoop
#spark-sumbit="/usr/bin/hadoop/software/sparkonyarn/bin/spark-submit"
#export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/etc/hadoop
source ~/.bashrc

#--archives hdfs:///home/$user/dependices/${job_name}/dependices.zip \
#--conf spark.yarn.jars=hdfs:///home/$user/dependices/spark_jars.zip \
$SPARK_HOME/bin/spark-submit \
  --name $job_name \
  --master yarn \
  --deploy-mode cluster \
  --queue default \
  --conf spark.driver.cores=2 \
  --conf spark.driver.memory=${driver_memory} \
  --conf spark.executor.instances=${num_executors} \
  --conf spark.executor.cores=${executor_cores} \
  --conf spark.executor.memory=${executor_memory} \
  --conf spark.default.parallelism=${parallelism} \
  --conf spark.yarn.archive=hdfs:///home/${user}/dependices/spark_jars.zip \
  --conf spark.sql.warehouse.dir=hdfs:///home/hive/warehouse \
  --archives hdfs:///home/fgg/dependices/spark_test.zip#dependices \
  main.py $data_date
