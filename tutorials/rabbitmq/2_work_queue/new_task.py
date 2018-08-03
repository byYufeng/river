#!/usr/bin/env python
#coding:utf-8
#Created by fsrm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)


    message= ' '.join(sys.argv[1:]) or 'hello!'
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode = 2
                              ))
    print(" [x] Sent %r" % message)
    connection.close()


if __name__ == "__main__":
    main()

