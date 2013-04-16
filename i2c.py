#!/usr/bin/env python3

import quick2wire.i2c as i2c

address = 0x27
iodira_register = 0x00
gpioa_register = 0x09
iodirb_register = 0x01
gpiob_register = 0x13

with i2c.I2CMaster() as bus:    
	#a
	bus.transaction(
        i2c.writing_bytes(address, iodira_register, 0xFF))
	#b
	bus.transaction(
        i2c.writing_bytes(address, iodirb_register, 0xFF))	
		
	reada_results = bus.transaction(
        i2c.writing_bytes(address, gpioa_register),
        i2c.reading(address, 1))
		
	readb_results = bus.transaction(
		i2c.writing_bytes(address, gpiob_register),
		i2c.reading(address, 1))
		
	gpioa_state = reada_results[0][0]
	gpiob_state = readb_results[0][0]
	
	print("%02x" % gpioa_state)
	print("%02x" % gpiob_state)