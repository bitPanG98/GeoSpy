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

import os
import wget
import platform

if platform.system() == "Windows":
	winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
	winpcap_dir = os.environ["ProgramFiles(x86)"] + "\\WinPcap"
	if not os.path.exists(winpcap_dir):
		print("[WARNING] Attention! Component [WinPcap] is not installed!\n    Do you want to install it automatically? (y/n)")
		if input(" >>> ").lower() in ("y", "yes", "1"):
			winpcap_installer = wget.download(winpcap_url)
			os.startfile(winpcap_installer)
			print("Please restart Quack Toolkit.")
			exit()
