#!/usr/bin/python3
"""Testing Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """Testing Amenity Class"""
    def test_amenity_attributes(self):
        """Testing Amenity Attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_amenity_inherits_from_base_model(self):
        """Testing Amenity Inheritance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
