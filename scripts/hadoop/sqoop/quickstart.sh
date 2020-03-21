#!/bin/bash
#Author: fsrm

# test mysql
sqoop list-databases --connect jdbc:mysql://127.0.0.1:3386/ --username root --^Cssword mysql

# import from sqlite to hdfs
# 使用query查询时，必须配合split-by指定分区字段和$CONDITIONS参数。
# 但是sqlite的导入仍存在bug，不可使用
sqoop import --connect jdbc:sqlite:/a.db --driver org.sqlite.JDBC  --target-dir /site/articles --query "select id from articles where visiable=1 and \$CONDITIONS order by id desc limit 10;" --split-by id
