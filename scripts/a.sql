---group by;
select family, count(*), date(insert_time) from table_ where date(insert_time) = date_sub(curdate(), interval 1 day) group by family;
