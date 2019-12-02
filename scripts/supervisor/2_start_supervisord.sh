#!/bin/bash
#Author: fsrm

docker run -d \
    --restart=on-failure:10 \
    -v ~/riven/scripts/supervisor/conf/supervisord.conf:/etc/supervisor/supervisord.conf \
    -v ~/riven/scripts/supervisor/conf/conf.d:/etc/supervisor/conf.d \
    -v ~/riven/scripts/supervisor/projects:/projects \
    --name supervisor \
    centos7:supervisor \
    /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
