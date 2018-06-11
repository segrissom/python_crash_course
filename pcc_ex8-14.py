# This is from Python Crash Course from Chapter 8, exercise 14


def make_car(make, model, **car_info):
    car = {}
    car['make']= make
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

