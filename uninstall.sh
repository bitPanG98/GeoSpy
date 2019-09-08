#! /bin/bash

# Copyright (C) 2016 - 2018 Entynetproject, Inc.
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

RSA="\033[31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
sleep 1
echo -e "$RS"run it as"$CE" "$YS"root"$CE"
sleep 1
echo -e "$RS"or use"$CE" "$YS"sudo"$CE"
sleep 1
exit
fi

{
rm /bin/geospy
rm /usr/local/bin/geospy
rm -r ~/geospy
} &> /dev/null
