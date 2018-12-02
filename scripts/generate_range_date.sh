date_format='%Y-%m-%d'
date1=`date -d "-0 day $1" +$date_format`
date2=`date -d "+0 day $2" +$date_format`
#echo "------------------------------"
#echo "date=$date"
#echo "enddate=$enddate"
#echo "------------------------------"
while [[ $date1 > $date2  ]]
do
    echo "sh spark_submit.sh $date1"
    date1=`date -d "-1 day $date1" +$date_format`
done
