#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../..')

import os
from utils.net import Net
from utils import Utils
import json

class Lanxin(object):

    def __init__(self, mobile='', passwd=''):
        #self.ip = 'http://open.lx.b.360.cn'
        #self.port = 80
        self.domain = 'open.lx.b.360.cn'
        self.appid = 100248

        self.mobile, self.passwd = mobile, passwd
        self.token = None
        self.check_token()
    
        self.logger = Utils().getLogger()

    def login_get_code(self, mobile, passwd):
        api = 'http://open.lx.b.360.cn/lop/oauth2/login'
        postdata = '''
            appid=100248,
            redirect_uri=baidu.com,
            response_type=code,
            scope=snsapi_userinfo,
            state=1,
            debug_oauth=true,
            global_account=false,
            source=fromloin,
            mobile={mobile},
            p={passwd},
            api_choose=1,
            api_choose=2,
            api_choose=3,
            '''.format(mobile=mobile, passwd=passwd)
        data = {}
        for s in postdata.split(','):
            ss = s.strip().split('=')
            if len(ss) > 1:
                data[ss[0]] = ss[1]

        res = Net.post(api, data)
        self.headers = res.headers
        content = json.loads(res.content)
        if not content['errcode']:
            return content['code']
        else:
            self.logger.error(content['errmsg'])
            return content['errmsg'] 
        
    def get_token(self, code):
        api = 'http://{DOMAIN}/sns/oauth2/access_token?code={CODE}&appid={APPID}&grant_type=authorization_code'
        api = api.format(DOMAIN=self.domain, CODE=code, APPID=self.appid)
        res = Net.get(api)
        content = json.loads(res.content)
        if not content['errcode']:
            return content['access_token']
        else:
            self.logger.error(content['errmsg'])
            return content['errmsg'] 

    def check_token(self):
        api = 'http://{DOMAIN}/sns/userinfo?access_token={ACCESS_TOKEN}&mobile={MOBILE}'
        api = api.format(DOMAIN=self.domain, ACCESS_TOKEN=self.token, MOBILE=self.mobile)
        res = Net.get(api)
        content = json.loads(res.content)
        #token过期
        if content['errcode']:
            if content['errcode']== 30004:
                self.token = self.get_token(self.login_get_code(self.mobile, self.passwd))
                print 'new token: %s' %self.token
            else:
                self.logger.error(content['errmsg'])

    def get_group_id(self, group_name):
        api = 'http://{DOMAIN}/lop/qun/message/dialog/get' 
        api = api.format(DOMAIN=self.domain)
        params = {'access_token':self.token, 'currentPage':1}
        res = Net.get(api, params=params)
        content = json.loads(res.content)
        if not content['errcode']:
            data = content['data']
            if int(content.get('totalCount')) > 20:
                raise Exception
            for data_ in data:
                if data_.get('name') == group_name:
                    return data_.get('id')
        

    def send_messages(self, text='', group_name='', person=[]):
        self.check_token()
        api = 'http://{DOMAIN}/lop/mass/message/send?rand=97&access_token={ACCESS_TOKEN}'
        api = api.format(DOMAIN=self.domain, ACCESS_TOKEN=self.token)
        group_id = self.get_group_id(group_name)
        data = {
            "toall": "false",
            "tousers": [],
            "togroups": [],
            "toqun" : group_id,
            "msgtype": "text",
            "text": {
                "content": text
            }
        }

        data = json.dumps(data)
        data = data.replace(r'\\n', r'\n')#替换掉转义后的\n
        #from urllib import urlencode, quote
        #data = str(data)
        #data = urlencode(data)
        #data = quote(data)
        res = Net.post(api, data=data)
        content = json.loads(res.content)
        if content['errcode']:
            self.logger.error('errorcode:%s errmsg:%s' % (content['errcode'], content['errmsg']))
        else:
            self.logger.info('%s %s' %(api, data))


def main():
    params = sys.argv[1:]
    mobile, passwd, group, text = params
    #group = '天眼实验室'
    #group = 'test_lanxin'
    #发送的文本无字数限制 可通过\n进行换行,无表格、html等展现形式。若有需求可考虑通过图文、附件等形式
    #存在一个bug： +字符会丢失
    lanxin = Lanxin(mobile, passwd)
    lanxin.send_messages(text, group)

if __name__ == "__main__":
    main()
