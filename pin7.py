#! /usr/bin/env python

#
# Demonstrates how to enable the pull up or pull down resistors on
# the Pi's GPIO pins.
#

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.cleanup()
