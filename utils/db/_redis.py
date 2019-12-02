#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-14 12:19:29
Last modify: 2018-12-09 02:52:33
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
import redis

class REDIS_CLIENT():
    def __init__(self, config={}):
        #self.connection_pool = redis.ConnectionPool(
        self.connection_pool = redis.BlockingConnectionPool(
                host=config.get('host', '127.0.0.1'),
                password=config.get('password', ''),
                port=int(config.get('port', 6379)),
                db=config.get('db', 0),
                max_connections=int(config.get('connections', 100))
        )
        self.redis_client = redis.Redis(connection_pool=self.connection_pool)

    # 不同的type key不能相同
    # String
    # set params: ex/px: expire time for seconds/miliseconds 
    # set params: nx/xx: only insert/only update (default:upsert)
    def set(self, k, v, **kwargs):
        self.redis_client.set(k, v, **kwargs)
        return None

    def get(self, k):
        return self.redis_client.get(k)

    def delete(self, k):
        return self.redis_client.delete(k)

    def incr(self, k, amount=1):
        return self.redis_client.incr(k) # return value after opration

    def scan(self, **kwargs):
        return self.redis_client.scan(**kwargs)

    ## hash:hset/hget/hmset/hmget/hgetall/hdel/hscan
    ## list:

    # Util
    def count(self):
        return self.redis_client.dbsize()

    def keys(self):
        return self.redis_client.keys()

    def truncate(self):
        return self.redis_client.flushdb()

    # batch [[[set], ['name', 'b']], [['set'], ['age', '23']]]
    def batch(self, operations):
        with self.redis_client.pipeline(transaction=False) as p:
            for operation in operations:
                #print operation
                handle = operation[0][0]
                k = operation[1][0]
                if len(operation[1]) > 1:
                    v = operation[1][1]

                if handle == 'set':
                    p.set(k, v)
                if handle == 'delete':
                    p.delete(k)
            p.execute()

def main():
    redis_config = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'connections':100
    }

    redis_client = REDIS_CLIENT(redis_config)
    redis_client.set('name', 'laozhang')
    print redis_client.get('name')
    print redis_client.delete('name')
    print redis_client.get('name')

    _batch = [
        [['set'], ['name', 'bbb']],
        [['set'], ['age', '26']],
        [['set'], ['addr', 'jjjjjj']],
        [['delete'], ['addr']],
    ]
    redis_client.batch(_batch)
    return


if __name__ == "__main__":
    main()
