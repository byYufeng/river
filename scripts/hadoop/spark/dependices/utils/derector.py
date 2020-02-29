#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-12-27 16:56:47
Last modify: 2019-12-27 16:56:47
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")
sys.path.append(os.getenv("HOME")+"/riven/utils")
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

import time, json, traceback


def main():
    #a = costtime(func);a()
    #costtime(func)()
    pass


def costtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print 'start time:', start_time
        data_size = func(*args, **kwargs)
        end_time = time.time()
        print 'end time:', end_time
        print 'data size: %s\tcost time: %s\tqps: %s' % ( 
            data_size, end_time - start_time, data_size / (end_time - start_time))
    return wrapper


@costtime
def func(end, start=0):  
    for i in range(start, end):
        print i
        time.sleep(0.01)
    return end-start

func(20)

