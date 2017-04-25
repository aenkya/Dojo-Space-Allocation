"""
Unit tests for the Room Class
"""
import unittest
from dojo import Dojo
import Room


class RoomClassTest():
    """Testing Room Class"""

    def test_room_instance(self):
        dojo = Dojo()
        room = dojo.create_room()
        self.assertIsInstance(
            room, Room, msg='The object should be an instance of the `Room` class')
