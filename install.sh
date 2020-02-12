#!/bin/bash



printf '\033]2;install.sh\a'

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "[ERROR] "$WHS"This script must be run as root!" 1>&2
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
cd ~/quack
echo -e """     
  █████   █    ██  ▄▄▄       ▄████▄   ██ ▄█▀
▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
   ░   ░  ░░░ ░ ░   ░   ▒   ░        ░ ░░ ░ 
    ░       ░           ░  ░░ ░      ░  ░   
                            ░               
"""
echo

sleep 1
echo -e "[BEGIN] Installing dependencies..."
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
echo "[SUCCESS] Successfully installed!"
sleep 1
