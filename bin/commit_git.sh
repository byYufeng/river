#!/bin/bash

#find. -type d -empty -exec touch {}/.gitignore \; #make sure to commit empty folder

#save bashrc&bash_profile&vimrc
cp ~/.bashrc ~/.bash_profile ~/.vimrc \
    ~/riven/.env

#add comment
if [ -n "$1" ]; then
    message=$1
else
    message='auto commit...'
fi

cd ~/riven
git add *
git add -A
git status
git commit -m "$message"
git push origin master
