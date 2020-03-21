#!/bin/bash
#Author: fsrm

# create topic
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# send msg
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

# receive msg
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
