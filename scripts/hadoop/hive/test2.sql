-- 行列转换：完全同mysql（但是需注意字段和表的别名不能带引号的语法区别）

-- 列转行
-- 以某一列为key，剩下所有列当做一个字段，每个字段对应的值当做一个字段，把一行的每一列都拆分为一条数据。同样只适于三个字段维度
-- k1=v1,k2=v2,k3=v3,k4=v4 ==> K1=v1,K2=k2,k3..,K3=v2,v3...
-- 分别把B列的值统一成一个字段,再把A列分别硬编码以对应B列的值，然后用union合并起来

(select name, math subject, math score from ft2) union
(select name, art subject, art score from ft2) union 
(select name, sport subject, sport score from ft2) order by name;

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
↑
↓
+------+------+------+-------+
| name | math | art  | sport |
+------+------+------+-------+
| fgg  |   95 |   82 |    86 |
| gf1  |   90 |   85 |     0 |
| gf2  |   61 |    0 |     0 |
| gf3  |    0 |   90 |    80 |
+------+------+------+-------+
*/

-- 行转列
-- 以某一列为key分组聚合，然后把它的每个值当做一列，使用 case when语句构造每一列。仅适用于有三个字段的情况。
-- k1=v1,k2=v2,k3=v3 ==> K1=v1,v21=v31,v22=v32
-- (case original_column1 when new_column1 then original_column2) new_column1, 
-- (case original_column1 when new_column2 then original_column2) new_column2...的形式，然后用max、min等聚合函数取值
select name, 
    max(case subject when 'math' then score else 0 END) math, 
    max(case subject when 'art' then score else 0 END) art, 
    max(case subject when 'sport' then score else 0 END) sport 
from ft1 group by name;
--create table ft2 as (select name, max(case subject when 'math' then score else 0 END) math, max(case subject when 'art' then score else 0 END) art, max(case subject when 'sport' then score else 0 END) sport from ft1 group by name) ;

-- 不存在的值用null而不是0填充 
--create table ft22 (select name, max(case subject when 'math' then score else null END) 'math', max(case subject when 'art' then score else null END) 'art', max(case subject when 'sport' then score else null END) 'sport' from ft1 group by name) ;



-- 行聚合为列
-- ...group_concat(k)...group by k


-- 列拆分为行
-- explode
