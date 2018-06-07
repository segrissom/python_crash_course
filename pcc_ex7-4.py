#This is from Python Crash Course Chapter 7, exercise 4
while True:
    topping=""
    message = "What topping would you like to add to your pizza? "
    message += "\nType 'quit' if you are done adding toppings. "
    topping = input(message)
    if topping=='quit':
        print("We'll start making your pizza immediately!")
        break
    print("We're adding " + topping + " to your pizza!")
