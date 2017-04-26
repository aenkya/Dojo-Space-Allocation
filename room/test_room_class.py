"""
Unit tests for the Room Class
"""
import unittest
from dojo.dojo import Dojo
from room import Room


class RoomClassTest(unittest.TestCase):
    """Testing Room Class"""

    def setUp(self):
        self.dojo = Dojo()
        self.room = Room()

    def test_room_instance(self):
        self.assertIsInstance(
            self.room, Room, msg='The object should be an instance of the `Room` class')
