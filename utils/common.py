#! coding:utf-8

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time, traceback, json
import multiprocessing

import logging
from logging.handlers import RotatingFileHandler


class Utils(object):

    def __init__(self):
        pass


#*********************************************Logger*****************************************
class Logger(object):
    @staticmethod
    # 设置文件路径,输出到文件和控制台
    def getLogger(path='', maxSize=1000000000):
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


# ******************************************Multi process**********************************************
# 单进程遍历执行
def single_process(func, params):
    results = []
    for param in params:
        results.append(apply(func, [param]))
    return results

# 多进程同步执行
def multi_sync(func, params, process_num):
    pool = multiprocessing.Pool(processes=process_num)
    results = []
    for param in params:
        if param != None:
            results.append(pool.apply(func, [param]))
        else:
            results.append(pool.apply(func))
    pool.close()
    pool.join()
    return results

# 多进程异步执行
def multi_async(func, params, process_num):
    pool = multiprocessing.Pool(processes=process_num)
    results = []
    for param in params:
        if param != None:
            results.append(pool.apply_async(func, [param]))
        else:
            results.append(pool.apply_async(func))
    pool.close()
    pool.join()

    #异步并发时需要通过get拿到返回结果
    #print results
    results = [res.get() for res in results]
    return results


# 返回按分隔符分隔列表元素的字符串:
def print_split(_list, seperator):
    return seperator.join(['%s'] * len(_list)) % tuple(_list)


#一个value为list的dict
class Dlist(dict):
    def __init__(self):
        super(Dlist, self).__init__()

    def put(self, k, v):
        if k not in self:
            self[k] = []
        self[k].append(v)


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
def readin(_file, func):
    with open(_file) as fin:
        for line in fin:
            line = line.strip()
            func(line)


# 批量处理数据 data: iteraotr or stdin
def batch(data_set, deal_func, bulk_func, size=500):
    cnt = 0 
    temp_data_list = []
    for _data in data_set:
        temp_data_list.append(deal_func(_data))
        cnt += 1
    
        if len(temp_data_list) == size:
            bulk_func(temp_data_list)
            temp_data_list = []

    if len(temp_data_list) > 0:
        bulk_func(temp_data_list)


# 处理json.dumps()中datetime无法直接转换的问题
def date_timeconverter(o):
    if isinstance(o, datetime.datetime):
            return o.__str__()

# 时间转换
def get_current_datetime(formatter='%Y-%m-%d %H:%M:%S'):
    return timestamp_to_formatter_string(time.time(), formatter)

def timestamp_to_formatter_string(timestamp, formatter='%Y-%m-%d %H:%M:%S'):
    return time.strftime(formatter, time.localtime(timestamp))

def formatter_string_to_timestamp(formatter_string, formatter='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(formatter_string, formatter))

# asc字符和编码转换
def int_to_asc(_int):
    return chr(_int)

def int_list_to_str(_ints):
    return ''.join([chr(i) for i in _ints])

def asc_to_int(_char):
    return ord(_char)

def asc_list_to_int_list(_str):
    return [ord(i) for i in _str]

# binany    0b11    bin(3)
# hex       0x11


# 正则
def regex_rule():
    regex_dic = { 
                'ip' : re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])(:\d{4})?'),
                'url' : re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
                }  
    return regex_dic


# *****************************GZ*********************************
def gzip_compress(c_data):
    buf = StringIO()
    try:
        with gzip.GzipFile(mode='wb', fileobj=buf) as f:
            f.write(c_data)
        return  buf.getvalue()
    except Exception as e:
        print ("compress wrong"+e)
    finally:
        f.close()

def gzip_uncompress(c_data):
    try:
        buf = StringIO(c_data)
        with gzip.GzipFile(mode='rb', fileobj=buf) as f:
            return f.read()
    except Exception as  e:
        print("uncompress wrong"+e)
    finally:
        f.close()


def main():
    # test trans
    print int_to_asc(70)
    print int_list_to_str([70, 80, 90])

    print asc_to_int('E')
    print asc_list_to_int_list('BDC')


if __name__ == "__main__":
    main()
