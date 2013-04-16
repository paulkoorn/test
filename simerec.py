#!/usr/bin/env python3

from quick2wire.gpio import pins, Out
from time import sleep

pinspc = pins.pin(5, direction=Out)

with pinspc:

	def PC_OFF():
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)



	def PC_ON():
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.004)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)


	def PC_OFF_FORCED():
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.004)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)


	def PC_REBOOT():
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.004)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.004)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)


	def PC_REBOOT_FORCED():
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.004)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.002)
		pinspc.value = 0
		sleep(0.002)
		pinspc.value = 1
		sleep(0.008)
		pinspc.value = 0
		sleep(0.002)

	
	PC_OFF()
	#PC_ON()
	#PC_OFF_FORCED()
	#PC_REBOOT()
	#PC_REBOOT_FORCED()	
	print ("done")
