#!/bin/bash
#Author: fsrm

USER='root'
PASSWORD='mysql'
docker exec -it mysql mysql -u$USER -p$PASSWORD
