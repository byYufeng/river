#!/usr/bin/env python
#coding:utf-8
"""
Create Time: 2018-06-13 17:32:01
Last modify: 2018-12-08 20:34:08
"""

import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/dependices')

import time, json, traceback


def main():
    for input_line in sys.stdin:
        line = input_line.strip()
        deal(line)


def deal(line):
    #k, v = line.split('\t', 1)
    #print('%s\t%s' % (k, v)) 

    k = line.split('\t', 1)[0]
    print('%s\t%s' % (k, line)) 
    #for x in os.walk('.'): print x;


if __name__ == "__main__":
    main()
