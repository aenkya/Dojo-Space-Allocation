"""
Unit tests for the Person Class
"""
import unittest
from dojo import Dojo
import Person


class PersonClassTest():
    """Testing Person Class"""

    def test_person_instance(self):
        person = Person()
        self.assertIsInstance(
            person, Person, msg='The object should be an instance of the `Person` class')
