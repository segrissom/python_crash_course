# This is from Python Crash Course Chapter 10, exercise 5

message = "Why do you like programming? (Type 'q' to quit)  "
file_name = "like_programming.txt"
while True:
    reason = input(message)
    if reason == 'q':
        False
    else:
        with open(file_name, 'w') as file_object:
            file_object.write(reson)
