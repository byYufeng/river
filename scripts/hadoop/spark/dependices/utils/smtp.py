#!/usr/bin/env python
#coding:utf-8
"""
Author: rainwind
Create Time: 2017-05-12 18:55:50
Last modify: 2017-05-19 16:57:10
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def main():

    def _format_addr(s):
        # s = 'name <addr@example.com>'
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    smtp_server = 'smtp-mail.outlook.com'
    stmp_port = 587
    smtp_address = 'riven666666666@outlook.com'
    smtp_passwd = 'riven666'

    subject = 'hello'
    content = 'haha!nice 2 meet u'
    msg_from = 'riven@outlook.com'
    msg_to = 'riven666666666@outlook.com'
    #msg_to = 'riven666@yopmail.com'

    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = msg_from
    msg['To'] = msg_to
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, stmp_port)
    server.starttls()
    server.set_debuglevel(1)
    server.login(smtp_address, smtp_passwd)
    server.sendmail(smtp_address, [msg_to], msg.as_string())
     
    #http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000

if __name__ == "__main__":
    main()
