#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-31 19:35:21
Last modify: 2018-09-04 17:08:29
"""


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../libs/py')
sys.path.append('..')


import os, time
import traceback, json


def test_redis():
    from utils.db._redis import REDIS_CLIENT
    from utils.common import batch
    redis_config = { 
        'host':'127.0.0.1',
        'port':9221,
        'db': 0,
        'connections':100
    }   
    
    redis_client = REDIS_CLIENT(redis_config)
    l = [
        [['set'], ['name', 'bbb']],
        [['set'], ['age', '26']],
        [['set'], ['addr', 'jjjjjj']],
        [['delete'], ['addr']],
    ]

    #redis_client.batch(l)
    batch(redis_client.batch, l, 3)
    return

    redis_client.set('name', 'laozhang')
    print redis_client.get('name')
    print redis_client.delete('name')
    print redis_client.get('name') 


def main():
    test_redis()


if __name__ == "__main__":
    main()
