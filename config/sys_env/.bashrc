# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# sys alias
alias ll='ls -lh --color=auto'
alias lla='ls -lha --color=auto'
alias mv='mv -i'
alias rm='trash'
alias free='free -h'
alias vim_none='vim -u NONE'

# hadoop alias
alias hdfs='hadoop fs'
alias hls='hadoop fs -ls'
alias hcat='hadoop fs -cat'
alias htext='hadoop fs -text'
alias hdu='hadoop fs -du -h'
alias hrm='hadoop fs -rm -r -f'

alias yls='yarn application -list'
alias ykill='yarn application -kill'

alias hhome='hadoop fs -ls ~'
alias pyspark='~/libs/spark-2.2.0-bin-hadoop2.6/bin/pyspark'

# User specific aliases and functions
alias googler='proxychains4 googler'

alias im="python ~/scripts/mojo_im.py "
alias qq="python ~/scripts/mojo_im.py qq"
alias wx="python ~/scripts/mojo_im.py wx"
alias ttt="python ~/scripts/mojo_im.py qq printt | tail -7 | head -5"
alias tt="python ~/scripts/mojo_im.py qq send uid "

#replace rm of mv
trash()
{
    # I quote this path last time and suffers a lot...
    #if [ ! -d ~/.trash ]; then
    #    mkdir ~/.trash
    #fi 
    timestamp=`date +%Y%m%d_%H%M`
    mkdir -p ~/.trash/$timestamp
    mv $@ ~/.trash/$timestamp/
}

#alias nohup='nohupp'
nohupp(){
    pwd
    /usr/bin/nohup ./$1 1>$1.out 2>$1.err &
}

# alias riven_commit='cd ~/riven && bin/commit_git.sh $1 && cd -'
riven_commit(){
    cd ~/riven && ./bin/commit_git.sh $1
    cd -
}

#disable generate .pyc
export PYTHONDONTWRITEBYTECODE=x

#download and upload files like scp
#but...The folder name always strange when use dl
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

#avoid to enter ssh phrase each time
ssh-agent_login(){
        eval `ssh-agent`
        ssh-add ~/code/documents/key/id_rsa.r81.hdp
}

tmux_init()
{
    tmux new-session -d                  # 开启一个会话(后台)
    tmux new-window                      # 开启一个窗口(新窗口)
    #tmux split-window -h                # 开启一个竖屏
    #tmux split-window -v "top"          # 开启一个横屏,并执行top命令
    #tmux -2 attach-session -d           # tmux -2强制启用256color，连接已开启的tmux
    tmux attach-session
}

# 判断是否已有开启的tmux会话，没有则开启
tmux_auto_attach(){
if which tmux 2>&1 >/dev/null; then
    test -z "$TMUX" && (tmux attach || tmux_init)
fi
}
