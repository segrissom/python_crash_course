# This is from Python Crash Course Chapter 11, exercise 1
# This one is about building a unit test

import unittest
from city_country_take_2 import city_country_take_2


class TestCity_Country:
    """Tests for city_country function"""

    def tests_capitalizing_names(self):
        """Do names like new york city, new york work?"""
        capitalized_names = city_country('new york city', 'new york')
        self.assertEqual(capitalized_names, 'New York City, New York')

    def tests_population(self):
        """Does it work if we put in the population?"""
        with_population = city_country_take_2('santiago', 'chile', 5000000)
        self.assertEqual(with_population, 'Santiago, Chile - population 5000000')

unittest.main
