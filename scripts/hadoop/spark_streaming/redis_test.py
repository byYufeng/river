#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-11-28 11:59:01
Last modify: 2019-11-28 11:59:01
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")
sys.path.append(os.getenv("HOME")+"/riven/utils")
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

import time, json, traceback
from db._redis import * 


def main():
    r = REDIS_CLIENT().redis_client
    #print r.incr("a",5)
    print r.mget("a", "b")


if __name__ == "__main__":
    main()
