#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def main():
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()

    exchange='direct_logs'
    channel.exchange_declare(exchange=exchange, type='direct')
    queue_name = channel.queue_declare(exclusive=True).method.queue

    binding_keys = sys.argv[1:] if len(sys.argv) > 1 else ['info', 'error']

    for binding_key in binding_keys:
        channel.queue_bind(exchange=exchange, queue=queue_name,routing_key=binding_key)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received %r:%r" % (method.routing_key, body))
        #print(ch, method, properties, body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(callback, queue=queue_name)

    channel.start_consuming() 

if __name__ == "__main__":
    main()

