#!/bin/bash
#Author: fsrm

ls logs | grep ERROR | awk -F'_' '{print $1}' | xargs -I {} sh daily_submit.sh {}
