#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def search(im, params):
    params = ''.join(params)
    if im == 'qq':
        #通过qq号或者备注查
        try:
            params = int(params)
            params_ = 'uid=%s' % params
        except:
            params_ = 'markname=%s' % params
        api = 'http://127.0.0.1:5000/openqq/search_friend?%s' % (params_)
    elif im == 'wx':
        if params.isalnum():
            params_ = 'account=%s' % params
        else:
            params_ = 'markname=%s' % params
        api = 'http://127.0.0.1:3000/openwx/search_friend?%s' % (params_)
    return "curl '%s'" % api

def send(im, params):
    if im == 'qq':
        #qq 只能通过qq帐号
        api = 'http://127.0.0.1:5000/openqq/send_friend_message?%s=%s&content=%s' % ('uid', params[0], params[1])
    elif im == 'wx':
        api = 'http://127.0.0.1:3000/openwx/send_friend_message?%s=%s&content=%s' % (params[0], params[1], params[2])
        #account帐号 markname备注
    return "curl '%s'" % api

def print_messages(im, keep=True):
    cmd = 'sudo docker logs %s' % (im)
    return cmd

def clear(im):
    if im == 'qq':
        cmd = 'sudo docker rm -f qq && sudo rm -f /tmp/mojo_webqq_*'
    elif im == 'wx':
        cmd = 'sudo rm -f /tmp/mojo_*'
    return cmd
    

def start(im):
    if im == 'qq':
        cmd = 'sudo docker run --name qq -d --env MOJO_WEBQQ_LOG_ENCODING=utf8 --env MOJO_WEBQQ_IS_INIT_GROUP=0 --env MOJO_WEBQQ_IS_UPDATE_GROUP=0 --env MOJO_WEBQQ_MSG_TTL=99999 -p 5000:5000 -v /tmp:/tmp sjdy521/mojo-webqq'
        #cmd = 'sudo docker run --name qq -it --env MOJO_WEBQQ_LOG_ENCODING=utf8 -p 5000:5000 -v /tmp:/tmp sjdy521/mojo-webqq'
    elif im == 'wx':
        cmd = 'sudo docker run --name wx -d --env MOJO_WEIXIN_LOG_ENCODING=utf8 -p 3000:3000 -v /tmp:/tmp sjdy521/mojo-weixin'
        #cmd = 'sudo docker run --name wx -it --env MOJO_WEIXIN_LOG_ENCODING=utf8 -p 3000:3000 -v /tmp:/tmp sjdy521/mojo-weixin'
    return cmd

'curl http://127.0.0.1:5000/openqq/get_user_info | jq . '

def main():
    #start: qq/wx start 
    #search: qq/wx id/markname/... objtext
    #send: qq/wx id/markname/... objtext content
    ##search-simple: qq/wx id/markname/... objtext
    args = sys.argv 
    im, op, params = args[1], args[2], args[3:]
    print '%s %s %s' % (im, op, params)
    
    if op == 'start':
        cmd = start(im)
    elif op == 'clear':
        cmd = clear(im)
    elif op == 'search':
        cmd = search(im, params)
    elif op == 'send':
        cmd = send(im, params)
    elif op == 'print':
        if not params:
            cmd = print_messages(im)
        else:
            while 1:
                os.system(print_messages(im))
                time.sleep(3)
    else:
        cmd = ''
    print 'cmd:%s' % cmd
    os.system(cmd)

if __name__ == "__main__":
    main()
