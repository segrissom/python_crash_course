# This is my answer from Python Crash Course, Chapter 9 exercise 4
# This exercise asks you to reuse code from 9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")


    def open_restaurant(self):
        print(self.restaurant_name + " is open!")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, increment):
        self.number_served += increment


my_restaurant = Restaurant("Ollie's", "American Diner")
# Changing the number served the 'easy' way, but by hard coding it
print(my_restaurant.number_served)
my_restaurant.number_served += 10
print(my_restaurant.number_served)
# Changing the number by calling the method that changes it
print(my_restaurant.set_number_served(2))
# Changing the number served by incrementing it
print(my_restaurant.increment_number_served(10))

