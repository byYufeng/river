#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('.')
sys.path.append(os.getenv('HOME')+'/riven')

from utils.common import Logger

def main():
    logger = Logger.getLogger()
    logger.debug(111)

if __name__ == "__main__":
     main()

