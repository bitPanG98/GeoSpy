#!/bin/bash

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

N="\033[1;37m"
C="\033[0m"

CE="\033[0m"
RS="\033[1;31m"
YS="\033[1;33m"
BS="\033[1;34m"
GNS="\033[1;32m"

R="\033[1;31m"
WS="\033[0m"

printf '\033]2;install.sh\a'

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-]"$WS" This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/quack ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/quack.git
} &> /dev/null
fi
sleep 0.5
clear
sleep 0.5
echo  
cd ~/quack
cat banner/banner.txt
echo

sleep 1
echo -e ""$BS"[*]"$WS" Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install git
pkg -y install python
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install python3-pip
apk update
apk add git
apk add python3
apk add py3-pip
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm python3-pip
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y python3-pip
yum -y install git
yum -y install python3
yum -y install python3-pip
dnf -y install git
dnf -y install python3
dnf -y install python3-pip
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install pip
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y python3-pip
} &> /dev/null

{
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
} &> /dev/null

{
cd ~/quack/bin
cp quack /usr/local/bin
chmod +x /usr/local/bin/quack
cp quack /bin
chmod +x /bin/quack
cp quack /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/quack
} &> /dev/null

sleep 1
echo -e ""$GNS"[+]"$WS" Successfully installed!"$CE""
sleep 1
