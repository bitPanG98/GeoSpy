#!/bin/bash

# Copyright (C) 2019, Entynetproject. All Rights Reserved.
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
WSW="\033[0;77m"
WS="\033[1;77m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$WS"["$RS"x"$WS"] "$RS"ERROR: "$WSW"This script must be run as root!"
   sleep 1
   exit
fi

{
rm /bin/geospy
rm /usr/local/bin/geospy
rm -rf ~/geospy
rm /etc/geospy.conf
rm /data/data/com.termux/files/usr/bin/geospy
} &> /dev/null
