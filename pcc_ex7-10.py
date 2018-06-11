#This is Python Crash Course Chapter 7, exercise 10
statement = True
responses = {}
while statement:
    name = input("\nWhat is your name? ")
    answer = input("\nIf you could visit one place in the world, where would you go?" )

#storing the data in the dictionary

    responses[name] = answer

#now we need to make sure that the thing doesn't go on for forever
    stop_or_no = input("Is there anyone else who is going to answer this poll? Yes or No. ")
    if stop_or_no == "No":
        statement = False

for name, response in responses.items():
    print(name.upper + " would like to visit " + response.upper() + ".")
