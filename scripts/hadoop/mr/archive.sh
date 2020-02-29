#!/bin/bash
#Author: fsrm

#
default_name="mr_test"
job_name=${1:-$default_name}
user=`whoami`
hdfs_archive_dir="/home/${user}/dependices"

#
dependices_dir="./dependices"
archive_dir="./archives"
#archive_name="${job_name}.tgz"
archive_name="$default_name.tgz"
mkdir -p ${dependices_dir} ${archive_dir}

cp -r ${HOME}/riven/utils \
    ${dependices_dir}/

#
hdfs_archive_path=${hdfs_archive_dir}/${archive_name}
hadoop fs -mkdir -p ${hdfs_archive_dir}
hadoop fs -test -e ${hdfs_archive_path}
if [ $? -eq 0 ]; then
    hadoop fs -rm ${hdfs_archive_path}
fi

tar czvf ${archive_dir}/${archive_name} -C ${dependices_dir} `ls ${dependices_dir}`
hadoop fs -put ${archive_dir}/${archive_name} ${hdfs_archive_dir}
