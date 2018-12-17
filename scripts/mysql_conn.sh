#!/bin/bash

mysql_path=''
host=''
port=''
username=''
password=''
db_name=''

$mysql_path/bin/mysql -h$host -P$port -u$username -p$password $db_name
