#!/bin/bash
#Author: fsrm

dir_path=''
hadoop dfs -ls $dir_path | tail -n +2 | awk '{print $NF}' | awk -F'/' '{print $NF}' | xargs -I {} sh daily_submit.sh {} 
