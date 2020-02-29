#!/usr/bin/env python
#coding:utf-8
"""
Create Time: 2018-06-13 17:32:01
Last modify: 2018-12-08 21:01:48
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

rmq_config_local = { 
    'host' : '127.0.0.1',
    'port' : '5672', 
    'username' : 'guest', 
    'password' : 'guest',
    'vhost' : '/',
    'exchange_name' : '', 
    'exchange_type' : '', 
    'queue_name' : 'fsrm_test',
    'routing_key' : 'fsrm_test'
}   

redis_config_local = { 
    'max_connections' : 100,
    'host' : '127.0.0.1',
    'port' : 9221,
    'password' : '',
    'db' : 0,
}   
