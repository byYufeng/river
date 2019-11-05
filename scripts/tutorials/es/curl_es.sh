#!/bin/bash
#Author: fsrm

USER="elastic"
PASS=""
curl -XGET -u $USER:$PASS http://127.0.0.1:9200/_cat/indices?v
