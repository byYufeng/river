#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def main():
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', type='fanout')
    queue_name = channel.queue_declare(exclusive=True).method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(callback, queue=queue_name)

    channel.start_consuming() 

if __name__ == "__main__":
    main()

