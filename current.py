#!/usr/bin/python

import sys
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15

# ============================================================================
# Example Code
# ============================================================================
ADS1015 = 0x00	# 12-bit ADC
ADS1115 = 0x01	# 16-bit ADC
vref = 5 ##vref voltage
bitvalue = 4096 # 12bit
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ToDo: Change the value below depending on which chip you're using!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ADS_Current = ADS1015

# Initialise the ADC using the default mode (use default I2C address)
adc = ADS1x15(ic=ADS_Current)

# Read channel 0 in single-ended mode 
result = adc.readADCSingleEnded(0)
while True:
if ADS_Current == ADS1015:
  # For ADS1015 at max range (+/-6.144V) 1 bit = 3mV (12-bit values)
  print "Channel 0 = %.3f V" % (result * 0.003)
  bitcalc = result / bitvalue
  valuepaul = bitcalc * vref
  print(valuepaul+"V")



