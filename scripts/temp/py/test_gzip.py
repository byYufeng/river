#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-09-24 16:15:45
Last modify: 2019-09-24 16:15:45
"""

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import time, json, traceback
from cStringIO import StringIO
import gzip, base64


def main():
    s = 'Hahaha!I\'m sososososo happy'
    bs = gzip_compress(s)
    bs_b64 = base64.b64encode(bs)
    bs_2 = base64.b64decode(bs_b64)
    s_2 = gzip_decompress(bs)

    print s, len(s)
    print bs, len(bs)
    print bs_b64, len(bs_b64)
    print bs_2, len(bs_2)
    print s_2, len(s_2)
     

def gzip_compress(r_data):
    buf = StringIO()
    zip_file = gzip.GzipFile(mode='wb', fileobj=buf)
    try:
        zip_file.write(r_data)
    finally:
        zip_file.close()
    return buf.getvalue()


def gzip_decompress(c_data):
    buf = StringIO(c_data)
    zip_file = gzip.GzipFile(mode='rb', fileobj=buf)
    try:
        r_data = zip_file.read()
    finally:
        zip_file.close()
    return r_data


if __name__ == "__main__":
    main()
