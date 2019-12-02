#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2018-08-13 19:31:27
Last modify: 2018-12-09 02:42:10
"""

import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getcwd())

import pika


class RMQ_CLIENT():
    def __init__(self, config): 
        host = config.get('host', '127.0.0.1')
        port = config.get('port', '5672') 
        user = config.get('username', '') 
        passwd = config.get('password', '')
        vhost = config.get('vhost', '/')

        exchange_name = config.get('exchange_name', 'fsrm_default_exchange')
        exchange_type = config.get('exchange_type', 'direct')
        queue_name = config.get('queue_name', 'fsrm_default_queue')
        routing_key = config.get('routing_key', '#')

        try:
            port = int(port)
        except:
            port = 5672

        self.init_conn(host, port, user, passwd, vhost)
        self.init_channel(exchange_name, exchange_type, queue_name, routing_key)


    def init_conn(self, host, port, user, passwd, vhost):
        credentials = pika.PlainCredentials(user, passwd)
        parameters = pika.ConnectionParameters(host, port, vhost, credentials, heartbeat_interval=0)
        self.rmq_conn = pika.BlockingConnection(parameters)
        #self.rmq_conn.socket.settimeout(86400*7)
        

    def init_channel(self, exchange_name, exchange_type, queue_name, routing_key):
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.queue_name = queue_name
        self.routing_key = routing_key

        self.channel = self.rmq_conn.channel()
        self.channel.queue_declare(queue=queue_name, durable=True, auto_delete=False) #持久化队列

        # 如果不绑定routing-key和queue 则自动在默认的exchange上绑定与routing-key同名的queue。若不存在routing_key同名的queue 则信息丢失
        if exchange_name and exchange_type:
            self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)
            self.channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)


class RMQ_PRODUCER(RMQ_CLIENT):
    def publish(self, message, headers={}):
        self.channel.basic_publish(exchange=self.exchange_name, 
                                    routing_key=self.routing_key, 
                                    body=message, 
                                    properties=pika.BasicProperties(delivery_mode=2, headers=headers) #持久化消息
                                    )


class RMQ_CONSUMER(RMQ_CLIENT):
    def consume(self, callback_func=default_callback):

        def callback(ch, method, properties, body):
            callback_func(body)
            self.channel.basic_ack(delivery_tag=method.delivery_tag)
            
        self.channel.basic_qos(prefetch_count=1) #轮询分发(每个consumer积压的数据不多于n条)
        self.channel.basic_consume(callback, queue=self.queue_name, no_ack=False) #确认消费正常完成，否则转发给其他消费者
        self.channel.start_consuming()

    def default_callback(msg):
        print msg


def main():
    from config import *
    rmq_config = rmq_config_local
    rmq_producer = RMQ_PRODUCER(rmq_config)
    rmq_producer.publish('hahaha\t gogogo')

    #rmq_producer.channel.queue_delete(queue='fsrm_test')
    #sys.exit(0)

    rmq_consumer = RMQ_CONSUMER(rmq_config)
    rmq_consumer.consume()


if __name__ == "__main__":
    main()
