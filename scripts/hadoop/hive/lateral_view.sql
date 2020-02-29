create table users(id int, tags string) row format delimited fields terminated by '|';
load data local inpath 'lateral_view.txt' into table users;
select * from users;
select users.id, t.* from users lateral view explode(split(tags, ',')) t as col;
select users.id, col from users lateral view explode(split(tags, ',')) t as col;

-- 在hive中使用explode等UDTF函数时，不允许再select其他字段。所以此时应使用Lateral view，将UDTF生成的结果生成一个虚拟表，然后这个虚拟表会和输入行进行join，来达到连接UDTF外的select字段的目的
-- lateral view explode() t as c： t为表，c为字段
-- >https://my.oschina.net/u/3754001/blog/3028523

-- data: array
create table users_array(id int, tags array<string>) row format delimited fields terminated by '|' collection items terminated by ',';
load data local inpath 'lateral_view.txt' into table users_array;
select * from users_array;
select users.id, t.* from users_array lateral view explode(tags) t as col;
