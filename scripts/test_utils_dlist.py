#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('..')

import os
import utils

def main():
    dl = utils.Dlist()
    dl.put(1, 3)
    print dl
    dl.put(1, 4)
    print dl
    dl[2] = 5
    print dl
    dl[1] = 6
    print dl
     

if __name__ == "__main__":
     main()
