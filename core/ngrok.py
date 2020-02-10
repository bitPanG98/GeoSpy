#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import sys
import os, platform
import subprocess
import socket
import os.path as path
from multiprocessing import Process

class ngrok(object):
	def __init__(self, authtoken, port, nT, hash):
		if authtoken:
			self.token = authtoken
		else:
			print "Can't use Ngrok without a valid token"
		system_type = os.name
		system_name = platform.system()
		system_architecture = platform.architecture()[0]

		str_ngrok = './ngrok'
		if "nt" in system_type:
			str_ngrok = './ngrok.exe'
		
		if path.exists(str_ngrok):
			pass
		else:
			import urllib2

			if "posix" in system_type:
				if "arwin" in system_name:
					if "64" in system_architecture:
						download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip"
					else:
						download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-386.zip"
				else:
					if "64" in system_architecture:
						download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
					else:
						download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip"
			elif "nt" in system_type:
				if "64" in system_architecture:
					download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"
				else:
					download_link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-386.zip"
			else:
				sys.exit(0)
            
			filename = "ngrok.zip"
			
			download = urllib2.urlopen(download_link)
			saved_file=file(filename,"w")
			saved_file.write(download.read())
			saved_file.close()
			
			result = subprocess.check_output(["unzip", filename]) 
			os.remove(filename)

		subprocess.check_output([str_ngrok, "authtoken", authtoken]) 
		
		if nT > 0:
			pNg = Process(target=start_ngrok, args=(str(port), hash, 1))
			pNg.start()

def start_ngrok(port, hash, f=0):
	if f != 0:
		str_ngrok = './ngrok'
		system_type = os.name
		if "nt" in system_type:
			str_ngrok = './ngrok.exe'
		result = subprocess.check_output([str_ngrok, "http", port, '-log', hash + '.nlog'])
		print result
