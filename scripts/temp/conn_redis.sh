#!/bin/bash
#Author: fsrm

redis_path='.'

host=''
port=''
password=''

$redis_path/src/redis-cli -h $host -p $port -a $password
