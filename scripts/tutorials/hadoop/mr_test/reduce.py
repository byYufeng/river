#!/usr/bin/env python
#coding:utf-8
"""
Create Time: 2018-06-13 17:32:01
Last modify: 2018-12-08 20:39:58
"""

import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/dependices')

import time, json, traceback
from utils.common import *


def main():
    def bulk_func(docs):
        for doc in docs:
            print doc

    batch(sys.stdin, deal, bulk_func)


def deal(map_output_line):
    line = map_output_line.strip()
    #k, v = line.split('\t', 1)
    k = line.split('\t', 1)[0]
    return k


if __name__ == "__main__":
    main()
