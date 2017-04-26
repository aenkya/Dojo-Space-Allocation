from docopt import docopt, DocoptExit
from ..living_space.living_space import living_space
from ..office_space.office_space import office_space


class Dojo(object):
    """Dojo Class to create rooms, add them, define the room type and add people to the rooms"""

    def __init__(self, id, name):
        self.id = id
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

        self.names = ['Kenya', 'Nigeria', 'Uganda', 'Costa Rica']

    def create_room(self, room_type, rooms):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg["<room_type>"]
        room_name = arg["<room_name>..."]
        rooms = room_name.split()
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
            raise ValueError('Rooms argument should be a list')
