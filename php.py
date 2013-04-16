#!/usr/bin/env python3

import sys
from quick2wire.gpio import pins, Out
from time import sleep
from time import time
start = time()

DEBUG = 0

led1 = pins.pin(2, direction=Out)
led2 = pins.pin(3, direction=Out)
led3 = pins.pin(4, direction=Out)

def PHP(phpvalue):
	if phpvalue == 1:
		led1.value = 1
	elif phpvalue == 2:
		led2.value = 1
	else:
		led3.value = 1	
	print ("led%s on" % phpvalue)
	print (led1.value,led2.value,led3.value)
	if DEBUG == 1:
		sleep(2)
	

def Main():
	with led1, led2, led3:

		status1 = int(sys.argv[1]) if len(sys.argv) >= 2 else "error"
		action = int(sys.argv[2]) if len(sys.argv) >= 3 else "0"
		if status1 =="error":
			print (status1)
		elif action == 1:
			print (led1.value,led2.value,led3.value)
		else:
			if status1 >= 4:
				print (status1)
				print ("Out of range")	
				sys.exit(1)				
			else:
				PHP(status1)
				print(action)
				runtime = time()-start
				print("%.2f" %runtime)
				sys.exit(0)
Main()

