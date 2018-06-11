# This is from Python Crash Course from Chapter 8, exercise 6


def city_country(city_name, country_name):
    message = city_name.title() + ", " + country_name.title()
    return message


# Calling the function three times
city_country("Kyoto", "Japan")

city_country("New York City", "New York")

city_country("New Haven", "Connecticut")
