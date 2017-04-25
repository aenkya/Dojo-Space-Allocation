from room.room import Room


class living_space(Room):
    """living space class"""

    def __init__(self):
        super(living_space, self).__init__(id, name)
        self.capacity = 4
