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

    exchange='direct_logs'
    channel.exchange_declare(exchange=exchange, type='direct')

    routing_key = sys.argv[1] if len(sys.argv) > 2 else 'info'
    message = ' '.join(sys.argv[2:]) or 'hello!'
    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=message,
          )
    print(" [x] Sent %r:%r" % (routing_key, message))
    connection.close()


if __name__ == "__main__":
    main()

