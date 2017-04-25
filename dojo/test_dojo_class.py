"""
Unit tests for the Dojo Class
"""
import unittest
from dojo import Dojo


class DojoClassTest():
    """Testing DojoClass"""

    def test_dojo_instance(self):
        dojo = Dojo()
        self.assertIsInstance(dojo, Dojo, msg='The object should be an instance of the `Dojo` class')
