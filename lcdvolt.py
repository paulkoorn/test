#!/usr/bin/python

import sys
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_ADS1x15")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep
from Adafruit_ADS1x15 import ADS1x15

ADS1015 = 0x00
ADS_Current = ADS1015
adc = ADS1x15(ic=ADS_Current)
lcd = Adafruit_CharLCDPlate()
lcd.backlight(lcd.YELLOW)
counter = 0
total = 0
total1 = 0
ms = 200
calibratie = 0.9
startvolt = 0.975
while True:
	try:
		result = adc.readADCSingleEnded(0)
		result1 = adc.readADCSingleEnded(1)
		total = total + result
		total1 = total1 + result1
		counter = counter + 1
		if counter >= ms:
			counter = 0
			result = total / ms
			result1 = total1 / ms
			total = 0
			total1 = 0
			amp = result1 * 0.003
			print amp
			amp = amp - startvolt
			print amp
			amp = amp / calibratie
			print amp
			amp = amp * 1000
			memo = "Ch 0=%.2fV %s \nCh 1=%.0fmA %s" % ((result * 0.003), result, amp, result1)
			print memo
			sleep(ms / 1000)
			lcd.clear()
			lcd.message(memo)		
	except KeyboardInterrupt:
		print "\nclean exit"
		lcd.clear()
		lcd.backlight(lcd.OFF)
		exit()
	