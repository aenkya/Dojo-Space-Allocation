"""
Unit tests for the office_space Class
"""
import unittest
from office_space import office_space


class office_space_classTest(unittest.TestCase):
    """Testing office_space_class"""

    def setUp(self):
        self.office_space = office_space()

    def test_office_space_instance(self):
        self.assertIsInstance(
            self.office_space, office_space, msg='The object should be an instance of the `office_space` class')
