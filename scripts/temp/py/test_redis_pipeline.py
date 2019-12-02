#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-31 19:35:21
Last modify: 2018-09-03 17:09:20
"""


import sys
sys.path.append('../libs/py')
sys.path.append('..')


import os, time
import traceback, json


import redis
import time
from concurrent.futures import ProcessPoolExecutor

r = redis.Redis(host='127.0.0.1', port=9221)


def try_pipeline():
    start = time.time()
    with r.pipeline(transaction=False) as p:
        p.sadd('seta', 1).sadd('seta', 2).srem('seta', 2).lpush('lista', 1).lrange('lista', 0, -1)
        p.execute()
    print(time.time() - start)


def without_pipeline():
    start = time.time()
    r.sadd('seta', 1)
    r.sadd('seta', 2)
    r.srem('seta', 2)
    r.lpush('lista', 1)
    r.lrange('lista', 0, -1)
    print(time.time() - start)


def worker():
    while True:
        #try_pipeline()
        without_pipeline()

with ProcessPoolExecutor(max_workers=12) as pool:
    for _ in range(10):
        pool.submit(worker)
