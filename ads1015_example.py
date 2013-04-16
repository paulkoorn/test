#!/usr/bin/python
import sys

sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
# ============================================================================
# Example Code
# ============================================================================
ADS1015 = 0x00	# 12-bit ADC
ADS1115 = 0x01	# 16-bit ADC

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ToDo: Change the value below depending on which chip you're using!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ADS_Current = ADS1015

# Initialise the ADC using the default mode (use default I2C address)
adc = ADS1x15(ic=ADS_Current)

# Read channel 0 in single-ended mode 

#Script By Shane B.
#Website: PIPBOY3000.com -- Contribute to the OpenSource PipBoy 3000 project
#MIT LICENSE
#Power Supply of 1.8v is on Header: P9 and PIN Number: 32
#Hook the negative to Ground pins 1(or 2) on Header: P9
#Hook signal to PIN Number: 37 on Header: P9
 
#RESOURCE TUTORIAL: http://www.gigamegablog.com/2012/01/22/beaglebone-coding-101-using-the-serial-and-analog-pins/
 
#Import libraries#
##################
#No Libaries yet
 
 
#Define Functions#
##################
def average(seq, total=0.0):  
		num = 0  
		for item in seq:  
				total += item  
				num += 1  
		return total / num  
 
 
 
#Define variables#
##################
avg = 0
inputData = []
sendOutputcounter = 0
 
 
#Begin Script
#########################################################################
while(True):
		#Analog 2
		result = adc.readADCSingleEnded(0)
		inputData.append(result)
 
		#Once inputData reaches the length of 100 -- delete the most out of date input value
		if len(inputData) >= 40:
				inputData.pop(0);
 
		avg = average(inputData)
		avg = round(avg)
 
		#Slow down read out
		sendOutputcounter = sendOutputcounter + 1
		if sendOutputcounter > 500:
				sendOutputcounter = 0
				avg1 = "Ch 0=%.2fV %s" % ((avg * 0.003), avg)
				print "Ch 0=%.2fV %s" % ((result * 0.003), result)
				print avg1
				print result
		

