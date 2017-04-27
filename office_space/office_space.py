from room.room import Room


class office_space(Room):
    """office space class"""

    def __init__(self, name):
        super(office_space, self).__init__(name)
        self.populate_slots()

    def populate_slots(self):
        for i in range(0, self.capacity):
            self.room_mates.append('X')
