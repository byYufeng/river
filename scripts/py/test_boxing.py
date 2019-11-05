#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-12-26 15:02:59
Last modify: 2018-12-26 15:02:59
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json


def func(*args, **kwargs):
    print args
    print kwargs


def main():
    func(1, 2, a=3, b=4) # ok
    func([1, 2], {'a':3, 'b':4}) # error

    l = [1, 2]
    k = {'a':3, 'b':4}
    func(*l, **k) # ok


if __name__ == "__main__":
    main()
