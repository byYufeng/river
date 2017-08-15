#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import pika

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', type='fanout')

    message= ' '.join(sys.argv[1:]) or 'hello!'
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message,
          )
    print(" [x] Sent %r" % message)
    connection.close()


if __name__ == "__main__":
    main()

