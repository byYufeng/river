# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
alias rm='trash'
trash()
{
    # I quote this path last time and suffers a lot...
    #if [ ! -d ~/.trash ]; then
    #    mkdir ~/.trash
    #fi
    mkdir -p ~/.trash/`date +%Y%m%dT%H%M%S`
    mv $@ ~/.trash/`date +%Y%m%dT%H%M%S`
}
alias riven_commit='cd ~/riven && bin/commit_git.sh'

#disable generate .pyc
export PYTHONDONTWRITEBYTECODE=x

#download and upload files like scp
#The folder name always strange when use dl
dl(){
        cmd="ssh $1 tar cz $2 | tar xzv"
        echo $cmd
        $cmd
}

ul(){
        cmd="tar cz $2 | ssh $1 tar xzv"
        echo $cmd
        $cmd
}

#eval `ssh-agent`
#ssh-add ~/code/documents/key/id_rsa.r81.hdp

