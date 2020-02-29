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
sys.path.append(os.getenv("HOME")+"/riven/utils")

import time, json, traceback
import common


def main():
    last_key = None
    count = 0 

    for _line in sys.stdin:
        line = _line.strip()
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
        print '%s\t%s' % (last_key, count)


def output(*args):
    common.print_split([*args])


if __name__ == "__main__":
    main()
