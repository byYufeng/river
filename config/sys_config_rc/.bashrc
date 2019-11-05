# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
#stty -ixon

# ***************************************sys************************************
alias yum='sudo yum'
alias ll='ls -lh --color=auto'
alias la='ls -A --color=auto'
alias lla='ls -lhA --color=auto'
alias mv='mv -i'
alias cp='cp -r -i'
alias rm='trash'
alias free='free -h'
alias dud='du -h --max-depth=1'
alias dus='du -sh'
alias vim_none='vim -u NONE'
curll(){
    curl localhost:$1
}

# ***************************************hadoop************************************
# hadoop alias
alias hdfs='hadoop fs'
alias hls='hadoop fs -ls'
alias hget='hadoop fs -get'
alias hput='hadoop fs -put'
alias hcat='hadoop fs -cat'
alias htext='hadoop fs -text'
alias hdu='hadoop fs -du -h'
alias hdus='hadoop fs -du -h -s'
alias hrm='hadoop fs -rm -r -f'
alias hmk='hadoop fs -mkdir -p'
alias hhome='hadoop fs -ls ~'
hhead(){
    hadoop fs -text $1 | head
}
htree(){
    hadoop fs -ls -R $1 | awk '{print $8}' | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/ /' -e 's/-/|/' 
}

alias yls='yarn application -list'
alias ylsm="yarn application -list | grep `whoami`"
alias ylogs="yarn logs -applicationId"
alias ykill='yarn application -kill'

alias pyspark='~/libs/spark/bin/pyspark'



# ***************************************git************************************
alias gstatus="git status"
alias gdiff="git difftool"


# User specific aliases and functions
#alias googler='proxychains4 googler'

#alias im="python ~/scripts/mojo_im.py "
#alias qq="python ~/scripts/mojo_im.py qq"
#alias wx="python ~/scripts/mojo_im.py wx"
#alias ttt="python ~/scripts/mojo_im.py qq printt | tail -7 | head -5"
#alias tt="python ~/scripts/mojo_im.py qq send uid "

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

#hide file
hide(){
    mv $1 .$1
}

#docker
dtags(){
    for Repo in $* ; do
        curl -s -S "https://registry.hub.docker.com/v2/repositories/library/$Repo/tags/" | \ 
        sed -e 's/,/,\n/g' -e 's/\[/\[\n/g' | \ 
        grep '"name"' | \ 
        awk -F\" '{print $4;}' | \ 
        sort -fu | \ 
        sed -e "s/^/${Repo}:/"
    done
}

# exec-attach $container_name
da(){
    docker exec -it $1 sh -c "cd && bash" || docker exec -it $1 sh -c "cd && sh"
}

# run $image_name $container_name #other_args
dr(){
    args=($@)
    docker run -itd --name $2 --restart always ${args[@]:2} $1 sh
}

# 
dps(){
    docker ps
}

# 
drm(){
    docker rm -f $1
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
    #eval `ssh-agent`
    ssh-add ~/.ssh/id_rsa.r81.key
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
#tmux_auto_attach
#source .bash_completion_tmux.sh

dnf(){
    da dnf_server
}

# ssh时自动补全.ssh/config中的Host
#complete -W "$(echo $(grep '^Host ' .ssh/config  | sort -u | sed 's/^ssh //'))" ssh 
