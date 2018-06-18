# This is from Python Crash Course Chapter 10, exercise 7
# This exercise requests that you reuse your code from 10-6
bool_t_or_f = True
while bool_t_or_f:
    message0 = "If you wish to quit at any time, type 'q' for either answer."
    message = "Please enter a number: "
    message2 = "Please enter a second number: "
    print(message0)
    num_1 = input(message)
    num_2 = input(message2)
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        print("The sum of the numbers is " + str(num_1 + num_2))
    # When using PyCharm, it said TypeError was not the correct error value
    # And said that ValueError was, so I made it ValueError instead of TypeError
    except ValueError:
        if num_1 == 'q' or num_2 == 'q':
            bool_t_or_f = False
        else:
            print("Please make sure to enter numbers")

