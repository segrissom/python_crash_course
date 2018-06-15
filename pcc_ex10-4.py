# This is from Python Crash Course Chapter 10, exercise 4

file_name = 'guest_book.txt'
message = "Hello and Welcome! Please enter your name: "
message += "If you want to quit, type 'q' "
while_stop = True
while while_stop:
    guest_name = input(message)
    if guest_name == 'q':
        while_stop = False
    else:
        with open(file_name, 'w') as file_object:
            file_object.write("\n" + guest_name)
