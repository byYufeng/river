#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-09-20 16:47:49
Last modify: 2019-09-20 16:47:49
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import time, json, traceback


def main():
    last_key = None
    count = 0 

    for map_output_line in sys.stdin:
        line = map_output_line.rstrip()
        k, v = line.split('\t', 1)

        v = int(v)
        if k == last_key:
            count += v
        else:
            if last_key:
                output(last_key, count)
            last_key = k 
            count = v 

    if last_key:
        output(last_key, count)


def output(*args):
    def print_split(_list, seperator="\t"):
        return seperator.join(['%s'] * len(_list)) % tuple(_list)

    print print_split(args)


if __name__ == "__main__":
    main()
