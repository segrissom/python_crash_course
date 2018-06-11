# This is from Python Crash Course from Chapter 8, exercise 5


def describe_city(city_name, country_name='United States'):
    message = city_name.title() + " is in " + country_name.title() + "."
    print(message)


# Tasked to call the function three times, one of which is not in the default country
describe_city("New York City")

describe_city("Portland")

describe_city("London", "England")
