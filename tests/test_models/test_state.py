#!/usr/bin/python3
"""Unittest for State"""
import unittest
from models.state import State


class TestStateModel(unittest.TestCase):
    """Testing State CLass"""
    def test_state_attributes(self):
        """Testing State Attttributes"""
        state = State()
        self.assertEqual(state.name, '')

    def test_state_inherits_from_base_model(self):
        """Testing State Inheritance"""
        state = State()
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
