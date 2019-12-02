#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2017-08-15 16:29:01
Last modify: 2017-08-15 16:32:43
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

#执行shell命令并获取输出结果
def main():
    cmd = 'ls'
    res = os.popen(cmd).read().strip("\n").split("\n")

    for o in res:
        print o
        #os.system(cmd)
 

if __name__ == "__main__":
    main()
