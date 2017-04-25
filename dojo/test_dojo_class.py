"""
Unit tests for the Dojo Class
"""
import unittest
from dojo import Dojo


class DojoClassTest(unittest.TestCase):
    """Testing DojoClass"""

    def setUp(self):
        self.dojo = Dojo()

    def test_dojo_instance(self):
        self.assertIsInstance(
            self.dojo, Dojo, msg='The object should be an instance of the `Dojo` class')
