#!/usr/bin/python3
""" Module to test class User """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Unittest for class user """

    def test_docstring(self):
        """ Test docstring """
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_regular_working(self):
        """ Test correct working """
        new = User()
        self.assertEqual(type(new).__name__, "User")

    def test_attributes(self):
        """ Test passing kwargs """
        new = User()
        self.assertEqual(type(new).__name__, "User")
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "__class__"))

    def test_str_format(self):
        """ Test if the strting representation is correct """
        my_obj = User()
        str_format = "[User] ({}) {}".format(my_obj.id, my_obj.__dict__)
        self.assertEqual(str_format, str(my_obj))
