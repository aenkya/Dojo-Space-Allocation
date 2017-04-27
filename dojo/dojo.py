from living_space.living_space import living_space
from office_space.office_space import office_space
from fellow.fellow import Fellow


class Dojo(object):
    """Dojo Class to create rooms, add them, define the room type and add people to the rooms"""

    def __init__(self, id, name):
        self.id = id
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

        self.fellows = {}
        self.staff = {}
        self.living_spaces = {}
        self.office_spaces = {}
        self.available_living_slots = {}
        self.available_office_slots = {}

    def create_room(self, room_type, rooms):
        if isinstance(rooms, list):
            space = room_type.title()
            if (not space == 'Office') and (not space == 'Living'):
                raise ValueError("Space Type not recognized")
            for room_name in rooms:  # Loop through rooms argument for all rooms in list
                if space == 'Office':
                    if self.check_if_room_exists(room_name, space) is True:
                        print("Room with name " +
                              room_name + " Already Exists!")
                        continue
                    else:
                        current_room = office_space(room_name)
                        self.office_spaces[room_name] = current_room
                        print("An Office Called " + current_room.name +
                              " has been successfully created!")
                else:
                    if self.check_if_room_exists(room_name, space) is True:
                        print("Room with name " +
                              room_name + " Already Exists!")
                        continue
                    else:
                        current_room = living_space(room_name)
                        self.living_spaces[room_name] = current_room
                        print("A Living Space Called " + current_room.name +
                              " has been successfully created!")
        else:
            raise ValueError('Rooms argument should be a list')

    def add_person(self, person_name, person_type, wants_accomodation):
        """Function to add person to dojo and allocate room"""
        id = person_name  # pick the name as the id
        gender = 'Male'  # TODO: Configure gender argument
        nationality = 'Ugandan'  # TODO: Configure gender
        living_space_bool = False  # living space option
        age = 25

        person_type = person_type.title()

        if not ((person_type == 'Fellow') or (person_type == 'Staff')):
            import pdb
            pdb.set_trace()
        else:
            if self.check_if_person_exists(person_name, person_type) is True:
                print("Person Exists!")
                return
            else:
                fellow = Fellow(person_name, gender, age, nationality)
                self.fellows[person_name] = fellow
                print(person_name + ' has been successfully added')
                self.add_to_room(person_name)

    def check_if_person_exists(self, person, person_type):
        """Function to check if user has already been added"""
        if person_type == 'Fellow':
            if person in self.fellows:
                print(self.fellows)
                return True
            else:
                return False
        elif person_type == 'Staff':
            if person in self.staff:
                return True
            else:
                return False
        else:
            return False

    def check_if_room_exists(self, room, room_type):
        """Function to check if user has already been added"""
        if room_type == 'Living':
            if room in self.living_spaces:
                return True
            else:
                return False
        elif room_type == 'Office':
            if room in self.office_spaces:
                return True
            else:
                return False
        else:
            return False

    def add_to_room(self, person):
        self.find_empty_slots('office_space')
        # for i in self.office_spaces:
        #     print (self.office_spaces[i].name)
        # if isinstance(self.fellows[person], Fellow):

    def find_empty_slots(self, room_type):
        if room_type == 'living_space':
            for i in self.living_spaces:
                for n in range(0, len(self.living_spaces[i].room_mates)):
                    if self.living_spaces[i].room_mates[n] == 'X':
                        if self.living_spaces[i].name in self.available_living_slots:
                            self.available_living_slots[
                                self.living_spaces[i].name] += 1
                        else:
                            self.available_living_slots[
                                self.living_spaces[i].name] = 1
        if room_type == 'office_space':
            for i in self.office_spaces:
                for n in range(0, len(self.office_spaces[i].room_mates)):
                    if self.office_spaces[i].room_mates[n] == 'X':
                        if self.office_spaces[i].name in self.available_office_slots:
                            self.available_office_slots[
                                self.office_spaces[i].name] += 1
                        else:
                            self.available_office_slots[
                                self.office_spaces[i].name] = 1

    def show_available_room(self, room_name, room_type):
        if room_type == 'living_space':
            print(self.living_spaces.find('room_name'))
