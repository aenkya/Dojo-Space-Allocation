from room.room import Room


class office_space(Room):
    """office space class"""

    def __init__(self):
        super(office_space, self).__init__()
        self.capacity = 6
