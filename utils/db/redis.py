#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-14 12:19:29
Last modify: 2018-09-03 12:10:12
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
import redis

class REDIS_CLIENT():

    def __init__(self, config):
        self.redis_client = redis.Redis(
                                #connection_pool=redis.BlockingConnectionPool(
                                connection_pool=redis.ConnectionPool(
                                                        max_connections=config['connections'],
                                                        host=config['host'],
                                                        port=config['port'],
                                                        db=config['db'])
                            )


    def set(self, k, v, **kwargs):
        self.redis_client.set(k, v, **kwargs)
        return None

    def get(self, k):
        return self.redis_client.get(k)

    def delete(self, k):
        return self.redis_client.delete(k)


def main():
    redis_config = {
        'host':'127.0.0.1',
        'port':9221,
        'db': 0,
        'connections':100
    }
    
    redis_client = REDIS_CLIENT(redis_config)
    redis_client.set('name', 'laozhang')
    print redis_client.get('name')
    print redis_client.delete('name')
    print redis_client.get('name')


if __name__ == "__main__":
    main()

