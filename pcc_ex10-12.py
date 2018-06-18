# This is from Python Crash Course Chapter 10, exercise 12

# Based on my reading and interpretation of the question, I think
# I already solved it in the last one.
def fave_number():
    message = "Please share with me your favorite number? "
    fav_num = input(message)
    file_name = 'fave_num.txt'
    try:
        with open(file_name) as file_objects:
            json.dump(fav_num, file_objects)
    except FileExistsError:
        print("You've already created your favorite number file!")

def display_num(file_name):
    try:
        with open(file_name) as file_objects:
            content = file_objects.read()
            print("I know your favorite number, it's " + str(content) + "!")
    except FileNotFoundError:
        print("We don't seem to have your favorite number saved!")
        fave_number()

