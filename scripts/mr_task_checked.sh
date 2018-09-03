HDFS_PATH=$1

echo total:
hadoop fs -ls $HDFS_PATH 2>/dev/null |wc -l

echo successed:
hadoop fs -ls $HDFS_PATH/* 2>/dev/null | grep _SUCCESS | wc -l
