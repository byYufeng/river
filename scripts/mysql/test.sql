create database fsrm;
use fsrm;
create table ft1(id int, name varchar(30), age int, area varchar(30));

-- connect: mysql -D fsrm -pmysql
load data local infile 'ft1.txt' into table ft1 fields terminated by ',';
