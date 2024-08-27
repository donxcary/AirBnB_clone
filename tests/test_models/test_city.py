#!/usr/bin/python3
"""Unittest for City"""
import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    """Testing City Class"""
    def test_city_attributes(self):
        """Testing city Attributes"""
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_inherits_from_base_model(self):
        """Testing City Inheritance"""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == '__main__':
    unittest.main()
