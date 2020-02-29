#!/bin/bash
#Author: fsrm

# 性能很差 只适用于小文件
FILENAME="f.txt"
#1024**3=1073741824/G
FILESIZE=10737418240
LINE_LENGTH=32

let n=$FILESIZE/$LINE_LENGTH
let i=0
#for i in `seq $n`
while [ $i -lt $n ]
do
    echo `date +%s%N | md5sum | head -c31` >> $FILENAME
    let i=i+1
done

