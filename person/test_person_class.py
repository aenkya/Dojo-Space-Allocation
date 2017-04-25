"""
Unit tests for the Person Class
"""
import unittest
from dojo import Dojo
import Person


class PersonClassTest(unittest.TestCase):
    """Testing Person Class"""

    def setUp(self):
        self.dojo = Dojo()
        self.person = Person()

    def test_person_instance(self):
        self.assertIsInstance(
            self.person, Person, msg='The object should be an instance of the `Person` class')
