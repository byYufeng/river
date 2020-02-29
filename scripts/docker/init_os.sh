#!/bin/bash
#Author: fsrm

create_user(){
    USER0=""
    useradd $USER0
    passwd $USER0
    # ...
    sudo echo "$USER0       ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
}

# centos7: yum&epel >ref: https://mirrors.163.com/.help/centos.html
config_yum(){
    cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
    yum install -y wget
    wget https://mirrors.163.com/.help/CentOS7-Base-163.repo -O /etc/yum.repos.d/CentOS-Base.repo
    yum clean all && yum makecache
    yum -y install epel-release
    wget  http://mirrors.aliyun.com/repo/epel-7.repo -O /etc/yum.repos.d/epel.repo
}

config_pip(){
    yum -y install python python-pip
    mkdir -p ~/.pip && echo -e '[global]\nindex-url = http://mirrors.aliyun.com/pypi/simple/\ntrusted-host = mirrors.aliyun.com' >> ~/.pip/pip.conf 
    pip install --upgrade pip
    #pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
}

install(){
    yum -y install vim git tmux tree
}

#create_user
config_yum
config_pip
install
