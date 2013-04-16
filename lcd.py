#!/usr/bin python

import sys
sys.path.append("/home/pi/git/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep

lcd = Adafruit_CharLCDPlate()

prevselect = 0
prevup = 0
prevdown = 0
buttons = 1
menu = 0
start = 0
print("hello")
while True:
	if menu >= 5:
		menu = 1
	if menu < 1 and start == 1:
		menu = 4
	if ((buttons) and menu == 0):
		lcd.clear()
		lcd.message("Welcome Please\nPress SELECT")
		buttons = 0
	if ((buttons) and menu == 1):
		lcd.clear()
		lcd.message("Menu 1")
		buttons = 0
	if ((buttons) and menu == 2):
		lcd.clear()
		lcd.message("Menu 2")
		buttons = 0
	if ((buttons) and menu == 3):
		lcd.clear()
		lcd.message("Menu 3")
		buttons = 0
	if ((buttons) and menu == 4):
		lcd.clear()
		lcd.message("Menu 4")
		buttons = 0
	if ((not prevselect) and lcd.buttonPressed(lcd.SELECT) and start == 1):
		print "Select"
		start = 0
		menu = 0
		buttons = 1
		sleep(0.2)
	if ((not prevselect) and lcd.buttonPressed(lcd.SELECT) and start == 0):
		print "Select"
		menu = 1
		buttons = 1
		start = 1
		sleep(0.2)
	if ((not prevup) and lcd.buttonPressed(lcd.UP)):
		print "UP"
		if start == 1:
			menu = menu + 1
			buttons = 1
	if ((not prevdown) and lcd.buttonPressed(lcd.DOWN)):
		print "DOWN"
		if start == 1:
			menu = menu - 1
			buttons = 1
		if start == 0:
			lcd.clear()
			lcd.message("Exit in 5 SEC")
			sleep(1)
			lcd.clear()
			lcd.message("Exit in 4 SEC")
			sleep(1)
			lcd.clear()
			lcd.message("Exit in 3 SEC")
			sleep(1)
			lcd.clear()
			lcd.message("Exit in 2 SEC")
			sleep(1)
			lcd.clear()
			lcd.message("Exit in 1 SEC")
			sleep(1)
			lcd.clear()
			lcd.message("Exit")
			sleep (0.5)
			lcd.clear()
			lcd.backlight(lcd.OFF)
			exit()
	
	#update previous input
	prevselect = lcd.buttonPressed(lcd.SELECT)
	prevdown = lcd.buttonPressed(lcd.DOWN)
	prevup = lcd.buttonPressed(lcd.UP)
	#slight pause to debounce
	sleep(0.05)
