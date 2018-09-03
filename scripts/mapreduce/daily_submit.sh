date=`/bin/date +%Y%m%d -d "-1 days"`
local_path=${HOME}/fsrm/hdp_test

source /usr/bin/hadoop/software/hadoop.bashrc
cd $local_path
mkdir -p logs
sh submit.sh $date 1>logs/$date.out 2>logs/$date.err &
