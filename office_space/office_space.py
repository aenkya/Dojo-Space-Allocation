from room.room import Room


class office_space(Room):
    """office space class"""

    def __init__(self, name):
        super(office_space, self).__init__(name)
        self.capacity = 6
        self.name = name
