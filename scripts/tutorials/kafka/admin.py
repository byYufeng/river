#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-01-10 13:58:55
Last modify: 2019-01-10 13:58:55
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
from kafka import *


def main():
    kafka_configs = { 
        'bootstrap_servers' : ['127.0.0.1:9092'], 
    }   
    admin_client = KafkaAdminClient(**kafka_configs)

    print admin_client.delete_topics(['test'])


if __name__ == "__main__":
    main()
