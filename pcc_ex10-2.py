# This is from Python Crash Course chapter 10, exercise 2

file_name = 'learning_python.txt'
with open(file_name) as file_objects:
    for line in file_objects:
        message = line.replace('Python', 'C')
        print(message)