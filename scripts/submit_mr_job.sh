#获取时间
if [[ $# == 0 ]];then
    #date=$(date +%F -d '-1 days')
    date=$(date +%F)
elif [[ $# == 1 ]];then
    date=${@:1:1}
fi

#导入_syslog函数
if [ -e ${HOME}/.bashrc ];then
    . ${HOME}/.bashrc
fi

cwd=$(dirname $0)
hdfs_path="hdfs://namenode.rainwind.net:9000"
hdfs_home="/home/hdp-skyeye/proj/hdp-skyeye-lab/"
hdfs_input="dga/daily/${date}/*"
hdfs_output="dga/daily_out/${date}"
job_name="rainwind_skyeye_dga-daily_${date}"

hdfs_input=${hdfs_path}${hdfs_home}${hdfs_input}
hdfs_output=${hdfs_path}${hdfs_home}${hdfs_output}

cmd="/usr/bin/hadoop/software/hadoop/bin/hadoop fs -rmr ${hdfs_output}"
echo "Remove output folder:"$cmd
$cmd

cmd="/usr/bin/hadoop/software/hadoop/bin/hadoop jar /usr/bin/hadoop/software/hadoop/contrib/streaming/hadoop-streaming.jar \
-D mapred.job.name=${job_name} \
-D mapred.reduce.tasks=800 \
-D mapred.output.compress=true \
-D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
-D mapred.task.timeout=3600000 \
-cmdenv _INSERT_TIME=${date} \
-cacheArchive ${hdfs_path}/home/hdp-skyeye/proj/hdp-skyeye-lab/libs/python/bson.tar.gz#bson \
-cacheArchive ${hdfs_path}/home/hdp-skyeye/proj/hdp-skyeye-lab/libs/python/pymongo.tar.gz#pymongo \
-input  ${hdfs_input} \
-output ${hdfs_output} \
-mapper map.py \
-reducer reduce.py \
-file ${cwd}/reduce.py \
-file ${cwd}/map.py"

haha(){
    echo $cmd
    $cmd
    if [ $? -ne 0 ];then
        _syslog ${MSG_TAG} "[lx title=\"DGA-daily ${DATE} job Failed\"]" "[submit.sh:$LINENO] hadoop job ${job_name} failed"
        exit
    fi
}
