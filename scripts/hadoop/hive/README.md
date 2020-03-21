0.
set hive.exec.mode.local.auto=true; #使用本地模式执行MR，用于快速测试
set hive.cli.print.header=true; #查询时显示字段名（字段名默认附带表名）
set hive.resultset.use.unique.column.names=false; # 显示字段时候去掉表名

2.计算一次TOP K需要两个MR：一次WordCount,再一次排序

3.
set hive.auto.convert.join=true; #自动根据情况执行mapjoin
