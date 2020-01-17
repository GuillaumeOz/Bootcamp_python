#!/usr/bin/python3

import sys

cookbook = {"sandwich":("ham, bread, cheese and tomatoes", "lunch", "10 minutes"),
	 "cake":("lour, sugar and eggs", "dessert", "60 minutes"), 
	 "salad":("avocado, arugula, tomatoes and spinach", "lunch", "15 minutes")}

user_input = 0
num = 0
loop = 1
#g_page = 3

def add_recipe(recipe, ingredients, meal, time):
	#g_page + 1
	cookbook[recipe] = ingredients
	cookbook[recipe] = meal
	cookbook[recipe] = time

def print_recipe():
#	while(page - 1 > 0):
#		print(cookbook[page])
	sys.exit(0)

def delete_recipe():
	sys.exit(0)

def print_all_recipe(): #formatting the output
	print("There is currently all the recipe of the Cookbook :")
#	page = g_page
#	page - 1
#	print(cookbook[page])
#	while(page > 0):
#		print(cookbook[page])
#		page - 1
	for key, value in cookbook.items():
    print (key, value)
	print("So now dude ?")

print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
while(loop):
	user_input = input()  
	if (user_input == "1"):
		print("Well let's add a new recipe")
		n_recipe = input("What is the name of the recipe ?\n")
		n_ingredients = input("What is your ingredients ?\n")
		n_meal = input("When did you want to eat this ?\n")
		n_time = input("What is the time of preparation ?\n")
		add_recipe(n_recipe, n_ingredients, n_meal, n_time)
		print("The recipe has been add, so what you want to do now ?")
	elif (user_input == "2"):
		sys.exit(0)
	elif (user_input == "3"):
		sys.exit(0)
	elif (user_input == "4"):
		print_all_recipe()
	elif (user_input == "5"):
		print("Cookbook closed.")
		sys.exit(1)
	else:
		print("This option does not exist, please type the corresponding number.")
		print("To exit, enter 5.")

#print(cookbook["sandwich"][0],cookbook["sandwich"][1])

