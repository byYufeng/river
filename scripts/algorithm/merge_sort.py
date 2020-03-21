#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2020-01-12 14:19:54
"""

import sys, os
import time, json, traceback
sys.path.append(".")


# 二分归并
def main():
    l = [7,3,5,2,6,1,9,4,3] 
    mergesort(l, 0, len(l)-1)
    print(l)


def mergesort(l, left, right):
    if right - left <= 1:
        # sort
        if l[left] > l[right]:
            # swap
            l[left] -= l[right]; l[right] += l[left]; l[left] = l[right] - l[left];
        return

    p = (right + left) / 2 
    mergesort(l, left, p)
    mergesort(l, p+1, right)
    merge(l, left, p, right)

from copy import deepcopy
def merge(l, left, p, right):
    t = deepcopy(l[left:p+1])
    x, y = 0, p+1
    while True:
        if x == len(t):
            break

        if y == right+1:
            break

        if l[y] <= t[x]:
            t.insert(x, l[y])
            x += 1
            y += 1
        else:
            x += 1

    t += l[y:right+1]
    l[left:right+1] = t

if __name__ == "__main__":
    main()
