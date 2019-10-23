#! /bin/bash

# Copyright (C) 2016 - 2018 Entynetproject
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use the software except in compliance with the License.
#
# You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# Disclaimer:
# This tool has been published educational purposes. It is intended to teach 
# people how bad guys could track them, monitor them or obtain information from 
# their credentials, we are not responsible for the use or the scope that someone 
# may have through this project. We are totally convinced that if we teach how 
# vulnerable things really are, we can make the Internet a safer place.

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RSA"*"$CE"] "$RSA"This script must be run as "$YSA"root"$CE""
   sleep 1
   exit
fi

if [[ -d ~/geospy ]]
then
cd ~/geospy/bin
{
cp geospy /usr/local/bin
chmod +x /usr/local/bin/geospy
cp geospy /bin
chmod +x /bin/geospy
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/geospy.git
cd ~/geospy/bin
cp geospy /usr/local/bin
chmod +x /usr/local/bin/geospy
cp geospy /bin
chmod +x /bin/geospy
} &> /dev/null
fi
sleep 0.5
cd ~/geospy
python banner.py

if [[ -f /etc/geospy.conf ]]
then

CONF="$( cat /etc/geospy.conf )"
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else 
echo ""$GNS"Installing dependencies..."$CE""
pkg update
pkg install python3
pkg install python3-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python3
apt-get install python3-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python3
apt-get install python3-pip
fi
fi

else
read -e -p $'\033[34m- Select your architecture (amd/intel/arm) \033[33m~> ' CONF
if [[ "$CONF" = "" ]]
then
exit
else
if [[ "$CONF" = "arm" ]]
then
read -e -p $'\033[34mIs this a single board computer (yes/no)? \033[33m~> ' PI
if [[ "$PI" = "yes" ]]
then
echo "amd" >> /etc/geospy.conf
CONF="amd"
else
echo "$CONF" >> /etc/geospy.conf
fi
fi
fi
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else 
echo ""$GNS"Installing dependencies..."$CE""
pkg update
pkg install python3
pkg install python3-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python3
apt-get install python3-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$GNS"Installing dependencies..."$CE""
else
echo ""$GNS"Installing dependencies..."$CE""
apt-get update
apt-get install python3
apt-get install python3-pip
fi
fi
fi

pip3 install -r requirements.txt
