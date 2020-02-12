#!/bin/bash

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
