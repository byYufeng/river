#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

#启动容器
def start(im, params):

    #更新或下载镜像
    def update(im, params):
        if im == 'qq':
            cmd = 'sudo docker pull sjdy521/mojo-webqq'
        elif im == 'wx':
            cmd = 'sudo docker pull sjdy521/mojo-weixin'
        return cmd
    _cmd = update(im, params)
    os.system(_cmd)
    
    #若参数为1则新起容器，否则直接启动旧的
    param = params[0] if params else None
    if param == '1':
        if im == 'qq':
            cmd = 'sudo docker run --name qq -d --env MOJO_WEBQQ_LOG_ENCODING=utf8 --env MOJO_WEBQQ_IS_INIT_GROUP=0 --env MOJO_WEBQQ_IS_UPDATE_GROUP=0 --env MOJO_WEBQQ_MSG_TTL=99999 -p 5000:5000 -v /tmp:/tmp sjdy521/mojo-webqq'
        elif im == 'wx':
            cmd = 'sudo docker run --name wx -d --env MOJO_WEIXIN_LOG_ENCODING=utf8 -p 3000:3000 -v /tmp:/tmp sjdy521/mojo-weixin'
    else:
        if im == 'qq':
            cmd = 'sudo docker start qq'
        elif im == 'wx':
            cmd = 'sudo docker start wx'
    return cmd

#搜索好友
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

#发送信息
def send(im, params):
    if im == 'qq':
        #uid(qq号)
        api = 'http://127.0.0.1:5000/openqq/send_friend_message?%s=%s&content=%s' % (params[0], params[1], params[2])
    elif im == 'wx':
        #account帐号 markname备注
        api = 'http://127.0.0.1:3000/openwx/send_friend_message?%s=%s&content=%s' % (params[0], params[1], params[2])
    return "curl '%s'" % api

#刷新显示
def printt(im, params):

    def _print(im):
        cmd = 'clear | sudo docker logs %s | tail' % (im)
        return cmd

    if params:
        while 1:
            os.system(_print(im))
            time.sleep(3)
        return ''
    else:
        return _print(im)

#清理容器
def clear(im):
    if im == 'qq':
        cmd = 'sudo docker rm -f qq && sudo rm -f /tmp/mojo_webqq_*'
    elif im == 'wx':
        cmd = 'sudo rm -f /tmp/mojo_*'
    return cmd


def test():
    pass

def main():
    args = sys.argv 
    im, op, params = args[1], args[2], args[3:]
    print('IM:%s OP:%s PARAMS:%s' % (im, op, params))
    '''
    start: qq/wx # start 
    search: qq/wx # id/markname xxx ...
    send: qq/wx # uid(qq)/markname(wx)/ xxx content
    search-simple: qq/wx # id/markname/... objtext
    printt: qq/wx # 1/0
    clear: qq/wx # 
    '''
    'curl http://127.0.0.1:5000/openqq/get_user_info | jq . '
    
    #cmd = op(im, params)
    cmd = globals()[op](im, params)
    print('cmd:%s' % cmd)
    os.system(cmd)

if __name__ == "__main__":
    main()
