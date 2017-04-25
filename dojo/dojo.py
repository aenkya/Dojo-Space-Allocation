from docopt import docopt, DocoptExit
from ..living_space.living_space import living_space
from ..office_space.office_space import office_space


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
            space = room_type.title()
            if space is not ('Office' or 'Living'):
                raise ValueError("Space Type not recognized")
            for room_name in rooms:  # Loop through rooms argument for all rooms in list
                if space is 'Office':
                    current_room = office_space(room_name, room_name)
                else:
                    current_room = living_space(room_name, room_name)
                self.rooms.append(current_room)
            return self.rooms
        else:
            raise TypeError('Rooms argument should be a list')
