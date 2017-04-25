"""
Unit tests for the Room Class
"""
import unittest
from dojo import Dojo
import Room


class RoomClassTest():
    """Testing Room Class"""

    def setUp(self):
        self.dojo = Dojo()
        self.room = Room()

    def test_room_instance(self):
        self.assertIsInstance(
            self.room, Room, msg='The object should be an instance of the `Room` class')
