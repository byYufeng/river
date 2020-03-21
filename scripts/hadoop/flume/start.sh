#!/bin/bash
#Author: fsrm

bin/flume-ng agent --conf conf --conf-file conf/test.conf --name a1 -Dflume.root.logger=INFO,console
