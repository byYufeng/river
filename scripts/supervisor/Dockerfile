FROM centos:7
MAINTAINER fsrm
RUN yum install -y wget \
    && wget https://mirrors.163.com/.help/CentOS7-Base-163.repo -O /etc/yum.repos.d/CentOS-Base.repo \
    && yum clean all \
    && yum makecache \
    && yum install -y epel-release \
    && yum install -y supervisor
