#!/bin/bash

# Copyright (C) 2016 - 2019 Entynetproject
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

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"
GNS="-e \033[32m"
GNSB="\033[1;32m"
WSW="\033[0;37m"
WS="\033[1;37m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$WS"["$RS"x"$WS"] "$RS"ERROR: "$WSW"This script must be run as root!"$CE""
   sleep 1
   exit
fi

if [[ -d ~/geospy ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/geospy.git
} &> /dev/null
fi

sleep 0.5
cd ~/geospy
chmod +x banner/banner.sh
banner/banner.sh

sleep 1
echo -e "["$GNSB"i"$CE"] Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install python
apt-get update
apt-get -y install python
apt-get -y install python-pip
apk add python
apk add python-pip
pacman -S python
pacman -S python-pip
} &> /dev/null

{
pip install setuptools
pip install -r requirements.txt
} &> /dev/null

{
cd ~/geospy/bin
cp geospy /usr/local/bin
chmod +x /usr/local/bin/geospy
cp geospy /bin
chmod +x /bin/geospy
cp geospy /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/geospy
} &> /dev/null
