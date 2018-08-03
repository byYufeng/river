#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('..')

import os
import utils

def main():
    logger = utils.Utils().getLogger()
    logger.info(123)

if __name__ == "__main__":
     main()

