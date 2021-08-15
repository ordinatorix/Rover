#!/usr/bin/python3
# File name   : setup.py
# Description : install the software for RPi 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

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
# update and upgrade;
# remove extra software if any.
for x in range(1,4):
	if os.system(" apt-get update") == 0:
		break

os.system(" apt-get purge -y wolfram-engine")
os.system(" apt-get purge -y libreoffice*")
os.system(" apt-get -y clean")
os.system(" apt-get -y autoremove")

for x in range(1,4):
	if os.system(" apt-get -y upgrade") == 0:
		break

# for x in range(1,4):
# 	if os.system(" apt-get update") == 0:
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get upgrade") == 0:
# 		break

# install pip
print('installing pip')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-pip") == 0:
		break		

for x in range(1,4):
	if os.system(" sudo apt-get install -y i2c-tools") == 0:
		break

for x in range(1,4):
	if os.system(" pip3 install adafruit-pca9685") == 0:
		break

for x in range(1,4):
	if os.system(" pip3 install rpi_ws281x") == 0:
		break

try:
	replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
except:
	print('try again')

# Update pip
for x in range(1,4):
	if os.system(" pip3 install -U pip") == 0:
		break

# for x in range(1,4):
# 	if os.system(" pip3 install numpy") == 0:
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libopencv-dev python3-opencv") == 0:
# 		break
# '''
# for x in range(1,4):
# 	if os.system(" apt-get install -y libhdf5-dev") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libhdf5-serial-dev") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y build-essential pkg-config") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libgtk2.0-dev libatlas-base-dev gfortran") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system(" apt-get install -y libqtgui4 python3-pyqt5 libqt4-test") == 0:
# 		break
# '''
for x in range(1,4):
	if os.system(" pip3 install imutils pyzmq pybase64 psutil") == 0:   ####
		break

for x in range(1,4):
	if os.system("git clone https://github.com/oblique/create_ap") == 0:
		break

try:
	os.system("cd //home/pi/Documents/Rover/create_ap &&  make install")
except:
	pass

try:
	os.system("cd //home/pi/create_ap &&  make install")
except:
	pass

for x in range(1,4):
	if os.system(" sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
		break


os.system("sudo cp -f //home/pi/Documents/Rover/server/config.txt //home/pi/config.txt")

os.system("sudo cp -f //home/pi/Documents/Rover/server/config.txt //etc/config.txt")
os.system("sudo cp -f //home/pi/Documents/Rover/server/config.txt //config.txt")
print('restarting')

# os.system("sudo reboot")
