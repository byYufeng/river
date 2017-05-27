#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2017-05-27 12:32:31
Last modify: 2017-05-27 12:42:43
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def main():
    def select(conn, sql):
        print 11

    sql = ('select *', ['a'])
    select(0, sql)

if __name__ == "__main__":
    main()
