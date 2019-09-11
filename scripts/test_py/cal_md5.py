#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-06-03 11:33:56
Last modify: 2019-06-03 11:33:56
"""

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json


def main():
    import hashlib

    m = hashlib.md5()
    m.update("123")
    print m.hexdigest()

    m = hashlib.md5("123")
    print m.hexdigest()

    print hashlib.md5("123").hexdigest()


if __name__ == "__main__":
    main()
