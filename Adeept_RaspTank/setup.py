#!/usr/bin/python3
# File name   : setup.py
# Description : install the software for RPi 
# Author      : William
# Edited	  : seb3n
# Date        : 2021/02/12

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
'''
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
'''
print('updating and upgrading')
for x in range(1,4):
	if os.system("sudo apt-get -y update") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get -y upgrade") == 0:
		break

print('installing gpio')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-rpi.gpio") == 0:
		break

print('installing picamera')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-picamera") == 0:
		break	

print('installing pip')
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-pip") == 0:
		break		

print('installing i2c-tools')
for x in range(1,4):
	if os.system("sudo apt-get install -y i2c-tools") == 0:
		break

		
print('installing adafruit-pca9685')
for x in range(1,4):
	if os.system("sudo pip3 install adafruit-pca9685") == 0:
		break

print('installing rpi_ws281x')
for x in range(1,4):
	if os.system("sudo pip3 install rpi_ws281x") == 0:
		break

print('updating boot config file')
try:
	replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\ndtparam=i2c1=on\n')
except:
	print('try again')

print('updating pip')
for x in range(1,4):
	if os.system("sudo pip3 install -U pip") == 0:
		break

print('installing numpy')
for x in range(1,4):
	if os.system("sudo pip3 install numpy") == 0:
		break

print('installing opencv')
for x in range(1,4):
	if os.system("sudo apt-get install -y libopencv-dev python3-opencv") == 0:
		break
'''
for x in range(1,4):
	if os.system("sudo apt-get install -y libhdf5-dev") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libhdf5-serial-dev") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y build-essential pkg-config") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libgtk2.0-dev libatlas-base-dev gfortran") == 0:   ####
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libqtgui4 python3-pyqt5 libqt4-test") == 0:
		break
'''

print('installing imutils; zmq; pybase64; psutil')
for x in range(1,4):
	if os.system("sudo pip3 install imutils zmq pybase64 psutil") == 0:   ####
		break

print('clonning oblique repo.')
print('This repo is used to create an wifi access point on the Rover')
for x in range(1,4):
	if os.system("git clone https://github.com/oblique/create_ap") == 0:
		break
print('creating access point.')
try:
	os.system("cd //home/pi/development/Rover/Adeept_RaspTank/create_ap && sudo make install")
except:
	pass

print('creating access point in home dir instead.')
try:
	os.system("cd //home/pi/create_ap && sudo make install")
except:
	pass

print('installing some networking packages.')
for x in range(1,4):
	if os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
		break
'''
try:
	os.system('sudo mkdir //home/pi/.config/autostart')
	os.system('sudo touch //home/pi/.config/autostart/car.desktop')
	with open("//home/pi/.config/autostart/car.desktop",'w') as file_to_write:
		file_to_write.write("[Desktop Entry]\n   Name=Car\n   Comment=Car\n   Exec=sudo python3 //home/pi/development/Rover/Adeept_RaspTank/server/server.py\n   Icon=false\n   Terminal=false\n   MutipleArgs=false\n   Type=Application\n   Catagories=Application;Development;\n   StartupNotify=true")
except:
	pass
'''
try:
	os.system('sudo touch //home/pi/startup.sh')
	with open("//home/pi/startup.sh",'w') as file_to_write:
		file_to_write.write("#!/bin/sh\n#sleep 10s\nsudo python3 //home/pi/development/Rover/Adeept_RaspTank/server/server.py")
except:
	pass

os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')

os.system("sudo cp -f //home/pi/development/Rover/Adeept_RaspTank/server/config.txt //home/pi/config.txt")

os.system("sudo cp -f //home/pi/development/Rover/Adeept_RaspTank/server/config.txt //etc/config.txt")
os.system("sudo cp -f //home/pi/development/Rover/Adeept_RaspTank/server/config.txt //config.txt")
print('restarting')

os.system("sudo reboot")
