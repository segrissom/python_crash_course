#This is from Python Crash Course Chapter 7's exercise 2
greeting = "Hello and welcome to Chili's."
greeting += "\nHow many are in your party?"
num_in_group = input(greeting)
#now need to convert into a num in order to compare
num_in_group = int(num_in_group)
#Now it asks for us to print statements depending on group size
if num_in_group>8:
    print("I'm sorry, but you'll have to wait for a table.")
else:
    print("Your table is ready!")