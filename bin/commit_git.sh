#find. -type d -empty -exec touch {}/.gitignore \; #make sure to commit empty folder

if [ -n "$1" ]; then
    message=$1
else
    message='auto commit...'
fi

git add *
git add -A
git status
git commit -m "$message"
git push origin master
