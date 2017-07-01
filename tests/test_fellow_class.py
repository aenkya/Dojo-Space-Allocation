"""
Unit tests for the Fellow Class
"""
import unittest
from app.models.fellow import Fellow


class FellowClassTest(unittest.TestCase):
    """Testing Fellow Class"""

    def setUp(self):
        self.name = 'Bruce'
        self.nationality = 'Ugandan'
        self.age = 35
        self.gender = 'Male'
        self.fellow = Fellow(self.name, self.gender,
                             self.age, self.nationality)

    def test_fellow_instance(self):
        self.assertIsInstance(
            self.fellow, Fellow, msg='The object should be an instance of the `Fellow` class')

    def test_fellow_name_is_same_as_given_name(self):
        self.assertTrue(self.name is self.fellow.name)
