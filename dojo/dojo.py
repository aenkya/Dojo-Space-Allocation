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
        self.rooms = []
        default_rooms = ['Kenya', 'Nigeria', 'Uganda', 'Costa Rica']
