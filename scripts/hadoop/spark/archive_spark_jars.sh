#!/bin/bash
#Author: fsrm

# define 
user=`whoami`
hdfs_archieve_dir="/home/${user}/dependices"
archive_name="spark_jars.zip"
hdfs_archieve_path=${hdfs_archieve_dir}/${archive_name}

#tar czvf ${archive_dir}/${archive_name} -C ${dependices_dir} `ls ${dependices_dir}`
zip -j ${archive_name} ${SPARK_HOME}/jars/* 

# upload
hadoop fs -mkdir -p ${hdfs_archieve_dir}
hadoop fs -test -e ${hdfs_archieve_path}
if [ $? -eq 0 ]; then
    hadoop fs -rm ${hdfs_archieve_path}
fi

hadoop fs -put ${archive_name} ${hdfs_archieve_dir}
