#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2017-07-27 16:41:05
Last modify: 2017-08-15 16:56:34
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def main():

    #global a
    #如果不声明global 在这里修改变量后会报错
    print a
    a = 2
    print a
     

if __name__ == "__main__":
    a = 1
    main()
