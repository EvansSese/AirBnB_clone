#!/usr/bin/python3
""" Tests the console """


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests the console """
    def setUp(self):
        """Sets up the tests """
        self.console = HBNBCommand()

    def tearDown(self):
        """Tears down the tests"""
        pass

    def test_quit_command(self):
        """ Test quit command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual("", f.getvalue().strip())

    def test_create_command(self):
        """ Tests create command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("-", f.getvalue())

    def test_show_command(self):
        """ Tests show command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_all_command(self):
        """ Tests all command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn("[BaseModel]", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
