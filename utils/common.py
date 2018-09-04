#! coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import logging
from logging.handlers import RotatingFileHandler
import time

#一个value为list的dict
class Dlist(dict):
    def __init__(self):
        super(Dlist, self).__init__()

    def put(self, k, v):
        if k in self:
            self[k].append(v)
        else:
            self[k] = [v]

#装饰器：单例
def Singleton(cls, *args, **kwargs):
    instances = []
    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

#装饰器：try catch
def trycatch(cls, *args, **kwargs):
    def wrapper():
        try:
            cls(*args, **kwargs)
        except Exception, e:
            pass
    return wrapper()

#逐行处理文件
def readin():
    with open(f) as fin:
        for line in fin:
            line = line.strip()
            func(line)

# 批量处理数据 data: iteraotr or stdin
def batch(func, data, size):
    cnt = 0 
    temp_data_list = []
    for _data in data:
        temp_data_list.append(_data)
        cnt += 1
    
        if cnt % size == 0:
            func(temp_data_list)
            temp_data_list = []

    if len(temp_data_list) > 0:
        func(temp_data_list)


class Utils(object):

    def __init__(self):
        self.ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'

    # 设置日志,输出到文件和控制台
    def getLogger(self, path='', maxSize=1000000000):
        if path:
            filename = path.strip().split('/')[-1]
        else:
            filename = sys.argv[0].split('.')[0]
            filename = sys.argv[0]#.split('.')[0]
            path = './%s.log' % filename
        logger = logging.getLogger(filename)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh = RotatingFileHandler(path, maxBytes=maxSize, backupCount=1000)
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    # 时间转换
    def timestamp_to_formatter_string(self, timestamp, formatter=''):
        formatter = self.ISOTIMEFORMAT if not formatter else formatter
        return time.strftime(formatter, time.localtime(timestamp))

    def formatter_string_to_timestamp(self, formatter_string, formatter = ''):
        formatter = self.ISOTIMEFORMAT if not formatter else formatter
        return time.mktime(time.strptime(formatter_string, formatter))


    # 正则
    def regex_rule():
        regex_dic = { 
                    'ip' : re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])(:\d{4})?'),
                    'url' : re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
                    }  
        return regex_dic
