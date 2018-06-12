# This is from Python Crash Course Chapter 9, exercise 3

class Users:
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.birth_date = str(birth_date)
        self.gender = gender.lower()

    def describe_user(self):
        message = self.first_name + "'s birthday is " + self.birth_date + "."
        if self.gender == 'woman' or self.gender == 'girl' or self.gender=='female':
            message += "Her last name is " + self.last_name + "."
        elif self.gender == 'man'  or self.gender =='boy' or self.gender == 'male':
            message += "His last name is " + self.last_name + "."
        else:
            message += "Their last name is " + self.last_name + "."


    def greet_user(self):
        print("Welcome back, " + self.first_name + "!")


