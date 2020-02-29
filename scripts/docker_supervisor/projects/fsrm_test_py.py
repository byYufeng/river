#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-12-02 16:02:31
Last modify: 2019-12-02 16:02:31
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")
sys.path.append(os.getenv("HOME")+"/riven/utils")
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

import time, json, traceback


def main():
    while 1:
        os.system('mkdir /tmp/test;cd /tmp/test;touch "`date`"')


if __name__ == "__main__":
    main()
