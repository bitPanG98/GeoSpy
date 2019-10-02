#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
#
#**
#
##########################################
# GeoSpy | People tracker on the Internet #
##########################################
#
# Learn to track the world, to avoid being traced
#
# @version     2.0
# @link        https://github.com/entynetproject/geospy
# @author      Entynetproject
# @copyright   2018 by Entynetproject / <entynetproject@gmail.com>
#
# This file is the boot in GeoSpy.
# For full copyright information this visit: https://github.com/entynetproject/geospy
#
#**
#
###############################################
                                              #
import os                                     #
                                              #
printf '\033]2;GeoSpy Console\a'              #
                                              #
from core.utils import utils                  #
from core.geospy import GeoSpy                #
from core.db import Database                  #
from time import sleep                        #                  
try:                                          #
    import flask                              #
    import flask_socketio                     #                                
except:                                       ############################################
    utils.Go("\t\nPlease install requirements.txt libraries, you can do it executing:")  #
    utils.Go("\t\npip install -r requirements.txt")  #####################################
######################################################

# We generalize the main class of <GeoSpy>
trackPeople = GeoSpy()

# call class database
generateData = Database()
if generateData.firstTime:
    utils.Go("\033[H\033[J")         
    utils.Go("\t" + utils.Color['white'] + "--" + " " + "v" + utils.Color['redBold'] + "2.0" + utils.Color['white'] + " " + "--" + "\n" + utils.Color['white'])
    utils.Go(utils.Color['whiteBold'] + "Welcome " + utils.Color['greenBold'] + os.uname()[1].upper() + utils.Color['whiteBold'] + " to GeoSpy" + utils.Color['white'])
    utils.Go("------")
    utils.Go("This is an exclusive version for researchers, or professionals \nwho are dedicated to research, we hope you enjoy." + "\n")
    utils.Go(utils.Color['whiteBold'] + "DISCLAIMER" + utils.Color['white'])
    utils.Go("------")
    utils.Go("This is a monitoring and research tool " + utils.Color['whiteBold'] + "OSINT" + utils.Color['white'] + ", which is distributed \nfor educational and investigative purposes, the person who has bought \nor uses this tool is responsible for its proper use or actions committed, \n" + utils.Color['whiteBold'] + "Entynetproject" + utils.Color['white'] + " is not responsible for the use or the scope that \npeople can have through this software." + "\n")
    utils.Go(utils.Color['whiteBold']+ "CREATOR" + utils.Color['white'])
    utils.Go("------")
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "Developer: " + utils.Color['white'] + "Entynetproject" + utils.Color['white'])
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "Twitter: " + utils.Color['white'] + "https://twitter.com/entynetproject/")
    utils.Go(utils.Color["white"] + "- " + utils.Color["greenBold"] + "Site: " + utils.Color['white'] + "http://entynetproject.simplesite.com/" + utils.Color['white'] + "\n")
    sleep(3)
    utils.Go("Press enter to continue...")
    raw_input()

# check OS
trackPeople.loadCheck()

# Request root home to run <GeoSpy> with all permissions
trackPeople.rootConnection()

# Call the creation of the database when you open this file.
generateData.loadDatabase()

if __name__ == "__main__":
    try:
        # General expression this is expressed after the root
        trackPeople.main()
    except Exception as error:
        # Result of error
        utils.Go(utils.Color['whiteBold'] + "[" + utils.Color['redBold'] + "x" + utils.Color['whiteBold'] + "]" + utils.Color['redBold'] + " " + "ERROR: " + utils.Color['white'] + "%s" % error)
