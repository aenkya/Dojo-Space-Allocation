from docopt import docopt, DocoptExit
from ..living_space import living_space


class Dojo(object):
    """Dojo Class to create rooms, add them, define the room type and add people to the rooms"""

    def __init__(self, id, name):
        self.id = id
        if isinstance(name, string):
            self.name = name
        else:
            raise TypeError("Name should be string")

        self.names = ['Kenya', 'Nigeria', 'Uganda', 'Costa Rica']

    def create_room(self, room_type, rooms):
        if isinstance(rooms, list):
            if room_type.lower() is not ('office' or 'living'):
                raise ValueError("Space Type not recognized")
            for room_name in rooms:  # Loop through rooms argument for all rooms in list
                current_room = Room(room_name)
                self.rooms.append(current_room)
            return self.rooms
        else:
            raise TypeError('Rooms argument should be a list')
