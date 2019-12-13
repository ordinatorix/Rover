#!/usr/bin/env python3
# File name   : servo.py
# Description : Control Motor
# Product     : RaspTank  
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/12/27
#scp ../server/servo.py pi@192.168.0.13:/home/pi/adeept_rasptank/server/servo.py

from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


def num_import_int(initial):		#Call this function to import data from '.txt' file
	global r
	with open("//etc/config.txt") as f:
		for line in f.readlines():
			if(line.find(initial) == 0):
				r=line
	begin=len(list(initial))
	snum=r[begin:]
	n=int(snum)
	return n

print('Loading...')
for i in range(0,16):
	exec('L%d_MAX=num_import_int("L%d_MAX:")'%(i,i))
	exec('L%d_MIN=num_import_int("L%d_MIN:")'%(i,i))
	for n in range(1,11):
		exec('L%d_ST%d=num_import_int("L%d_ST%d:")'%(i,n,i,n))
print('Setting up server...')

org_pos = L11_ST4

def camera_ang(direction, ang):
	global org_pos
	if ang == 0:
		ang=4
	if direction == 'lookdown':
		if org_pos >= L11_MIN:
			org_pos+=ang
		else:
			org_pos = L11_MIN
	elif direction == 'lookup':
		if org_pos <= L11_MAX:
			org_pos-=ang
		else:
			org_pos = L11_MAX
	elif direction == 'home':
		org_pos = L11_MAX
	else:
		pass
	#print(ang)
	pwm.set_pwm(11,0,org_pos)


def hand(command):
	if command == 'out':
		pwm.set_pwm(13, 0, L13_ST3)
		pwm.set_pwm(12, 0, L12_ST4)
		time.sleep(0.5)
		pwm.set_pwm(13, 0, L13_ST2)
		pwm.set_pwm(12, 0, L12_ST2)
	elif command == 'in':
		pwm.set_pwm(12, 0, L12_ST1)
		pwm.set_pwm(13, 0, L13_ST1)
		


def cir_pos(pos):
	pwm.set_pwm(14, 0, L14_ST2+30*pos)


def catch(pos):
	pwm.set_pwm(15, 0, L15_ST2+15*pos)


def hand_pos(pos,data):
	cur_pos_L12 = L12_ST6-24*pos
	cur_pos_L13 = L13_ST1-15*pos
	if 'out' == data:
		#pos has been increased
		prev_pos_L12 = L12_ST6-24*(pos-1)
		prev_pos_L13 = L13_ST1-15*(pos-1)
		while prev_pos_L12>cur_pos_L12 or prev_pos_L13<cur_pos_L13:
			if prev_pos_L12 == cur_pos_L12:
				prev_pos_L13-= 1
				pwm.set_pwm(13,0,prev_pos_L13)
			elif prev_pos_L13 == cur_pos_L13:
				prev_pos_L12 -= 1
				pwm.set_pwm(12,0,prev_pos_L12)
			else:
				prev_pos_L12-=1
				prev_pos_L13-=1
				pwm.set_pwm(12,0,prev_pos_L12)
				pwm.set_pwm(13,0,prev_pos_L13)

	elif 'in' == data:
		#pos has been decreased
		prev_pos_L12 = L12_ST6-24*(pos+1)
		prev_pos_L13 = L13_ST1-15*(pos+1)
		while prev_pos_L12<cur_pos_L12 or prev_pos_L13>cur_pos_L13:
			if prev_pos_L12 == cur_pos_L12:
				prev_pos_L13+= 1
				pwm.set_pwm(13,0,prev_pos_L13)
			elif prev_pos_L13 == cur_pos_L13:
				prev_pos_L12 += 1
				pwm.set_pwm(12,0,prev_pos_L12)
			else:
				prev_pos_L12+=1
				prev_pos_L13+=1
				pwm.set_pwm(12,0,prev_pos_L12)
				pwm.set_pwm(13,0,prev_pos_L13)


	"""if pos <= 4:
		pwm.set_pwm(12, 0, L12_ST6-30*pos)
		pwm.set_pwm(13, 0, L13_ST1-30*pos)
		#print(L12_ST6-30*pos)
	elif pos >16:
		pwm.set_pwm(13, 0 , L13_ST4+7*(pos-7))
	else:
		pwm.set_pwm(12, 0, (L12_ST6-24*pos))
		pwm.set_pwm(13, 0, L13_ST4+6+(pos+4))
	"""

#def hand_reach(pos):



def clean_all():
	pwm.set_pwm(0, 0, 0)
	pwm.set_pwm(1, 0, 0)
	pwm.set_pwm(2, 0, 0)
	pwm.set_pwm(3, 0, 0)
	pwm.set_pwm(4, 0, 0)
	pwm.set_pwm(5, 0, 0)
	pwm.set_pwm(6, 0, 0)
	pwm.set_pwm(7, 0, 0)
	pwm.set_pwm(8, 0, 0)
	pwm.set_pwm(9, 0, 0)
	pwm.set_pwm(10, 0, 0)
	pwm.set_pwm(11, 0, 0)
	pwm.set_pwm(12, 0, 0)
	pwm.set_pwm(13, 0, 0)
	pwm.set_pwm(14, 0, 0)
	pwm.set_pwm(15, 0, 0)


if __name__ == '__main__':
	try:
		pos_input = 0
		OUT = 1
		while 1:
			a=input()
			if OUT == 1:
				if pos_input < 13:
					pos_input+=1
				else:
					print('MAX')
					OUT = 0
			else:
				if pos_input > 1:
					pos_input-=1
				else:
					print('MIN')
					OUT = 1
			catch(pos_input)
			print(pos_input)

			pass
	except KeyboardInterrupt:
		clean_all()

