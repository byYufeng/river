#!/bin/bash
#Author: fsrm

input=$1
mapper=map.py
reducer=reduce.py

cat $input | python $mapper | python $reducer
