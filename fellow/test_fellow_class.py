"""
Unit tests for the fellow Class
"""
import unittest
from fellow.fellow import Fellow


class fellow_classTest(unittest.TestCase):
    """Testing fellow_class"""

    def setUp(self):
        self.fellow = Fellow()

    def test_fellow_instance(self):
        self.assertIsInstance(
            self.fellow, Fellow, msg='The object should be an instance of the `Fellow` class')
