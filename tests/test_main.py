"""
Unit tests for the __main__.py file
"""
import unittest
from models.dojo import Dojo
from models.room import Room
from models.living_space import living_space
from models.office_space import office_space


class test_main(unittest.TestCase):
    """Testing Main Class"""

    def setUp(self):
        self.dojo = Dojo('DOJO001', 'The Dojo')
