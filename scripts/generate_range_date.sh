#!/bin/bash
date_format1='%Y-%m-%d'
date_format2='%Y%m%d'

cmd='sh submit.sh'

# judge date & cmd format
if [ "`echo $1 | grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}'`" != "" -a "`echo $2 | grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}'`" != "" ]
then 
    date_format=$date_format1
elif [ "`echo $1 | grep -E '[0-9]{4}[0-9]{2}[0-9]{2}'`" != "" -a "`echo $2 | grep -E '[0-9]{4}[0-9]{2}[0-9]{2}'`" != "" ]
then
    date_format=$date_format2
else 
    echo 'Date format error!'
    exit 1
fi

if [[ $# > 2 ]];then cmd=$3;fi


start_time=`date -d $1 +$date_format`
end_time=`date -d $2 +$date_format`
echo "----------start_time=$start_time end_time=$end_time--------------------"
op=''
if [[ $start_time > $end_time ]]
then
    op='-'
    end_time=`date -d "-1 day $end_time" +$date_format`
else
    op='+'
    end_time=`date -d "+1 day $end_time" +$date_format`
fi

while [[ $start_time != $end_time ]]
do
    _cmd="$cmd $start_time"
    echo $_cmd
    start_time=`date -d "${op}1 day $start_time" +$date_format`
done
