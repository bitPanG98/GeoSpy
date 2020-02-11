#!/bin/bash

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"
WHS="\033[0m"

printf '\033]2;uninstall.sh\a'

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-] "$WHS"This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

{
rm /bin/quack
rm /usr/local/bin/quack
rm -rf ~/quack
rm /data/data/com.termux/files/usr/bin/quack
} &> /dev/null
