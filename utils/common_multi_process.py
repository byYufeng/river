#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-15 19:38:53
Last modify: 2018-08-15 19:38:53
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
import multiprocessing


def walk(func, params):
    results = []
    for param in params:
        results.append(apply(func, [param]))
    return results


def multi_sync(func, params, process_num):
    pool = multiprocessing.Pool(processes=process_num)
    results = []
    for param in params:
        results.append(pool.apply(func, [param]))
    pool.close()
    pool.join()

    return results


def multi_async(func, params, process_num):
    pool = multiprocessing.Pool(processes=process_num)
    results = []
    for param in params:
        #print param
        if param:
            results.append(pool.apply_async(func, [param]))
        else:
            results.append(pool.apply_async(func))
    pool.close()
    pool.join()

    results = [res.get() for res in results]
    return results


def func(params):
    print('params:%s' % params)
    #params = params + params ** 2 + params ** 3
    return params

def func2():
    print(0)
    #params = params + params ** 2 + params ** 3
    return None

def main():
    process_num = 16
    params = [x for x in range(100)]
    params = [[x, x+1] for x in range(100)]
    #print params
    #print walk(func, params)
    print multi_sync(func, params, process_num)
    #print multi_async(func, params, process_num)
    #print multi_async(func2, [[] for i in range(10)], process_num)
        

if __name__ == "__main__":
    main()
