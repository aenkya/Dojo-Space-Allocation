"""
Unit tests for the __main__.py file
"""
import unittest
from app.models.dojo import Dojo
from app.models.room import Room
from app.models.living_space import living_space
from app.models.office_space import office_space


class test_main(unittest.TestCase):
    """Testing Main Class"""

    def setUp(self):
        self.dojo = Dojo('DOJO001', 'The Dojo')
