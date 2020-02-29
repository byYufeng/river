#!/bin/bash
#Author: fsrm

"""
a
b
a
"""

"""
['a': 2],
['b': 1]
"""

awk '{a[$1]+=1;} END{for(i in a) print i,a[i]}' | sed -e 's/\(.*\) \(.*\)/["\1", \2],/'

