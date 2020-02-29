create database fsrm;
use fsrm;
create table ft1(id int, name varchar(30), subject varchar(30), score int);

-- connect: mysql -D fsrm -pmysql
load data local infile 'ft1.txt' into table ft1 fields terminated by ',';

-- 行转列
-- k1=v1,k2=v2,k3=v3 ==> K1=v1,v21=v31,v22=v32
-- 以某一列为key分组聚合，然后使用 case when语句
-- (case original_column1 when new_column1 then original_column2) new_column1, 
-- (case original_column1 when new_column2 then original_column2) new_column2...的形式，然后用max、min等聚合函数取值
/*
+------+------+---------+-------+
| id   | name | subject | score |
+------+------+---------+-------+
|    1 | fgg  | math    |    95 |
|    2 | fgg  | art     |    82 |
|    3 | fgg  | sport   |    86 |
|    4 | gf1  | art     |    85 |
|    5 | gf1  | math    |    90 |
|    6 | gf2  | math    |    61 |
|    7 | gf3  | art     |    90 |
|    8 | gf3  | sport   |    80 |
+------+------+---------+-------+
to
+------+------+------+-------+
| name | math | art  | sport |
+------+------+------+-------+
| fgg  |   95 |   82 |    86 |
| gf1  |   90 |   85 |     0 |
| gf2  |   61 |    0 |     0 |
| gf3  |    0 |   90 |    80 |
+------+------+------+-------+
*/

select name, 
    max(case subject when 'math' then score else 0 END) 'math', 
    max(case subject when 'art' then score else 0 END) 'art', 
    max(case subject when 'sport' then score else 0 END) 'sport' 
from ft1 group by name;


-- 列转行
-- k1=v1,k2=v2,k3=v3,k4=v4 ==> K1=v1,K2=k2,k3..,K3=v2,v3...
-- 分别把B列的值统一成一个字段,再把A列分别硬编码以对应B列的值，然后用union合并起来
create table ft2  (select name, max(case subject when 'math' then score else 0 END) 'math', max(case subject when 'art' then score else 0 END) 'art', max(case subject when 'sport' then score else 0 END) 'sport' from ft1 group by name) ;

select name, 'math' as 'subject', math as 'score' from ft2 union (select name, 'art' as 'subject', art as 'score' from ft2) union (select name, 'sport' as 'subject', sport as 'score' from ft2) order by name;



-- 行聚合为列
-- ...group_concat(k)...group by k

-- 列拆分为行
-- mysql没有split to rows的函数，所以比较麻烦，略过
-- >https://xbuba.com/questions/17942508/sql-split-values-to-multiple-rows
-- >https://blog.csdn.net/fdipzone/article/details/76473148
