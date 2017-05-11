#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import pika
    import uuid

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
    channel = connection.channel()

    queue_name_request = 'rpc_request'
    channel.queue_declare(queue=queue_name_request, exclusive=True)


    def fib(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return fib(n-1) + fib(n-2)
    
    def callback_on_request(ch, method, properties, body):
        n = int(body)
        response = fib(n)
        channel.basic_publish(exchange='',
                              routing_key=properties.reply_to,
                              properties=pika.BasicProperties(
                                  correlation_id = properties.correlation_id
                                ),
                              body=str(response)
        )

    channel.basic_consume(callback_on_request,queue=queue_name_request)
    channel.start_consuming()


if __name__ == "__main__":
    main()

