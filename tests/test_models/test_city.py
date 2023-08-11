#!/usr/bin/python3
""" This tests the City Model class """


import unittest
import os
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ Tests for the city model class """
    def setUp(self):
        """ Sets up the tests """
        self.city = City()

    def tearDown(self):
        """ Tears down the tests """
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_city_attributes(self):
        """ Tests for the city attributes """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_city_state_id_default_value(self):
        """ Tests the default state_id attr """
        self.assertEqual(self.city.state_id, "")
    
    def test_city_name_default_value(self):
        """ Tests the default name attr """
        self.assertEqual(self.city.name, "")

    def test_city_state_id_type(self):
        """ Tests the type of the state_id attr """
        self.assertIsInstance(self.city.state_id, str)

    def test_city_name_type(self):
        """ Tests the type of the name attr """
        self.assertIsInstance(self.city.name, str)

if __name__ == "__main__":
    unittest.main()
