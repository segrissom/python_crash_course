# This is from Python Crash Course from Chapter 8, exercise 4
def make_shirt(size='large', text='I love Python'):
    message = "Your ordered a " + size + " sized shirt which says:"
    message += "\n" + text
    print(message)

# now I'm going to make a large shirt w/ the default message
make_shirt()
# now I'm going to make a medium shirt w/ the default message
make_shirt(size='medium')
# now I'm going to make a shirt of any size w/ a different message
make_shirt(size='small',text='coffee.now()')

