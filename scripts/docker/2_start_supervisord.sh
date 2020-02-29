#!/bin/bash
#Author: fsrm

docker run -itd \
    --restart=on-failure:3 \
    --name centos7 \
    centos7:fsrm_base \
    bash
