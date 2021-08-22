#!/usr/bin/python3
# File name   : controller_setup.py
# Description : Install the software for controller 
# Author      : seb3n
# Date        : 2021/08/22

import os
import time


# We will try to run each install command up to 4 times; then move on to the next

# update and upgrade;
print("###-------->Updating and packages and removing unnecessary ones<--------###")
for x in range(1,4):
	if os.system(" apt-get update") == 0:
		break
# remove extra software if any.
os.system(" apt-get purge -y wolfram-engine")
os.system(" apt-get purge -y libreoffice*")
os.system(" apt-get -y clean")
os.system(" apt-get -y autoremove")

for x in range(1,4):
	if os.system(" apt-get -y upgrade") == 0:
		break

# Install pip
print('###-------->Installing pip<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-pip") == 0:
		break		


# Update pip
print("###--------->Updating pip<--------###")
for x in range(1,4):
	if os.system(" pip3 install -U pip") == 0:
		break

# Install numpy library
print("###-------->Installing numpy<--------###")
for x in range(1,4):
	if os.system(" pip3 install numpy") == 0:
		break

# Install openCV library
print("###-------->Installing OpenCV<--------###")
for x in range(1,4):
	if os.system(" apt-get install -y libopencv-dev python3-opencv") == 0:
		break

# Install imutil, pyzmq, pybase64 & psutil
print("###-------->Installing imutils; pyzmq; pybase64 & psutil<--------###")
for x in range(1,4):
	if os.system(" pip3 install imutils pyzmq pybase64 psutil") == 0:   ####
		break

# Restart system once all install /update is done.
print('###-------->Restarting<--------###')
os.system("sudo reboot")
