#!/usr/bin/env python
#coding:utf-8
#Created by baiyufeng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

def main():
    import pika
    import uuid, time 

    class RPC(object):
        def __init__(self):
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
            self.channel = self.connection.channel()

            self.queue_name_request = 'rpc_request'
            self.queue_name_response = 'rpc_response'
            
            #channel.queue_declare(queue=queue_name_request,exclusive=True)
            self.channel.queue_declare(queue=self.queue_name_response,exclusive=True)

            self.channel.basic_consume(self.callback_on_response, queue=self.queue_name_response)


        def callback_on_response(self, ch, method, props, body):
            if props.correlation_id == self.corr_id:
                self.response = body

        def call(self, data):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(exchange='',
                                  routing_key=self.queue_name_request,
                                  properties=pika.BasicProperties(
                                      reply_to = self.queue_name_response,
                                      correlation_id = self.corr_id
                                    ),
                                  body=str(data)
                                  )
            while self.response is None:
                self.connection.process_data_events()
            self.connection.close()
            return int(self.response)


    rpc = RPC()
    n = sys.argv[1]
    time.sleep(int(n)) 
    print('rpc_call send:%r' % n)
    response = rpc.call(n)
    print('rpc_call result:%r' % response)


if __name__ == "__main__":
    main()

