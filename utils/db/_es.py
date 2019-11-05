#!/usr/bin/env python
#coding:utf-8
"""
Author: fsrm
Create Time: 2019-04-25 18:22:35
Last modify: 2019-04-25 18:22:35
"""

import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.getenv('HOME') + '/riven/libs/python')
sys.path.append(os.getenv('HOME') + '/riven/utils')

import time, traceback, random
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from pprint import pprint
import common
import pytz
try:
    import simplejson as json
except:
    import json


def main():
    #import config
    es_online_config = { 
            'hosts': '127.0.0.1:9200',
            'indices': [
                'fsrm_test_1',
                'fsrm_test_2'
            ],  
            #'http_auth': ('', '')
            'http_auth': (sys.argv[1:3])
    }

    def init():
        indices = es_online_config.get('indices')
        es = ES(es_online_config)
        es.delete_indice(indices[0])
        es.create_indice(indices[0], es.get_default_mapping())
        es.init_indices(indices[1])
        data = {"key": "ttt", "value":10, "insert_time":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}
        data = {"key": "ttt", "value":10, "insert_time":time.strftime('%Y-%m-%dT%H:%M:%S+0800', time.localtime(time.time()))}
        #data = {"key": "ttt", "value":10, "insert_time": "2019-11-05 10:%0.2s:%0.2s" % (int(random.random()*60), int(random.random()*60),)}
        data_for_bulk = [["index", indices[1], "100000001", data]]
        es.insert(indices[0], data)
        es.bulk(data_for_bulk)

        return es

    init()
    time.sleep(1)
    es = ES(es_online_config)
    print es.search("fsrm*", {"query": {"match_all": {}}})
    print es.search("fsrm*", {"query": {"match_all": {}}}, filter_path=['hits.hits._index', 'hits.hits._id', 'hits.hits._source'])

    query_body_default = {"query": {"match_all": {}}}
    query_body_template = {
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


class ES(object):
    def __init__(self, config):
        hosts = config.get('hosts', '127.0.0.1:9200')
        timeout = config.get('timeout', 300)
        if config.get('http_auth'):
            http_auth = config.get('http_auth')
            self.es_client = Elasticsearch(hosts=hosts, http_auth=http_auth, timeout=timeout)
        else:
            self.es_client = Elasticsearch(hosts=hosts, timeout=timeout)


    # indices & mapping
    def create_indice(self, indice, indice_mapping):
        return self.es_client.indices.create(index=indice, body=indice_mapping)

    def delete_indice(self, indices):
        return self.es_client.indices.delete(index=indices, ignore=404)

    def get_default_mapping(self):
        # ES7.x起 mapping不再支持_type类型和_all参数
        indice_mapping_template = {
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
                    #"analyzer": "fsrm_custom_analyzer",
                    "properties": {
                        "key": {"type": "keyword"},
                        "value": {"type": "long"},
                        "note": {"type": "text"},
                        "insert_time": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                        "insert_time": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ssZ"},
                }
            }
        }
        return indice_mapping_template

    def init_indices(self, indice, mappings={}, delete=True):
        if delete:
            self.delete_indice(indice)

        if not mappings:
            mappings = self.get_default_mapping()
        res = self.es_client.indices.create(index=indice, body=mappings)
        return res


    # data CRUD
    def insert(self, index, body):
        return self.es_client.index(index=index, body=body)

    def search(self, index, body, **kwargs):
        return self.es_client.search(index=index, body=body, **kwargs)


    def bulk(self, bulk_docs):
        bulk_actions = [
                {
                    "_op_type": op_type,
                    "_index": indice,
                    "_id": doc_id,
                    "_source": doc # update文档时此字段为doc
                } for op_type, indice, doc_id, doc in bulk_docs]
        res = helpers.bulk(self.es_client, bulk_actions)
        return res

    # for ES under 7.x: remove _type from ES 7.X
    def bulk2(self, bulk_docs):
        bulk_actions = [
                {
                    "_op_type": op_type,
                    "_index": doc_index,
                    "_type": doc_type,
                    "_id": doc_id,
                    "_source": doc # update文档时此字段为doc
                } for op_type, doc_index, doc_type, doc_id, doc in bulk_docs ]
        res = helpers.bulk(self.es_client, bulk_actions)
        return res


    # 自适应update的格式，update时指定upsert
    def deal_and_bulk2(self, bulk_docs, upsert=True):
        bulk_actions = []
        for _doc in bulk_docs:
            try:
                op_type, doc_index, doc_type, doc_id, doc = _doc
            except:
                sys.stderr.write(str(_doc))
                sys.exit(0)

            bulk_doc = {
                    "_op_type": op_type,
                    "_index": doc_index,
                    "_type": doc_type,
                    "_id": doc_id,
                    }
            if op_type == 'index':
                bulk_doc['_source'] = json.loads(doc)
            if op_type == 'update':
                bulk_doc['doc'] = json.loads(doc)
                if upsert:
                    bulk_doc['doc_as_upsert'] = True
            bulk_actions.append(bulk_doc)

        res = helpers.bulk(es, bulk_actions)
        return res


if __name__ == "__main__":
    main()
