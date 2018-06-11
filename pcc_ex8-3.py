# This is from Python Crash Course from Chapter 8, exercise 3
def make_shirt(size, text):
    message = "Your ordered a " + size + " sized shirt which says:"
    message += "\n" + text
    print(message)


# Calling it using the positional arguments
make_shirt('large', 'coffee.now()')

# Calling it using the keyword arguments
make_shirt(text='coffee.now()', size='large')