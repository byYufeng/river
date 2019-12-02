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
import time, json, traceback


def main():
    for map_output_line in sys.stdin:
        line = map_output_line.strip()
        deal(line)


def deal(line):
    reduce_input_columns = line.split('\t', 1)
    reduce_k = reduce_input_columns[0]
    print('%s\t%s' % (reduce_k, map_output_line))


if __name__ == "__main__":
    main()
