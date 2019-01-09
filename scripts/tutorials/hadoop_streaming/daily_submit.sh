#!/bin/bash

# get date param
if [[ $# == 0 ]];then
    data_date=$(date +%F -d '-1 days')
else
    data_date=${@:1:1}
fi

# get code path & log path
cwd_path=$(dirname `readlink -f $0`)
logs_path=${cwd_path}/logs
log_prefix=${data_date}

# config env
HADOOP_PATH=/usr/bin/hadoop/software/hadoop/bin:/usr/bin/hadoop/software/hadoop/etc/hadoop
export PATH=$PATH:$HADOOP_PATH
source ~/.bashrc

# execute 
mkdir -p ${logs_path}
cd ${cwd_path}
if [ -a "${logs_path}/${log_prefix}*" ]; then
    rm ${logs_path}/${log_prefix}*
fi
echo "Data date: $data_date"
sh submit.sh ${data_date} 1>${logs_path}/${log_prefix}.out 2>${logs_path}/${log_prefix}.err

# check submit state & create ERROR FILE LOG
if [[ $? -ne 0 ]]; then
    cp ${logs_path}/${data_date}.err ${logs_path}/${log_prefix}_ERROR
fi
