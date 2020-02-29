1.
set hive.cli.print.header=true; #查询时显示字段名（带表名）
set hive.resultset.use.unique.column.names=false; # 显示字段时候去掉表名

2.计算一次TOP K需要两个MR：一次WordCount,再一次排序
