#!/bin/bash
REMOTE_CLUSTER_URI='0.0.0.0:50070'
CLUSTER1_PATH="/home/data"
CLUSTER2_PATH="webhdfs://${REMOTE_CLUSTER_URI}/home/data"
hadoop distcp -Dmapreduce.framework.name=local -m 200 ${CLUSTER1_PATH} ${CLUSTER2_PATH}
