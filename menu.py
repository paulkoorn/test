#!/usr/bin/env python3

import signal
signal.signal(signal.SIGINT, lambda x,y: exit())

def Back():
	back = input('go back y/n? ')
	if back == "y":
		Menu()
	elif back == "n":
		exit()
	else:
		print("That was not y/n.")
		Back()
def Option0():
	print("0")
	Back()
def Option1():
	print("1")
	Back()
def Option2():
	print("2")
	Back()
options = ['Option 0', 'Option 1', 'Option 2']
callbacks = [Option0, Option1, Option2]
def Menu():
	for i,option in enumerate(options):
		print('%s. %s' % (i, option)) # display all options
	print("9. Exit")
	try:
		choice = int(input('your choice 0-%s? ' % (i)))
		if choice <= i:
			callbacks[choice]() # call correspondending function 
		elif choice == 9:
			print("Exit")
			exit()
		else:
			print("Choise out off range 0-%s" %(i))
			Menu()
	except ValueError:
		print("That was not a number.")
		Menu()
Menu()