通用
coalesce    调整分区 （默认为减少，不shuffle）
repartition 调整分区(coalesce(shuffle=True)的情况)   
countByKey/countByValue
flatMapValues   [(k, [v1,v2...]...)] => [(k, v1), (k, v2)...]
foreach 没有返回值的map
mapPartitions    每个executor一次拉取整个partition的数据并计算，若数据量过大可能会导致OOM
mapValues   保留key值不变，对values应用函数
glom    将rdd中元素按照partition划分并返回（一般用于测试分区结果）
partitionBy
reduce      
reduceByKey 按key分组并reduce。会默认按哈希分区
repartition 调整分区。shuffle版的coalesce


自身聚合
aggregate
aggregateByKey
cogroup 按key聚合，并合并values
combineByKey
groupBy 按照指定函数返回的key分组

关联
cartesian 两个rdd元素一一计算笛卡尔积,生成一个[(a11, b11)..]的kv list
intersection    计算交集
fullOuterJoin
leftOuterJoin
rightOuterJoin





>https://www.cnblogs.com/fillPv/p/5392186.html
