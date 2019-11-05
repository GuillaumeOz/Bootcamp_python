#!/usr/bin/python3

import sys

words = []

def reverse(word):
    return [char.upper() if char.islower() else char.lower() for char in word]

if (len(sys.argv) > 1):
    args = sys.argv[1:]
    args = args[::-1]
    words = ["".join(reverse(word[::-1])) for word in args]
    words = " ".join(words)
    print(words)