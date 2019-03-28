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
import time, json, traceback


def main():
    data_date = os.getenv('DATA_DATE')
    for line in sys.stdin:
        input_line = line.strip()
        deal(input_line)


def deal(input_line):
    print(input_line)


if __name__ == "__main__":
    main()
