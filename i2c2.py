#!/usr/bin/env python

import sys
import smbus
import time
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_MCP230xx")
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX

mcp = Adafruit_MCP230XX(address = 0x27, num_gpios = 16)

def reverse_int(n):
    return int(str(n)[::-1])

print("test")
# ***************************************************
# Set num_gpios to 8 for MCP23008 or 16 for MCP23017!
# If you have a new Pi you may also need to add:
# busnum = 1
# ***************************************************

# all pins out
for pins in range(3, 16):
	mcp.config(pins, mcp.OUTPUT)
	print(pins)


# all pins as high
for pins1 in range(3, 16):
	mcp.output(pins1, 0)  # Pin 0 High
print(mcp.outputvalue)
bit = (bin(mcp.outputvalue)[2:] ).zfill(16)
bit2 = str(reverse_int(bit))
print(bit)
print(bit2.zfill(16))
print(bit2[0])
