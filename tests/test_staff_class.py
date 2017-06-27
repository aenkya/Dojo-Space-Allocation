"""
Unit tests for the Staff Class
"""
import unittest
from app.models.staff import Staff


class StaffClassTest(unittest.TestCase):
    """Testing Staff Class"""

    def setUp(self):
        self.name = 'Bruce'
        self.nationality = 'Ugandan'
        self.age = 35
        self.gender = 'Male'
        self.staff = Staff(self.name, self.gender, self.age, self.nationality)

    def test_staff_instance(self):
        self.assertIsInstance(
            self.staff, Staff, msg='The object should be an instance of the `Staff` class')

    def test_staff_name_is_same_as_given_name(self):
        self.assertTrue(self.name is self.staff.name)
