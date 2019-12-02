malfile_scan_agg(){
curl http://127.0.0.1:9200/*/_search?\
q=source:$1\
 -d '{"size":0,"aggs":{"scan_date":{"date_histogram":{"field":"scan_time","interval":"day"}}}}'\
 | python -m json.tool\
 > es_agg.$1_res
}

malfile_scan_agg test_index
