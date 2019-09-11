input=$1
mapper=map.py
reducer=reduce.py
cat $input | python $mapper | sort | python $reducer
