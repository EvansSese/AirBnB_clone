#!/usr/bin/python3
""" Tests the amenity class """


import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Tests the Amenity object """
    def setUp(self):
        """ Sets up the tests """
        self.amenity = Amenity()

    def tearDown(self):
        """ Tears down the tests """
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_attributes(self):
        """ Tests if the amenity attr are present """
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_name_default_value(self):
        """ Tests if amenity default value """
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name_type(self):
        """ Tests the type of name attr """
        self.assertIsInstance(self.amenity.name, str)

if __name__ == '__main__':
    unittest.main()
