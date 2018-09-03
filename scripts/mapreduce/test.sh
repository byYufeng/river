input=$1
mapper=$2
reducer=$3
#head -n100 multi_engine.xml | python map.py | sort | python reduce.py 
#head multi_engine2.xml | python map.py | sort | python reduce.py 
cat $input | python $mapper | sort | python $reducer
