#!/usr/bin/env python3

from time import sleep
from quick2wire.gpio import pins, Out, In

button = pins.pin(0, direction=In)
runled = pins.pin(1, direction=Out)
led1 = pins.pin(2, direction=Out)
led2 = pins.pin(3, direction=Out)
led3 = pins.pin(4, direction=Out)
print("go")
with button, runled, led1, led2, led3:
	 
	while True:
		if button.value == 1:
			runled.value = 1
			led1.value = 1
			led2.value = 1
			led3.value = 1
			print("started")
			sleep(5)
		elif button.value != 1:	
			runled.value = 0
			led3.value = 0
			sleep(2)
			led2.value = 0
			sleep(2)
			led1.value = 0
			sleep(2)
			print("stopped", end='\r')