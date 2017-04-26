from room.room import Room


class living_space(Room):
    """living space class"""

    def __init__(self, name):
        super(living_space, self).__init__(name)
        self.capacity = 4
