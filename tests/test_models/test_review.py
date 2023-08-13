#!/usr/bin/python3
""" Tests the review model class """


import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Tests the review model class """
    def setUp(self):
        """ Sets up the tests """
        self.review = Review()

    def tearDown(self):
        """ Tears down the tests """
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_review_attributes(self):
        """ Tests the review attributes """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_place_id_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.review.place_id, "")

    def test_review_user_id_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.review.user_id, "")

    def test_review_text_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.review.text, "")

    def test_review_place_id_type(self):
        """ Tests the type """
        self.assertIsInstance(self.review.place_id, str)

    def test_review_user_id_type(self):
        """ Tests the type """
        self.assertIsInstance(self.review.user_id, str)

    def test_review_text_type(self):
        """ Tests the type """
        self.assertIsInstance(self.review.text, str)


if __name__ == "__main__":
    unittest.main()
