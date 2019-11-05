#!/usr/bin/python3

import sys

none = ""
nbchar = 0
upper_case = 0
lower_case = 0
punctuation_marks = 0
spc = 0

args = sys.argv[1]

if (arg == none):
    print("What is the text to analyse?")
    sys.exit(1)


print ("The text contains nbchar characters:")
print ("- ",upper_case ," upper letters")
print ("- ",lower_case ," lower letters")
print ("- ",punctuation_marks ," punctuation marks")
print ("- ",spc ," spaces")

text_analyser(arg)