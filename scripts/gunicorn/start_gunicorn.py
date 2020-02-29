#!/bin/python
# -*- coding: utf-8 -*-
import re
import sys 

from gunicorn.app.wsgiapp import run 

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(run())

    #usage: python start_gunicorn.py -w 8 -b 0.0.0.0:6081 index(module_name):app(app_name)
