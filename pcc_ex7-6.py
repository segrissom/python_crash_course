#Python Crash Course Chapter 7, exercise 6
#This exercise requests that you rehash either 5 or 6
#and add certain things to it - I am going to redo 5

message = "In order for us to give you the correct price for your ticket, tell my your age."
message+="\nType 'quit' in order to finish your order.  "
cost = 0
while True:
    age = input(message)
#Need to add a conditional test in the while statement to stop the loop
    while age != 'quit':
        age = int(age)
        if age < 3:
            print("The ticket for this person is free.")
        elif age < 12:
            print("The ticket for this person is $10.")
            cost += 10
        else:
            print("The ticket for this person is $15.")
            cost += 15
