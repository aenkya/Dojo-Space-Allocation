"""
Unit tests for the __main__.py file
"""
import unittest
from __main__ import main
from dojo.dojo import Dojo


class test_main(unittest.TestCase):
    """Testing Main Class"""

    def setUp(self):
        self.main = main()

    def test_main_instance(self):
        self.assertIsInstance(
            self.main, main, msg='The object should be an instance of the `main` class')

    def test_create_room_function_creates_rooms_for_each_room_name_provided(self):
        self.main.create_room('Office', ['Green', 'Yellow'])
        self.assertEqual(2, len(self.main.dojo.office_spaces))

    def test_create_room_function_creates_office_space_if_room_type_is_Office(self):
        self.assertIsInstance(self.main.create_room('Office', [
                              'Green']), Room, msg='The object should return an instance of office_space Class')
