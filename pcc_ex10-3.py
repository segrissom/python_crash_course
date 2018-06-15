# This is from Python Crash Course Chapter 10, exercise 3

message = "Please tell my your name. "
guest_name = input(message)

with open('guest.txt', 'w') as file_object:
    file_object.write(guest_name)
