# This is from Python Crash Course Chapter 10, exercise 10
# This one requires you to download stuff from the project gutenberg
# and determine how many times the word 'the' appears

# For this project, I am just going to write the outline
# You can modify this pretty easily but putting your own texts on in
filenames = []
the_count = []
for file in filenames:
    try:
        with open(file, 'r') as file_objects:
            contents = file_objects.read()
            words = contents.split()
            count = words.lower().count('the')
            print(file.title() + " has the word 'the' appear " + str(count) + " times.")
    except FileNotFoundError:
        pass
