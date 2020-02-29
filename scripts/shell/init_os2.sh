#!/bin/bash
#Author: fsrm

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
    mkdir -p ~/.pip && echo '[global]' > ~/.pip/pip.conf && echo 'index-url = http://mirrors.aliyun.com/pypi/simple/' >> ~/.pip/pip.conf
    pip install --upgrade pip
    #pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
}

install_apps(){
    yum -y install vim tmux tree
}

install_docker(){
    sudo yum -y install docker
    sudo usermod -a -G dockerroot $USER
    sudo systemctl restart docker
}

install_riven(){
    cd && git clone $ .
    riven/bin/env_recover.sh
}

#sudo_nopassword
config_yum
config_pip
install_apps
