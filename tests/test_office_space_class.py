"""
Unit tests for the office_space Class
"""
import unittest
from app.models.office_space import office_space


class office_space_classTest(unittest.TestCase):
    """Testing office_space_class"""

    def setUp(self):
        self.name = 'Orange'
        self.office = office_space(self.name)

    def test_office_space_instance(self):
        self.assertIsInstance(
            self.office, office_space, msg='The object should be an instance of the `office_space` class')

    def test_office_space_initializes_with_capacity_sixr(self):
        self.assertEqual(self.office.capacity, 6)

    def test_office_space_initializes_with_empty_slots_x(self):
        self.assertEqual(len(self.office.room_mates), 6)

    def test_office_space_name_is_same_as_given_name(self):
        self.assertTrue(self.name == self.office.name)
