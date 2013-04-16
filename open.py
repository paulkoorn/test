#!/usr/bin/env python3

from time import sleep
from quick2wire.gpio import pins, Out, In, Pin
import subprocess

button = pins.pin(0, direction=In)
runled = pins.pin(1, direction=Out)
led1 = pins.pin(2, direction=Out)
led2 = pins.pin(3, direction=Out)
led3 = pins.pin(4, direction=Out)
print("go")
#led1.open()
#led2.open()
#led3.open()
led1.close()
Pin(23).unexport()
Pin(22).unexport()
