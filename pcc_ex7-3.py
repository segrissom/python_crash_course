#This is from Python Crash Course Chapter 7, exercise 3
message = "Please input a number: "
number = input(message)
#Have to convert to an int
number = int(number)
#Now I have to check that it is a multiple of ten
if number % 10 ==0:
    print(str(number)+ " is a multiple of ten.")
else:
    print(str(number) + " is not a multiple of ten.")
    