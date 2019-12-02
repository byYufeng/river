#! /usr/bin/env python
# coding:utf-8
"""
Author: fsrm
Create Time: 2019-06-10 20:43:13
Last modify: 2019-06-10 20:43:13
"""

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import json, time, traceback
from datetime import datetime


def main():
    try:
        input_file = os.environ['mapreduce_map_input_file']
    except KeyError:
        input_file = os.environ['map_input_file']


if __name__ == "__main__":
    main()
