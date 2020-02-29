#!/bin/bash
# create by fsrm

CLUSTER1_PATH=""
CLUSTER2_PATH=""

# ly cluster -> zz cluster
HOSTS[0]=""
HOSTS[1]=""
PORT="50070"
MAP_NUM=200

get_active_nn(){
    for HOST in ${HOSTS[@]}
    do
        status=`curl "http://$HOST:$PORT/jmx?qry=Hadoop:service=NameNode,name=NameNodeStatus" | awk -F"[:,]" '/State/{print $2}'`
        if [ $status == '"active"' ] ; then
            echo $HOST
        fi
    done
}          
REMOTE_CLUSTER_URI="`get_active_nn`:$PORT"
hadoop distcp -D mapreduce.framework.name=local -m $MAP_NUM ${CLUSTER1_PATH} webhdfs://${REMOTE_CLUSTER_URI}/${CLUSTER2_PATH}
