from room.room import Room


class living_space(Room):
    """living space class"""

    def __init__(self, name):
        super(living_space, self).__init__(name)
        self.capacity = 4
        self.populate_slots()

    def populate_slots(self):
        for i in range(0, self.capacity):
            self.room_mates.append('X')
