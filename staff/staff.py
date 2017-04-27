from person.person import Person


class Staff(Person):
    """Staff class"""

    def __init__(self, name, gender, age, nationality):
        super(Staff, self).__init__(self, name, gender, age, nationality)
        self.role = 'Staff'
