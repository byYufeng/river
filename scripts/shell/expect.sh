#!/usr/bin/expect

cmd=""
qes=""
ans=""

spawn $cmd

expect $qes {
    send $ans
    send "\n"
    interact
}
