#!/bin/bash
#Author: fsrm

# export: pip freeze 
mkdir -p ../libs/py
pip install -r ../config/py_module_requirements.txt -t ../libs/py
