-- Author: fsrm
-- https://cwiki.apache.org/confluence/display/Hive/GettingStarted#GettingStarted-DDLOperations

-- fgg_test1
create table ft1(id int, name string, age int);
insert into table ft1 values (1, 'bbb', 23);

-- fgg_test2
create table ft2(id int, name string, age int) partitioned by (province string);
