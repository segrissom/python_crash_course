# This is from Python Crash Course Chapter 10, exercise 5


message = "Please enter a number: "
message2 = "Please enter a second number: "
num_1 = input(message)
num_2 = input(message2)
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print("The sum of the numbers is " + str(num_1 + num_2))
# When using PyCharm, it said TypeError was not the correct error value
# And said that ValueError was, so I made it ValueError instead of TypeError
except ValueError:
    print("Please make sure to enter numbers")

