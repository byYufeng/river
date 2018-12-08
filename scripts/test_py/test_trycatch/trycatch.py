#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2018-07-10 18:52:05
Last modify: 2018-07-12 10:42:11
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json


#捕获异常并将详细信息输出到stderr
def main():
    try:
        print 1/0
    except Exception, e:
        ex = traceback.format_exc()
        sys.stderr.write(ex)
        sys.stderr.write("\n")
 

if __name__ == "__main__":
    main()
    main()
