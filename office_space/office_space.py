from room import Room


class office_space(Room):
    """office space class"""

    def __init__(self):
        super(office_space, self).__init__(id, name)
        self.capacity = 6
