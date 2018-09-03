#!/usr/bin/env python
#coding:utf-8
"""
Create Time: 2018-06-13 17:32:01
Last modify: 2018-08-31 19:23:41
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

rmq_config_local = { 
    'host' : '127.0.0.1',
    'port' : '5672', 
    'user' : 'guest', 
    'passwd' : 'guest',
    'p1' : '/',
    'exchange_name' : '', 
    'exchange_type' : '', 
    'queue_name' : 'fsrm_test',
    'routing_key' : 'fsrm_test'
}   

redis_config_local = { 
    'host' : '127.0.0.1',
    'port' : 9221,
    'db' : 0,
    'connections' : 100
}   
