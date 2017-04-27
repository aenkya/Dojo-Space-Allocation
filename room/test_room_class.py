"""
Unit tests for the Room Class
"""
import unittest
from dojo.dojo import Dojo
from room.room import Room


class RoomClassTest(unittest.TestCase):
    """Testing Room Class"""

    def setUp(self):
        self.name = 'Orange'
        self.room = Room(self.name)

    def test_room_instance(self):
        self.assertIsInstance(
            self.room, Room, msg='The object should be an instance of the `Room` class')

    def test_room_initializes_with_default_capacity_four(self):
        self.assertEqual(self.room.capacity, 4)

    def test_room_initializes_with_no_room_mates(self):
        self.assertEqual(len(self.room.room_mates), 0)

    def test_room_name_is_same_as_given_name(self):
        self.assertTrue(self.name is self.room.name)
