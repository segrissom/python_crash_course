# This is from Python Crash Course from Chapter 8, exercise 12


def sandwich_maker(*toppings):
    print("The sandwich you are ordering has the following item(s) in it:")
    for topping in toppings:
        print("\n\t- " +topping)


sandwich_maker("Ham", "Swiss")
sandwich_maker("Turkey", "avocado", "lettuce", "tomato")
sandwich_maker("Bacon")
