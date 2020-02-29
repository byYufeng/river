#!/bin/bash
#Author: fsrm

start_time=`date -d '2019-01-01' +%Y-%m-%d`
end_time=`date -d '2019-02-15' +%Y-%m-%d`

echo $start_time
#if (( $start_time < $end_time )) 结果异常 不能这样比--使用(())比较字符串
if [[ $start_time < $end_time ]]
then 
    echo 1
else
    echo 0
fi

start_time=`date -d '20190101' +%Y%m%d`
end_time=`date -d '20190215' +%Y%m%d`

echo $start_time
if [[ $start_time < $end_time ]]
then 
    echo 1
else
    echo 0
fi
