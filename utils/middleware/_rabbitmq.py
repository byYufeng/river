#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-13 19:31:27
Last modify: 2018-08-31 19:45:11
"""

import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getcwd())

import pika

class RMQ_CLIENT():
    def __init__(self, config): 
        host = config.get('host', '')
        port = config.get('port', '') 
        user = config.get('user', '') 
        passwd = config.get('passwd', '')
        p1 = config.get('', '/')

        exchange_name = config.get('exchange_name', '')
        exchange_type = config.get('exchange_type', '')
        queue_name = config.get('queue_name', '')
        routing_key = config.get('routing_key', '')

        try:
            port = int(port)
        except:
            port = 5672

        self.init_conn(host, port, user, passwd, p1)
        self.init_channel(exchange_name, exchange_type, queue_name, routing_key)


    def init_conn(self, host, port, user, passwd, p1):
        credentials = pika.PlainCredentials(user, passwd)
        parameters = pika.ConnectionParameters(host, port, p1, credentials)
        self.rmq_conn = pika.BlockingConnection(parameters)
        

    def init_channel(self, exchange_name, exchange_type, queue_name, routing_key):
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.queue_name = queue_name
        self.routing_key = routing_key

        self.channel = self.rmq_conn.channel()
        #channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)
        self.channel.queue_declare(queue=queue_name, durable=True, auto_delete=False) #持久化队列
        #channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)


class RMQ_PRODUCER(RMQ_CLIENT):
    def publish(self, message):
        self.channel.basic_publish(exchange=self.exchange_name, 
                                    routing_key=self.routing_key, 
                                    body=message, 
                                    properties=pika.BasicProperties(delivery_mode=2) #持久化消息
                                    )


class RMQ_CONSUMER(RMQ_CLIENT):
    def consume(self, callback_func):

        def callback(ch, method, properties, body):
            callback_func(body)
            self.channel.basic_ack(delivery_tag=method.delivery_tag)
            
        self.channel.basic_qos(prefetch_count=1) #轮询分发(每个consumer积压的数据不多于n条)
        self.channel.basic_consume(callback, queue=self.queue_name, no_ack=False) #确认消费正常完成，否则转发给其他消费者
        self.channel.start_consuming()


if __name__ == "__main__":

    from config import *

    rmq_config = rmq_config_filees06
    rmq_config = rmq_config_k6204v

    rmq_producer = RMQ_PRODUCER(rmq_config)
    #rmq_producer.publish('hahaha\t gogogo')

    #rmq_producer.channel.queue_delete(queue='fsrm_test')
    #sys.exit(0)

    rmq_consumer = RMQ_CONSUMER(rmq_config)
    def callback(msg):
        print msg
    rmq_consumer.consume(callback)
