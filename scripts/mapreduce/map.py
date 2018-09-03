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
    for line in sys.stdin:
        line = line.strip()
        cols = line.split('\t', 1)
        k, v = cols[0], cols[1]
        print('%s\t%s' % (k, v))


if __name__ == "__main__":
    main()

    try:
        pass
    except Exception, e:
        ex = traceback.format_exc()
        sys.err.write(ex)
