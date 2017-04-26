"""
Unit tests for the __main__.py file
"""
import unittest
from __main__ import main


class test_main(unittest.TestCase):
    """Testing Main Class"""

    def setUp(self):
        self.main = main()

    def test_main_instance(self):
        self.assertIsInstance(
            self.main, main, msg='The object should be an instance of the `main` class')
