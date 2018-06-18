# This is from Python Crash Course Chapter 10, exercise 8
# In this one you are to create txt files, which I saved in the same folder to make it easier

filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    try:
        with open(file, 'r') as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print("The file " + file + " does not seem to be where you thought it was!")
