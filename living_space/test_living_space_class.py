"""
Unit tests for the living_space Class
"""
import unittest
from .living_space import living_space


class living_space_classTest(unittest.TestCase):
    """Testing living_space_class"""

    def setUp(self):
        self.living_space = living_space()

    def test_living_space_instance(self):
        self.assertIsInstance(
            self.living_space, living_space, msg='The object should be an instance of the `living_space` class')

    def test_create_living_space_returns_value_error_if_arg_not_list():
        self.assertRaises(
            ValueError, self.living_space.create_living_space(), 'two')
