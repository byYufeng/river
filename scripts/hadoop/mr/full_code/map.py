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
    cols = line.split('\t', 1)
    k = cols[0]
    v = line
    print('%s\t%s' % (k, v)) 


if __name__ == "__main__":
    main()
