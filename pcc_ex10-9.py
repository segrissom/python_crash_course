# This is from Python Crash Course Chapter 10, exercise 9
# This exercise requires you to modify the text from 10-8

filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    try:
        with open(file, 'r') as file_object:
            print(file_object.read())
    except FileNotFoundError:
        # print("The file " + file + " does not seem to be where you thought it was!")
        # This time wants you to silently fail by using pass
        pass
