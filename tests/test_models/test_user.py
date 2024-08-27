#!/usr/bin/python3
"""Defining User Testing"""
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Testing UserModel"""

    def test_user_attributes(self):
        """Testing User Attributes"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_inherits_from_base_model(self):
        """Testing User Inhertance"""
        user = User()
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
