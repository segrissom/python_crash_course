# This is from Python Crash Course Chapter 11, exercise 1
# This one is about building a unit test

import unittest
from city_country import city_country


class TestCity_Country:
    """Tests for city_country function"""

    def tests_capitalizing_names(self):
        """Do names like new york city, new york work?"""
        capitalized_names = city_country('new york city', 'new york')
        self.assertEqual(capitalized_names, 'New York City, New York')


unittest.main
