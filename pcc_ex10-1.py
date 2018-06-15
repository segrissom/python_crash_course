# This is from Python Crash Course Chapter 10, exercise 1
# In this, you are to first create a .txt file listing the things you know about python

# I saved my file in the same folder as this so it's simpler
file_name = 'learning_python.txt'
# This method is from just reading the whole file
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

# This method is from reading line by line and printing out
with open(file_name) as file_object:
    for line in file_object:
        print(line)

# This method is the storing the lines in a list and then working with them outside
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)
