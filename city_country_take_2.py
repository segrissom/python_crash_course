# This is from Python Crash Course Chapter 11, exercise 2


def city_country_take_2(city_name, country_name, population=''):
    """This is just like the previous exercise, with a new addition of population"""
    if population:
        message = city_name.title() + ", " + country_name.title() + " - population " + str(population)
    else:
        message = city_name.title() + ", " + country_name.title()
    return message

