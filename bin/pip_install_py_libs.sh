#!/bin/bash
#Author: fsrm

# export: pip freeze 
root_path=`readlink -f .`/..
mkdir -p $root_path/libs/python
pip install -r $root_path/config/py_module_requirements.txt -t $root_path/libs/python
