from person.person import Person


class Fellow(Person):
    """Fellow class"""

    def __init__(self, name, gender, age, nationality):
        super(Fellow, self).__init__(self, name, gender, age, nationality)
        self.role = 'Fellow'
        self.wants_accomodation = False

    def request_accomodation(self):
    	self.wants_accomodation = True
