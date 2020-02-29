#!/bin/bash
#Author: fsrm

$HADOOP_HOME/bin/hadoop jar $HADOOP_STREAMING_JAR \
   -D mapreduce.job.name=$JOB_NAME \
   -D mapred.job.queue.name=root.default \
   -D mapreduce.success.file.status=true \
   -D mapreduce.job.priority="HIGH" \
   -D mapreduce.job.reduces=2 \
   -D stream.map.output.field.separator=',' \
   -D stream.num.map.output.key.fields=2 \
   -D map.output.key.field.separator=','  \
   -D num.key.fields.for.partition=1 \
   -D mapred.text.key.comparator.options="-k2,2nr" \
   -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
   -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
   -input $INPUT \
   -output "$OUTPUT" \
   -mapper "cat" \
   -reducer "cat" 

