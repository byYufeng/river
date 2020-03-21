#!/bin/bash
#Author: fsrm

docker run -d --name redis -p 6379:6379 --restart=always redis redis-server
