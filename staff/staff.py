from person import Person


class Staff(Person):
    """Staff class"""

    def __init__(self):
        super(Staff, self).__init__(id, name, gender, age, nationality)
        self.role = 'Staff'
