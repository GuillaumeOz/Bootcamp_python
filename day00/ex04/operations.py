#!/usr/bin/python3

import sys

def two_number(a, b):
	c = a + b
	print("Sum:  ", c)
	c = a - b
	print("Difference:  ", c)
	c = a * b
	print("Product:  ", c)
	if (b == 0):
		print("Quotient:    ERROR (div by zero)")
		print("Remainder:    ERROR (modulo by zero)")
		sys.exit(1)
	c = a / b
	print("Quotient:  ", c)
	c = a % b
	print("Remainder:  ", c)

if ((len(sys.argv) < 1 or len(sys.argv) > 3)):
	print("InputError: too many arguments")
	print("Usage: python operations.py")
	print("Example:")
	print("python operations.py 10 3")
	sys.exit(1)
try:
    num = int(sys.argv[1])
except ValueError:
	print("InputError: only numbers")
	sys.exit(1)
try:
    num = int(sys.argv[2])
except ValueError:
	print("InputError: only numbers")
	sys.exit(1)
two_number(int(sys.argv[1]), int(sys.argv[2]))
