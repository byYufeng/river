#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import pika

    host = 'localhost'
    #connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    exchange_name = 'test_topic'
    channel.exchange_declare(exchange=exchange_name, durable=True, type='topic')

    routing_key = sys.argv[1] if len(sys.argv) > 1 else '#'
    message = ' '.join(sys.argv[2:]) or 'hello!'
    channel.basic_publish(exchange=exchange_name,
                          routing_key=routing_key,
                          body=message,
                          #properties=pika.BasicProperties(
                          #    delivery_mode = 2
                          #    )
                          )
    print(" [x] %s:%s Sent %r" % (exchange_name, routing_key, message))
    connection.close()


if __name__ == "__main__":
    main()

