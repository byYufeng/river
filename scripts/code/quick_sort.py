#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2020-01-12 14:19:54
"""

import sys, os
import time, json, traceback
sys.path.append(".")


def main():
    l = [3,2,5,6,7,3,1,9,4] 
    print(l)
    quicksort(l, 0, len(l)-1)
    print(l)

def quicksort(l, left, right):
    if left == right:
        return 

    flag = l[left]
    x, y = left, right
    while x<y:
        x += 1
        if l[x] > flag:
            while y>x:
                if l[y] < flag :
                    swap(l, x, y)
                    y -= 1
                    break
                y -= 1

    if l[x] > flag:
        swap(l, left, x-1)
    if l[x] < flag:
        swap(l, left, x)

    quicksort(l, left, x-1)
    quicksort(l, x, right)


def swap(l, x, y):
    if x != y:
        l[x] ^= l[y];l[y] ^= l[x];l[x] ^= l[y];


if __name__ == "__main__":
    main()
