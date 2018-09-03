#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-09-03 18:56:05
Last modify: 2018-09-03 19:08:00
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json

def main():
    l = [x for x in range(95)] 
    print l

    def batch(func, data, size):
        cnt = 0
        temp_data_list = []
        for _data in data:
            temp_data_list.append(_data)
            cnt += 1
            
            if cnt % size == 0:
                func(temp_data_list)
            temp_data_list
            
        
            
            

if __name__ == "__main__":
    main()
