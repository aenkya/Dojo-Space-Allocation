"""
Unit tests for the staff Class
"""
import unittest
from staff import Staff


class staff_classTest(unittest.TestCase):
    """Testing staff_class"""

    def setUp(self):
        self.staff = Staff()

    def test_staff_instance(self):
        self.assertIsInstance(
            self.staff, Staff, msg='The object should be an instance of the `Staff` class')
