"""
Unit tests for the living_space Class
"""
import unittest
from living_space.living_space import living_space


class living_space_classTest(unittest.TestCase):
    """Testing living_space_class"""

    def setUp(self):
        self.name = 'Orange'
        self.living = living_space(self.name)

    def test_living_space_instance(self):
        self.assertIsInstance(
            self.living, living_space, msg='The object should be an instance of the `living_space` class')

    def test_living_space_initializes_with_capacity_four(self):
        self.assertEqual(self.living.capacity, 4)

    def test_living_space_initializes_with_empty_slots_x(self):
        self.assertEqual(len(self.living.room_mates), 4)