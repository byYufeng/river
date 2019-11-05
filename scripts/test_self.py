#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-09-17 18:12:07
Last modify: 2019-09-17 18:12:07
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import time, json, traceback

class A():
    a = 1
    #self.b = 2

    def aa(self):
        print self.a
        #print self.b


def main():
    print A().a
    #print A().b
    A().aa()


if __name__ == "__main__":
    main()
