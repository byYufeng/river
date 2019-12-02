#!/bin/bash
#Author: fsrm

docker run --name supervisor --restart=on-failure:10 -v ~/projects/supervisor/conf/supervisord.conf:/etc/supervisor/supervisord.conf -v ~/projects/supervisor/conf/conf.d:/etc/supervisor/conf.d -v ~/projects/supervisor/projects:/projects docker.io/kdelfour/supervisor-docker
