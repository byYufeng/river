#! /usr/bin/env python
# coding:utf-8
"""
Author: fsrm
Create Time: 2019-06-13 18:06:57
Last modify: 2019-06-13 18:06:57
"""

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(".")

import json, time, traceback
from datetime import datetime
from elasticsearch import Elasticsearch, helpers


class ES(object):
    def __init__(self, config):
        hosts = config.get('hosts', '127.0.0.1:9200')
        self.es_client = Elasticsearch(hosts=hosts, timeout=60)
        #indexes = 'fsrm_test_index'


    def create_index(self, index, index_settings):
        return self.es_client.indices.create(index=index, body=index_settings)


    def delete_index(self, indexes):
        return self.es_client.indices.delete(index=indexes, ignore=404)


    def search(self, index, body)
        return self.es_client.search(index=index, body=body)


    def bulk(bulk_docs):
        bulk_actions = [{
                    "_op_type": op_type,
                    "_index": doc_index,
                    "_type": doc_type,
                    "_id": doc_id,
                    "_source": json.loads(doc) # update文档时此字段为doc
                    }
                for op_type, doc_index, doc_type, doc_id, doc in bulk_docs]
        res = helpers.bulk(self.es_client, bulk_actions)
        return res


def main():
    index_default_settings = {
            "settings": {
                "analysis": {
                    "analyzer":{
                        "fsrm_custom_analyzer":{
                            "type": "custom",
                            "tokenizer": "letter",
                            "char_filter": ["html_strip"],
                            "filter": ["lowercase"],
                        }
                    }
                }
            },
            "mappings": {
                "NETWORK": {
                    "_all":{
                        "analyzer": "fsrm_custom_analyzer",
                    },
                    "properties": {
                        "md5": {"type": "keyword"},
                        "name": {
                            "type": "text",
                            "keyword": {
                                "type": "keyword"
                                "ignore_above": 256,
                            }
                        },
                        "timestamp": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                        "count": {"type": "long"},
                    }
                },
            }
    }

    default_body = {"query": {"match_all": {}}}
    template_body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "@timestamp": {
                                "gt": "2019-01-01 00:00:00",
                                "lt": "2019-06-07 00:00:00"
                            }
                        }
                    }
                ],
                "must_not": [],
                "should": []
            }
        },
        "from": 0,
        "size": 10,
        "sort": [],
        "aggs": {}
    }


if __name__ == "__main__":
    main()
