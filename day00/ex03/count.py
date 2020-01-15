#!/usr/bin/python3

import string

string_int = ""

def text_analyzer(texte):
	print ("- ", sum(1 for a in string_int if a.isupper()) ," upper letters")
	print ("- ", sum(1 for b in string_int if b.islower()) ," lower letters")
	print ("- ", sum(1 for c in string_int if c in string.punctuation)," punctuation marks")
	print ("- ", string_int.count(' ')," spaces")

while(string_int == ""):
	string_int = input("What is the text to analyse?")
print ("The text contains nbchar characters:")
text_analyzer(string_int)