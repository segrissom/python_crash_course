#This is from Python Crash Course Chapter 7, exercise 8
#This is the one regarding sandwich orders
sandwich_orders = ['BLT', 'Ham & Cheese', 'Tuna Salad', 'Plain Turkey', 'Meatball']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("The " + sandwich + " is ready!")
    finished_sandwiches.append(sandwich)