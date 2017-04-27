"""
Unit tests for the Person Class
"""
import unittest
from person.person import Person


class PersonClassTest(unittest.TestCase):
    """Testing Person Class"""

    def setUp(self):
        self.name = 'Bruce'
        self.nationality = 'Ugandan'
        self.age = 35
        self.gender = 'Male'
        self.person = Person(self.name, self.gender,
                             self.age, self.nationality)

    def test_person_instance(self):
        self.assertIsInstance(
            self.person, Person, msg='The object should be an instance of the `Person` class')

    def test_person_name_is_same_as_given_name(self):
        self.assertTrue(self.name is self.person.name)
