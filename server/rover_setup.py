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



# # Install some needed dev tools to help with OpenCV configurations.
# print('###-------->Installing dev tools<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y build-essential cmake pkg-config") == 0:   ####
# 		break

# # Install image I/O packages.
# print('###-------->Installing image I/O packages<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libjpeg-dev libtiff-dev libjasper-dev libpng-dev") == 0:   ####
# 		break

# # Install some video I/O packages.
# print('###-------->Installing video I/O packages<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev") == 0:   ####
# 		break

# # Install more video I/O packages.
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libxvidcore-dev libx264-dev") == 0:   ####
# 		break

# # Install GTK development library.
# print('###-------->Installing GTK dev library<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libgtk-3-dev") == 0:   ####
# 		break

# # Install a package which may reduce pesky GTK warnings:
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libcanberra-gtk*") == 0:   ####
# 		break

# # Install numerical optimization packages
# print('###-------->Installing numerical optimization packages<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libatlas-base-dev gfortran") == 0:   ####
# 		break

# # Install python 3 development headers
# print('###-------->Installing python3 dev headers<--------###')
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y python3-dev") ==0:
# 		break

# # Navigate to home folder
# print('###-------->Navigating to home folder<--------###')
# for x in range(1,4):
# 	if os.system("cd ~") ==0:
# 		break

# # Download OpenCV archives
# print('###-------->Downloading OpenCV archives<--------###')
# for x in range(1,4):
# 	if os.system("wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip") ==0:
# 		break


# for x in range(1,4):
# 	if os.system("wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip") ==0:
# 		break

# # Unzip archive downloaded
# print('###-------->Unziping archive<--------###')
# for x in range(1,4):
# 	if os.system("unzip opencv.zip") ==0:
# 		break

# for x in range(1,4):
# 	if os.system("unzip opencv_contrib.zip") ==0:
# 		break

# # Renaming directories
# print('###-------->Renaming directories<--------###')
# for x in range(1,4):
# 	if os.system("mv opencv-4.0.0 opencv") ==0:
# 		break

# for x in range(1,4):
# 	if os.system("mv opencv_contrib-4.0.0 opencv_contrib") ==0:
# 		break


# # Build OpenCV using CMake
# print('###-------->Building OpenCV with CMake<--------###')
# for x in range(1,4):
# 	if os.system("cd ~/opencv") ==0:
# 		break

# for x in range(1,4):
# 	if os.system("mkdir build") ==0:
# 		break

# for x in range(1,4):
# 	if os.system("cd build") ==0:
# 		break

# for x in range(1,4):
# 	if os.system("cmake -D CMAKE_BUILD_TYPE=RELEASE \
#     -D CMAKE_INSTALL_PREFIX=/usr/local \
#     -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
#     -D ENABLE_NEON=ON \
#     -D ENABLE_VFPV3=ON \
#     -D BUILD_TESTS=OFF \
#     -D OPENCV_ENABLE_NONFREE=ON \
#     -D INSTALL_PYTHON_EXAMPLES=OFF \
#     -D BUILD_EXAMPLES=OFF ..") ==0:
# 		break




	
# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libqtgui4 python3-pyqt5 libqt4-test") == 0:
# 		break

# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libhdf5-dev") == 0:   ####
# 		break

# for x in range(1,4):
# 	if os.system("sudo apt-get install -y libhdf5-serial-dev") == 0:   ####
# 		break


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

# '''
# try:
# 	os.system('sudo mkdir //home/pi/.config/autostart')
# 	os.system('sudo touch //home/pi/.config/autostart/car.desktop')
# 	with open("//home/pi/.config/autostart/car.desktop",'w') as file_to_write:
# 		file_to_write.write("[Desktop Entry]\n   Name=Car\n   Comment=Car\n   Exec=sudo python3 //home/pi/Rover/server/server.py\n   Icon=false\n   Terminal=false\n   MutipleArgs=false\n   Type=Application\n   Catagories=Application;Development;\n   StartupNotify=true")
# except:
# 	pass
# '''

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

os.system("sudo cp -f //home/pi/Rover/server/config.txt //etc/config.txt")
os.system("sudo cp -f //home/pi/Rover/server/config.txt //config.txt")

# Rebooting after install is complete
print('###-------->restarting<--------###')

# os.system("sudo reboot")
