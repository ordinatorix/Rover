#!/usr/bin/python3
# File name   : rover_setup.py
# Description : Install the software for Rover
# Author      : William
# Edited	  : seb3n
# Date        : 2021/08/22

import os
import time

def replace_num(file,initial,new_num):  
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

# Update and remove any unnecessary software.
print('###-------->Updating and freeing up space<--------#')
for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		break

os.system("sudo apt-get purge -y wolfram-engine")
os.system("sudo apt-get purge -y libreoffice*")
os.system("sudo apt-get -y clean")
os.system("sudo apt-get -y autoremove")

for x in range(1,4):
	if os.system("sudo apt-get -y upgrade") == 0:
		break


# Install gpio support
print('###-------->Installing gpio<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-rpi.gpio") == 0:
		break
# Install picamera support	
print('###-------->Installing picamera<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-picamera") == 0:
		break	

# Install pip
print('###-------->Installing pip<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-pip") == 0:
		break		
	
# Install I2C tools
print('###-------->Installing i2c-tools<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y i2c-tools") == 0:
		break

# Install 16-Channel servo driver.
print('###-------->Installing adafruit-pca9685<--------###')
for x in range(1,4):
	if os.system("sudo pip3 install adafruit-pca9685") == 0:
		break

# Install support for RGB LED.
print('###-------->Installing rpi_ws281x<--------###')
for x in range(1,4):
	if os.system("sudo pip3 install rpi_ws281x") == 0:
		break

# update boot config file to allow i2c
print('###-------->Updating boot config file<--------###')
try:
	replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\ndtparam=i2c1=on\n')
except:
	print('try again')

#update pip 
print('###-------->Updating pip<--------###')
for x in range(1,4):
	if os.system("sudo pip3 install -U pip") == 0:
		break

# Install numpy
print('###-------->Installing numpy<--------###')
for x in range(1,4):
	if os.system("sudo pip3 install numpy") == 0:
		break

# Install opencv
print('###-------->Installing OpenCV<--------###')
for x in range(1,4):
	if os.system("sudo apt-get install -y libopencv-dev python3-opencv") == 0:
		break

# install imutil, zmq, pybase64, psutil
print('###-------->Installing imutils; zmq; pybase64; psutil<--------###')
for x in range(1,4):
	if os.system("sudo pip3 install imutils zmq pybase64 psutil") == 0:   ####
		break
# install support for local wifi access point and create access point.
print('clonning oblique repo.')
print('This repo is used to create an wifi access point on the Rover')
for x in range(1,4):
	if os.system("git clone https://github.com/oblique/create_ap") == 0:
		break


print('creating access point.')
try:
	os.system("cd //home/pi/Rover/create_ap && sudo make install")
except:
	pass

print('creating access point in home dir instead.')
try:
	os.system("cd //home/pi/create_ap && sudo make install")
except:
	pass

# install some networking packages
print('installing some networking packages.')
for x in range(1,4):
	if os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
		break


# Create startup file.
# This file will be run on startup and have Rover awaiting connection.
try:
	os.system('sudo touch //home/pi/startup.sh')
	with open("//home/pi/startup.sh",'w') as file_to_write:
		file_to_write.write("#!/bin/sh\n#sleep 10s\nsudo python3 //home/pi/Rover/server/server.py")
except:
	pass
# Change startup file permission
os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')

os.system("sudo cp -f //home/pi/Rover/server/config.txt //home/pi/config.txt")

os.system("sudo cp -f //home/pi/Rover/server/config.txt //config.txt")

# Rebooting after install is complete
print('###-------->restarting<--------###')

# os.system("sudo reboot")
