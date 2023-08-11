#!/usr/bin/python3
""" Tests the file storage """


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class Test_FileStorage(unittest.TestCase):
    """ Tests the file storage """
    def setUp(self):
        """ Sets up the tests """
        self.file_storage = FileStorage()

    def tearDown(self):
        """ Tears down the tests """
        del self.file_storage
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """ Tests the method all() """
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """ Tests the method new() """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        exp = "BaseModel.{}".format(base_model.id)
        self.assertTrue(exp in self.file_storage.all())

    def test_save_method(self):
        """ Tests the method save() """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        with open("file.json", "r") as file:
            file_data = file.read()
            self.assertIn("BaseModel.{}".format(base_model.id), file_data)

    def test_reload_method(self):
        """ Tests the method reload """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        exp = "BaseModel.{}".format(base_model.id)
        self.assertIn(exp, new_file_storage.all())


if __name__ == '__main__':
    unittest.main()
