#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-15 19:38:53
Last modify: 2018-10-11 18:26:06
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
        if param != None:
            results.append(pool.apply(func, [param]))
        else:
            results.append(pool.apply(func))
    pool.close()
    pool.join()

    return results


def multi_async(func, params, process_num):
    pool = multiprocessing.Pool(processes=process_num)
    results = []
    for param in params:
        if param != None:
            results.append(pool.apply_async(func, [param]))
        else:
            results.append(pool.apply_async(func))
    pool.close()
    pool.join()

    #异步并发时需要通过get拿到返回结果
    #print results
    results = [res.get() for res in results]
    return results


# 用此方式时自定义函数需把参数都放在一个变量里以方便进程池调用
# 有参
def func(params):
    print('params:%s' % params)
    res = [x for x in params]
    return res

# 无参
def func2():
    print('params:%s' % 'NOT EXIST')
    return None


def main_test():
    process_num = 16
    #params = [x for x in range(100)]
    #params = [[x, x+1] for x in range(100)]
    params = [[] for i in range(10)]
    #print params
    #print walk(func, params)
    print multi_sync(func, params, process_num)
    print 'sync finished'
    print multi_async(func, params, process_num)
    print 'async finished'
    print 

    print multi_sync(func2, [None] * 10 , process_num)
    print 'sync finished'
    print multi_async(func2, [None] * 10, process_num)
    print 'async finished'


def main():
    #main_test()
    pass
    
def func(in_str):
    in_str = in_str.strip()
    return in_str
    
with open('config.py') as fin:
    print(multi_async(func, fin, 4))
        

if __name__ == "__main__":
    main()
