input=$1
mapper=$2
reducer=$3
cat $input | python $mapper | sort | python $reducer
