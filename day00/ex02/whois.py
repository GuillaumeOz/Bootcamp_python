#!/usr/bin/python3

import sys

if (len(sys.argv) == 1):
	sys.exit(1)
if (len(sys.argv) != 2):
    print("ERROR")
    sys.exit(1)
try:
    num = int(sys.argv[1])
except ValueError:
	print("ERROR")
	sys.exit(1)
if ((len(sys.argv) > 1) and (len(sys.argv) < 3)):
	num = int(sys.argv[1])
	if (num == 0):
   		print("I'm Zero.")
	elif(num % 2) == 0:
   		print("I'm Even.")
	else:
		print("I'm Odd.")