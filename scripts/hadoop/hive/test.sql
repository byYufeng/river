-- Author: fsrm
-- https://cwiki.apache.org/confluence/display/Hive/GettingStarted#GettingStarted-DDLOperations

-- fgg_test
create table ft(id int, name string, age int);
insert into table ft1 values (1, 'bbb', 23);


-- fgg_test1
create table ft1(id int, name varchar(30), subject varchar(30), score int) row format delimited fields terminated by ',';
-- 相比于mysql，字段的分隔符由load data时定义改为create table时定义，并且加了row format delimited前缀
load data local inpath 'ft1.txt' into table ft1;

-- fgg_test2
create table ft2(id int, name string, age int) partitioned by (province string);

-- 相比mysql，子查询的字段和表的别名不可带引号
-- select max(case subject when 'math' then score else 0 END) 'math' from ft1;  X
-- select max(case subject when 'math' then score else 0 END) math from ft1;    √
-- select name, 'math' as 'subject', math as 'score' from ft2;                  X
-- select name, math subject, math score from ft2;                              √
