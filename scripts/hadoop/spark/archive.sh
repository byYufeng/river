#!/bin/bash
#Author: fsrm

# define 
default_name="spark_test"
job_name=${1:-$default_name}
user=`whoami`
hdfs_archive_dir="/home/${user}/dependices"

# make package at local
dependices_dir="./dependices"
archive_dir="./archives"
#archive_name="${job_name}.zip"
archive_name="$default_name.zip"
mkdir -p ${dependices_dir} ${archive_dir}

cp -r ${HOME}/riven/utils \
    ${dependices_dir}/

# upload
hdfs_archive_path=${hdfs_archive_dir}/${archive_name}
hadoop fs -mkdir -p ${hdfs_archive_dir}
hadoop fs -test -e ${hdfs_archive_path}
if [ $? -eq 0 ]; then
    hadoop fs -rm ${hdfs_archive_path}
fi

#tar czvf ${archive_dir}/${archive_name} -C ${dependices_dir} `ls ${dependices_dir}`
cd ${dependices_dir} && zip -r ../${archive_dir}/${archive_name} * && cd -
hadoop fs -put ${archive_dir}/${archive_name} ${hdfs_archive_dir}
