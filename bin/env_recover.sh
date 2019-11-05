#!/bin/bash

#cp ~/riven/config/sys_config_rc/.* ~

# 把所有配置（bashrc/vimrc等）追加到当前home路径配置下 (重定向的文件不能用{}代替:暂时不生效)
sys_config_dir="$HOME/riven/config/sys_config_rc/"
#ls -a $sys_config_dir | egrep '[^.]$' | xargs -I {} cat $sys_config_dir/{} >> $HOME/{}
ls -a $sys_config_dir | egrep '[^.]$' | xargs -I {} cp $sys_config_dir/{} $HOME

. ~/.bashrc
