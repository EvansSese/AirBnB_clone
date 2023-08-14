#!/bin/usr/python3
""" This is the test for state class """


import os
import unittest
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """ This class tests the state model """
    def setUp(self):
        """ Sets up the state test """
        self.state = State()

    def tearDown(self):
        """ Tears down the tests """
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_attributes(self):
        """ Tests the state class attributes """
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_name_default_value(self):
        """ Tests the default state name value """
        self.assertEqual(self.state.name, "")

    def test_state_name_type(self):
        """ Tests the name type """
        self.assertIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
