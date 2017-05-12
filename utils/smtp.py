#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2017-05-12 18:55:50
Last modify: 2017-05-12 19:23:44
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import smtplib
from email.mime.text import MIMEText

def main():


    smtp_server = 'smtp.zoho.com.cn'
    stmp_port = 465
    smtp_address = 'riven666'
    smtp_passwd = 'riven999'

    msg = 'haha'
    address_to = 'riven666@zohu.com.cn'

    content = MIMEText(msg, 'html', 'utf-8')
    server = smtplib.SMTP(smtp_server, stmp_port)
    server.set_debuglevel(1)
    server.login(smtp_address, smtp_passwd)
    server.sendmail(smtp_address, [address_to], msg.as_string())
     
    #http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000

if __name__ == "__main__":
    main()
