#!/bin/bash
#Author: fsrm

docker run -itd --name mysql -e MYSQL_ROOT_PASSWORD=mysql -p 3386:3306 mysql:5.7
