#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2020-01-13 17:34:09
"""

import sys, os
sys.path.append(".")
sys.path.append(os.getenv("HOME")+"/riven/utils")
sys.path.append(os.getenv("HOME")+"/riven/libs/python")

import time, json, traceback, random, string


def main():
    #filename = 'random.txt'
    line_length = 32
    file_size = 1 << 30 * 16 #G
    for x in range(file_size):
        print(''.join(random.sample(string.ascii_letters + string.digits, line_length-1)))


if __name__ == "__main__":
    main()
