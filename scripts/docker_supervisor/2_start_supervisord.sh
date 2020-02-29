#!/bin/bash
#Author: fsrm

docker run -d \
    --restart=on-failure:3 \
    -v ~/riven/scripts/supervisor/conf/supervisord.conf:/etc/supervisor/supervisord.conf \
    -v ~/riven/scripts/supervisor/conf/conf.d:/etc/supervisor/conf.d \
    -v ~/riven/scripts/supervisor/projects:/projects \
    -v ~/riven/scripts/supervisor/logs:/var/log/supervisor \
    --name supervisor \
    centos7:supervisor \
    /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
