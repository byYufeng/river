#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-04-02 17:45:05
Last modify: 2019-04-02 17:45:05
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time
import traceback, json
from pprint import pprint
from mail_interface import send_mail
from pprint import pprint


def main():
    f = '/tmp/hdfs_monitor_path'
    hdfs_list = []
    with open(f) as fin: 
        hdfs_list = fin.read().strip().split('\n')
        
    # 过滤掉注释和空行
    hdfs_list = filter(lambda x: not x.strip() == '', hdfs_list)
    hdfs_list = filter(lambda x: not x.strip().startswith('#'), hdfs_list)

    print 'Paths:'
    pprint(hdfs_list)
    print ''

    mail_content = ""
    for hdfs_path in hdfs_list:
        res = statistic(hdfs_path)
        print 'statisting:', hdfs_path
        ls_splited = [x.split('\t') for x in res[0]]
        du_splited = [x.split() for x in res[1]]
        matched_group = zip(ls_splited, du_splited)
        res = [[k[0][1], k[0][0], ''.join(k[1][:-1])] for k in matched_group]
        res = [map(lambda x: x.strip(), x) for x in res]
        res.reverse()

        mail_content += 'Path %s:\n' % hdfs_path
        for line in res:
            mail_content += '\t'.join(line)
            mail_content += '\n'
        mail_content += '\n'
    print mail_content

    mail_args = {
            'subject': 'hdfs_move_monitor(last 7 days)',
            'body': mail_content,
            'to': '',
            'cc': '',
            }
    send_mail(mail_args)


def statistic(hdfs_path):
    cmd_ls = "source /etc/profile && hdfs dfs -ls %s" % hdfs_path + " | awk '{printf \"%s %s\\t%s\\n\",$6,$7,$8}'" 
    cmd_du = 'source /etc/profile && hdfs dfs -du -h %s' % hdfs_path

    #filter_pipe = " | grep -v '[a-z]$' | tail -n7" 
    filter_pipe = " | tail -n7" 
    res = (
            os.popen(cmd_ls + filter_pipe, 'r', 1).readlines(),
            os.popen(cmd_du + filter_pipe, 'r', 1).readlines(),
        )

    # with stderr
    #from subprocess import PIPE,Popen
    #scanCmd_res = Popen(scanCmd, shell=True, stdout=PIPE, stderr=PIPE)
    #scanStdout, scanStderr = scanCmd_res.communicate()

    return res


if __name__ == "__main__":
    main()
