"""
Unit tests for the Dojo Class
"""
import unittest
from dojo.dojo import Dojo


class DojoClassTest(unittest.TestCase):
    """Testing DojoClass"""

    def setUp(self):
        self.dojo = Dojo('THEDOJO', 'The Dojo')

    def test_dojo_instance(self):
        self.assertIsInstance(
            self.dojo, Dojo, msg='The object should be an instance of the `Dojo` class')

    def test_create_room_method_raises_typeerror_if_rooms_arg_not_list(self):
        self.assertRaises(TypeError, self.dojo.fellows, 'Room 1')

    def test_create_room_method_raises_valueerror_if_room_type_not_known(self):
        args = ['New Office', 'Grey']
        kwargs = {}
        self.assertRaises(ValueError, self.dojo.create_room,
                          *args, **kwargs)