from living_space.living_space import living_space
from office_space.office_space import office_space
from fellow.fellow import Fellow


class Dojo(object):
    """Dojo Class to create rooms, add them, define the room type and add people to the rooms"""

    def __init__(self, id, name):
        self.id = id
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

        self.names = ['Kenya', 'Nigeria', 'Uganda', 'Costa Rica']
        self.people = []
        self.living_spaces = []
        self.office_spaces = []

    def create_room(self, room_type, rooms):
        if isinstance(rooms, list):
            space = room_type.title()
            if (not space == 'Office') and (not space == 'Living'):
                raise ValueError("Space Type not recognized")
            for room_name in rooms:  # Loop through rooms argument for all rooms in list
                if space == 'Office':
                    import pdb
                    pdb.set_trace()
                    current_room = office_space(room_name)
                    self.office_spaces.append(current_room)
                    print("An Office Called "+ current_room.name + " has been successfully created!")
                else:
                    current_room = living_space(room_name)
                    self.living_spaces.append(current_room)
                    print("A Living Space Called "+ current_room.name + " has been successfully created!")
                return current_room
        else:
            raise ValueError('Rooms argument should be a list')


