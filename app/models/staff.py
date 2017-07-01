from app.models.person import Person


class Staff(Person):
    """Staff class"""

    def __init__(self, name, gender, age, nationality):
        super(Staff, self).__init__(name, gender, age, nationality)
