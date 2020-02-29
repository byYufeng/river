#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2020-02-09 01:41:53
"""

import sys, os
sys.path.append(".")
sys.path.append(os.getenv("HOME")+"/riven/utils")
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

import time, json, traceback


def main():
    a = {"a":1}
    b = {"b":2}

    a = {11:1}
    b = {22:2}

    a.update(b);print(a) #原地更新，不推荐
    print(dict(a, **b)) #推荐，但仅限python2，python3中需限定key为string
    print({**a, **b}) #推荐，但仅限python3


if __name__ == "__main__":
    main()
