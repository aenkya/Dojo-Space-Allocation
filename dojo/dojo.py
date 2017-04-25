from docopt import docopt, DocoptExit
from room import Room


class Dojo(object):
    """Dojo Class to create rooms, add them, define the room type and add people to the rooms"""

    def __init__(self, id, name):
        self.id = id
        if isinstance(name, string):
            self.name = name
        else:
            raise TypeError("Name should be string")
        self.rooms = ['Kenya', 'Nigeria', 'Uganda', 'Costa Rica']

    def create_room(self, rooms):
        if isinstance(rooms, list):
            for room_name in rooms:  # Loop through rooms argument for all rooms in list
                current_room = Room(room_name)
                self.rooms.append(current_room)
        else:
            raise ValueError
