#!/usr/bin/python3
""" This is the test for BaseModel class """


import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class Test_BaseModel(unittest.TestCase):
    """ Define test for Base Model """
    base_model = BaseModel()

    def setup(self):
        """ This is the setup method """
        pass

    def tearDown(self):
        """ Tears down the test instance """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_attributes(self):
        """ Tests if attributes are in the instance """
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_is_string(self):
        """ Tests if id is a string """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """ Test if created_at is datetime """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """ Tests if updated_at is datetime """
        self.assertIsInstance(self.base_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
