from person import Person


class Fellow(Person):
    """Fellow class"""

    def __init__(self):
        super(Fellow, self).__init__(id, name, gender, age, nationality)
        self.role = 'Fellow'
