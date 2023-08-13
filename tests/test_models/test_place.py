#!/usr/bin/python3
""" Tests the place model """


import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Tests the Place object """
    def setUp(self):
        """ Sets up the tests """
        self.place = Place()

    def tearDown(self):
        """ Tears down the tests """
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_place_attributes(self):
        """ Tests if place has the required attributes """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_city_id_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.city_id, "")

    def test_place_user_id_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.user_id, "")

    def test_place_name_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.name, "")

    def test_place_description_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.description, "")

    def test_place_number_rooms_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.number_rooms, 0)

    def test_place_number_bathrooms_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_place_max_guest_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.max_guest, 0)

    def test_place_price_by_night_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.price_by_night, 0)

    def test_place_latitude_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.latitude, 0.0)

    def test_place_longitude_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.longitude, 0.0)

    def test_place_amenity_id_default_value(self):
        """ Tests the default value """
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_city_id_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.city_id, str)

    def test_place_user_id_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.user_id, str)

    def test_place_name_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.name, str)

    def test_place_description_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.description, str)

    def test_place_number_rooms_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_place_number_bathrooms_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_place_max_guest_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.max_guest, int)

    def test_place_price_by_night_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_place_latitude_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.latitude, float)

    def test_place_longitude_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.longitude, float)

    def test_place_amenity_ids_type(self):
        """ Tests the city id type """
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
