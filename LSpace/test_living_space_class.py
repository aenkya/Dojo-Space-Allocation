"""
Unit tests for the living_space Class
"""
import unittest
from LSpace import living_space


class LivingSpaceClassTest(unittest.TestCase):
    """Testing LivingSpaceClass"""

    def setUp(self):
        self.living_space = living_space()

    def test_living_space_instance(self):
        self.assertIsInstance(
            self.living_space, living_space, msg='The object should be an instance of the `living_space` class')

    def test_create_living_space_returns_value_error_if_arg_not_list():
        self.assertRaises(
            ValueError, self.living_space.create_living_space(), 'two')
