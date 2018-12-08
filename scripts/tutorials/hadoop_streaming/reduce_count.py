#!/usr/bin/env python
#coding:utf-8
"""
Create Time: 2018-06-13 17:32:01
Last modify: 2018-06-14 16:28:21
"""

import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getcwd())
import time, json, traceback


def main():
    last_k = ''
    cnt = 1
    for line in sys.stdin:
        line = line.strip()
        k, v = line.split('\t', 1)

        # uniq
        if k == last_k:
            cnt += 1
            continue
        else:
            print('%s\t%s\t%s' % (k, v, 'count:%s'%count))
            last_k = k
            cnt = 1


if __name__ == "__main__":
    main()
