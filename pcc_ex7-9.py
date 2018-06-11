#This is from Python Crash Course from Chapter 7, exercise 9
sandwich_orders = ['BLT', 'pastrami', 'pastrami', 'Ham & Cheese', 'Tuna Salad', 'pastrami', 'Plain Turkey', 'Meatball']
print("Unfortunately, the deli has run out of pastrami - and so you will need to order something else.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("The " + sandwich + " is ready!")
    finished_sandwiches.append(sandwich)