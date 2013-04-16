#!/usr/bin python

import sys
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep


lcd = Adafruit_CharLCDPlate()
str_pad = " " * 16  
my_long_string = "this is a string that needs to scroll"  
my_long_string = str_pad + my_long_string  
def Scroll():
	lcd.clear()
	for i in range (0, len(my_long_string)):  
		lcd_text = my_long_string[i:(i+15)]  
		print lcd_text
		print i
		lcd.backlight(lcd.ON)
		lcd.message(lcd_text)
		sleep(0.4)
	Scroll()
while True:
	try:
		Scroll()
	except KeyboardInterrupt:
		print "\nclean exit"
		lcd.clear()
		lcd.backlight(lcd.OFF)
		exit()