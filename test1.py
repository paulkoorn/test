#!/usr/bin/env python3

from time import sleep
from quick2wire.gpio import pins, Out, In

button = pins.pin(0, direction=In)
led = pins.pin(1, direction=Out)

with button, led:
    while True:
	if button.value == 1:
		led.value = 1
		print(led.value)
	else:
		led.value = 0