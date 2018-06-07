#This is from Python Crash Course Chapter 7, exercse 5
message = "In order for us to give you the correct price for your ticket, tell my your age."
message+="\nType 'quit' in order to finish your order.  "
cost = 0
while True:
    age = input(message)
    if age == 'quit':
        print("The cost of your tickets is $" + str(cost)+".")
        break
    else:
        age = int(age)
        if age < 3:
            print("The ticket for this person is free.")
        elif age < 12:
            print("The ticket for this person is $10.")
            cost += 10
        else:
            print("The ticket for this person is $15.")
            cost += 15

