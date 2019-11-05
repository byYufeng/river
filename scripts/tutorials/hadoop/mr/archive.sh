#!/bin/bash
#Author: fsrm

dependices_dir="./dependices"
archive_dir="./archives"
mkdir -p ${dependices_dir} ${archive_dir}
cp -r ${HOME}/riven/utils \
    ${dependices_dir}/

job_name=$1
archive_name=${job_name}.tgz
hdfs_archieve_dir="/home/fsrm/job_dependices"
hdfs_archieve_path=${hdfs_archieve_dir}/${archive_name}

hadoop fs -mkdir -p ${hdfs_archieve_dir}
hadoop fs -test -e ${hdfs_archieve_path}
if [ $? -eq 0 ]; then
    hadoop fs -rm ${hdfs_archieve_path}
fi

tar czvf ${archive_dir}/${archive_name} -C ${dependices_dir} `ls ${dependices_dir}`
hadoop dfs -put ${archive_dir}/${archive_name} ${hdfs_archieve_dir}
