#!/bin/bash

#find. -type d -empty -exec touch {}/.gitignore \; #make sure to commit empty folder


#sh ~/riven/bin/env_backup.sh

#add comment
if [ -n "$1" ]; then
    message=$1
else
    message='auto commit...'
fi

cd ~/riven
git add * -A
git status
git commit -m "$message"
git push origin master
