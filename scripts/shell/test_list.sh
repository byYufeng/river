#!/bin/bash
#Author: fsrm

#array1
a1=(1 3 5)

#array2
a2[1]="11";
a2[2]="22";

# iter by element
for v in ${a1[@]}
do
    echo $v
done

# iter by index
for i in ${!a2[@]}
do
    echo ${a2[$i]}
done

# short line
for i in ${!a2[@]}; do echo ${a2[$i]}; done
#https://www.coder4.com/archives/3853
