#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os, time

def main():
    import pika

    host = 'localhost'
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()

    exchange_name = 'test_topic'
    queue_name = 'test_topic_queue'
    routing_key = 'info.#'

    channel.exchange_declare(exchange=exchange_name, durable=True, type='topic')
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %s:%s:%s Received %r %r %r %r" % (exchange_name, queue_name, routing_key, ch, method, properties, body))
        print(' [x] Done')
        #ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True
                          )
    channel.start_consuming() 

if __name__ == "__main__":
    main()

