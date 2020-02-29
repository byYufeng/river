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

mkdir -p ${logs_path}
cd ${cwd_path}
if [ -a "${logs_path}/${log_prefix}.out" ]; then
    rm ${logs_path}/${log_prefix}*
fi

# config param
MSG_ID=""
JOB_NAME="fsrm__test__${data_date}__mr"
cmds[1]="sh submit.sh ${data_date} ${JOB_NAME} 1>${logs_path}/${log_prefix}.out 2>${logs_path}/${log_prefix}.err"
cmds[2]="sh submit_sort.sh ${data_date} ${JOB_NAME} 1>${logs_path}/${log_prefix}.out 2>${logs_path}/${log_prefix}.err"

# config env
HADOOP_PATH=/usr/bin/hadoop/software/hadoop/bin:/usr/bin/hadoop/software/hadoop/etc/hadoop
export PATH=$PATH:$HADOOP_PATH
source ~/.bashrc

log(){
   echo $1
}

# execute 
log "`date` [*] $JOB_NAME started."
#sh -x archive.sh $JOB_NAME
for i in ${!cmds[@]}
do
    #echo $i, ${cmds[$i]}
    ${cmds[$i]}
    if [[ $? -ne 0 ]]; then
        #trace_url=`cat ${logs_path}/${data_date}.err | egrep 'url|URL' | awk -F 'http' '{print "http"$2}'`
        #application_id=`cat ${logs_path}/${data_date}.err | grep 'application' | awk -F 'application_' '{print "application_"$2}' | awk '{print $1}'`
        #echo -e "\nTrace url:\c ${trace_url}" >> ${logs_path}/${log_prefix}_ERROR
        #cat ${logs_path}/${log_prefix}.* > ${logs_path}/${log_prefix}_ERROR
        #cat ${logs_path}/${log_prefix}_ERROR > ${logs_path}/error_${log_prefix}
        log "[*] `date` $JOB_NAME failed at ${i}."
        #log "[*] Trace url: ${trace_url}"
        #log "[*] Application ID: ${application_id}"
        exit 1
    else
        exit 0
    fi
done
log "[*] `date` $JOB_NAME successed."
 
