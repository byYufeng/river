#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import traceback, raise_ 
    #raise_.main()

    try:
        raise_.main()
    except:
        print 0

    try:
        raise_.main()
    except:
        ee = traceback.format_exc()
        print ee

    try:
        raise_.main()
    except:
        ee = traceback.print_exc()
        print ee

    while 1:
        pass

if __name__ == "__main__":
    main()

