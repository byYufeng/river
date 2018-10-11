#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-10-11 18:45:48
Last modify: 2018-10-11 18:59:29
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json

def main():
    with open('todo') as fin:
        for info in enumerate(fin):
            print info 

if __name__ == "__main__":
    main()
