#!/usr/bin/python3
"""Testing Review"""
import unittest
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """Review Class Testing"""

    def test_review_attributes(self):
        """Testing Review Attributes"""
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_review_inherits_from_base_model(self):
        """Testing Review Inheritances"""
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == '__main__':
    unittest.main()
