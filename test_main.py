"""
Unit tests for the __main__.py file
"""
import unittest
from dojo.dojo import Dojo
from room.room import Room
from living_space.living_space import living_space
from office_space.office_space import office_space


class test_main(unittest.TestCase):
    """Testing Main Class"""

    def setUp(self):
        self.dojo = Dojo('DOJO001', 'The Dojo')
