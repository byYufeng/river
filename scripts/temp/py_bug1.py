#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2020-01-03 12:44:02
Last modify: 2020-01-03 12:44:02
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import time, json, traceback

# 如果不声明x为局部变量，在函数中可以正常读取/赋值，但若在判断语句中赋值则会出现问题（将这个变量当作局部变量对待）
# 全程使用global则可解决
#global x
x = None
def main():
    a() 

def a():
    #global x
    print x
    if x == 1:
        print 1
    else:#
        x = 0# 


if __name__ == "__main__":
    main()

