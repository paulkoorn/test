#!/usr/bin/env python3

from time import sleep
from quick2wire.gpio import pins, Out, In

#initialise a previous input variable to 0 (assume button not pressed last)
prevbutton1 = 0
button1 = pins.pin(0, direction=In)
runled = pins.pin(1, direction=Out)
ledstatus = 0

with button1, runled:
	while True:
		#take a reading
		input1 = button1.value
		#if the last reading was low and this one high, print
		if ((not prevbutton1) and input1):
			print("Button pressed")
			print(input1)
			print(prevbutton1)
			if ledstatus == 0:
				runled.value = 1
				ledstatus = 1
			else:
				runled.value = 0
				ledstatus = 0
		#update previous input
		prevbutton1 = input1
		#slight pause to debounce
		sleep(0.05)