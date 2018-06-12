# This is my answer from Python Crash Course, Chapter 9 exercise 1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()


    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")


    def open_restaurant(self):
        print(self.restaurant_name + " is open!")


new_restaurant = Restaurant('Aegan', 'Mediterranean')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
