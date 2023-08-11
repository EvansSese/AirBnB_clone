#!/usr/bin/python3
""" This tests the user class """


import os
import unittest
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """ Tests user class """
    def setUp(self):
        """ Setup test """
        self.user = User()

    def tearDown(self):
        """ Tear down test """
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_attributes(self):
        """ Tests if attributes are present """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_user_email_default_value(self):
        """ Tests the default value for email attr """
        self.assertEqual(self.user.email, "")
    
    def test_user_password_default_value(self):
        """ Tests the default user password attr """
        self.assertEqual(self.user.password, "")

    def test_user_first_name_default_value(self):
        """ Tests the default user first name """
        self.assertEqual(self.user.first_name, "")

    def test_user_last_name_default_value(self):
        """ Tests the default user last name """
        self.assertEqual(self.user.last_name, "")

    def test_user_email_type(self):
        """ Tests the type of user email """
        self.assertIsInstance(self.user.email, str)

    def test_user_password_type(self):
        """ Tests the type of user password """
        self.assertIsInstance(self.user.password, str)

    def test_user_first_name_type(self):
        """ Tests the type of user first name """
        self.assertIsInstance(self.user.first_name, str)

    def test_user_last_name_type(self):
        """ Tests the type of user last name """
        self.assertIsInstance(self.user.last_name, str)

if __name__ == '__main__':
    unittest.main()
