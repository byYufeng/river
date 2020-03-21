# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
#stty -ixon

# ***************************************sys************************************
HISTSIZE=10000
HISTFILESIZE=10000
alias python='python3'
alias py='python3'
alias py2='python2'
alias py3='python3'

alias l='ls -l'
alias ll='ls -lh --color=auto'
alias la='ls -A --color=auto'
alias lla='ls -lhA --color=auto'
alias mv='mv -i'
alias cp='cp -r -i'
alias rm='trash'
alias brm='/bin/rm -rf'
alias free='free -h'
alias dud='du -h --max-depth=1'
alias dus='du -sh'
alias psg="ps axu | grep" #ps
alias hg="history | grep" #history
alias yum='sudo yum'
alias svim='sudo vim'


alias vim_none='vim -u NONE'
alias mtop="ps auxw | head -1; ps auxw | sort -rn -k4 | head -3"
alias tcpdump="sudo tcpdump"

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

awkp(){ # awk -F"$1" '{print $2,$3...}', 不适于用分隔符为空格
    args=($@);awk -F"$1" "BEGIN{OFS=\"\t\"};{print ${args[@]:1}}"
}

suma(){ #单列数字 按列求和
    awk '{a[0]+=$1;} END{print a[0]}'
}

wca(){ # word count: 适用单列key和key+分隔符+value
    if [ $# == 0 ]
    then # echo -e 'a\nb\na' |wca
        awk '{a[$1]+=1;} END{for(i in a) print i,a[i]}'
    else # echo -e 'a 1\nb 2\na 3' | wca ' '
        awk -F"$1" '{a[$1]+=$2;} END{for(i in a) print i,a[i]}'
    fi
}

curll(){ # curl localhost
    #if [ $# == 0 ]; then port=80; else port=$1; fi;curl 127.0.0.1:$port
    curl 127.0.0.1:${1:-80}
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
alias hmv='hadoop fs -mv'
alias hmk='hadoop fs -mkdir -p'
alias hrm='hadoop fs -rm -r -f'
alias hhome='hadoop fs -ls ~'

hgett(){ #hget & rename /a/b -> hdfs_a_b
    hadoop dfs -get $1 hdfs`echo $1 | sed 's#/#_#g'`
}
hhead(){
    hadoop fs -text $1 | head
}
htree(){
    hadoop fs -ls -R $1 | awk '{print $8}' | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/ /' -e 's/-/|/' 
}
harchive(){ # $1:path $2:dir_name
    hadoop archive -archiveName $2.har -p $1 $2 $1
}

alias yls='yarn application -list'
alias ylsm="yarn application -list | grep `whoami`"
alias ylogs="yarn logs -applicationId"
alias ykill='yarn application -kill'
alias yui="w3m http://127.0.0.1:8088" # 访问UI界面
alias pyspark='/usr/lib/spark/bin/pyspark'


# ***************************************git************************************
alias gstatus="git status"
alias gdiff="git difftool -y"
alias gadd="git add * -A"
alias gcommit="git commit -am" #comment
alias gpush="git push origin" #branch


# ********************************************other****************************************
# User specific aliases and functions
#alias googler='proxychains4 googler'

#alias im="python ~/scripts/mojo_im.py "
#alias qq="python ~/scripts/mojo_im.py qq"
#alias wx="python ~/scripts/mojo_im.py wx"
#alias ttt="python ~/scripts/mojo_im.py qq printt | tail -7 | head -5"
#alias tt="python ~/scripts/mojo_im.py qq send uid "


# ********************************************************docker*******************************************
dtags(){
    for Repo in $* ; do
        curl -s -S "https://registry.hub.docker.com/v2/repositories/library/$Repo/tags/" | sed -e 's/,/,\n/g' -e 's/\[/\[\n/g' | grep '"name"' | awk -F\" '{print $4;}' | sort -fu | sed -e "s/^/${Repo}:/"
#        curl -s -S "https://registry.hub.docker.com/v2/repositories/library/$Repo/tags/" | \ 
#            sed -e 's/,/,\n/g' -e 's/\[/\[\n/g' | \ 
#            grep '"name"' | \ 
#            awk -F\" '{print $4;}' | \ 
#            sort -fu | \ 
#            sed -e "s/^/${Repo}:/"
    done
}

drm(){
    docker stop $1 && docker rm $1
}

# exec-attach $container_name
da(){
    docker exec -it $1 sh -c "cd && bash" || docker exec -it $1 sh -c "cd && sh"
}

# run $image_name $container_name #other_args;rm cmd:sh
dr(){
    args=($@)
    #docker run -itd --name $2 ${args[@]:2} $1 sh
    docker run -itd --name $2 --restart always ${args[@]:2} $1
}

# 
dlogs(){
    docker logs $1
}

# 
dps(){
    docker ps
}

# 
drm(){
    docker rm -f $1
}

# *************************************other functions****************************
rready(){
    sh ~/riven/bin/env_backup.sh
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
#ssh-agent_login(){
    #eval `ssh-agent`
    #ssh-add ~/.ssh/id_rsa.r81.key
#}

tmux_init(){
    tmux new-session -d                  # 开启一个会话(后台)
    tmux new-window                      # 开启一个窗口(新窗口)
    #tmux split-window -h                # 开启一个竖屏
    #tmux split-window -v "top"          # 开启一个横屏,并执行top命令
    #tmux -2 attach-session -d           # tmux -2强制启用256color，连接已开启的tmux
    tmux attach-session
}

ta(){
    tmux a -t $1 2>/dev/null || tmux a -t 0
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
