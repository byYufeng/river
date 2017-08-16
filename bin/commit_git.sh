#find. -type d -empty -exec touch {}/.gitignore \; #make sure to commit empty folder

#cp .bashrc
cp ~/.bashrc ~/riven/bin/.bashrc
cp ~/.vimrc ~/riven/bin/.vimrc

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
