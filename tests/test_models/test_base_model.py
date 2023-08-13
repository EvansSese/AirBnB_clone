#!/usr/bin/python3
""" This is the test for BaseModel class """


import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class Test_BaseModel(unittest.TestCase):
    """ Define test for Base Model """
    def setUp(self):
        """ This is the setup method """
        self.base_model = BaseModel()

    def tearDown(self):
        """ Tears down the test instance """
        del self.base_model
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

    def test_str_rep(self):
        """ Tests the str representation """
        exp_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                               self.base_model.__dict__)
        self.assertEqual(str(self.base_model), exp_str)

    def test_save_updates_updated_at(self):
        """ Tests the update method """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """ Tests the to_dict method """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], "BaseModel")
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
