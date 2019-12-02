#!/bin/bash
#Author: fsrm

# 适用于tmux版本不匹配：protocol version mismatch
#/proc/`pgrep tmux`/exe attach
pid=`pgrep tmux`
cd /proc/$pid && ./exe attach
