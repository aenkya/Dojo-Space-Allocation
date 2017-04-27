import random
import os
from living_space.living_space import living_space
from office_space.office_space import office_space
from fellow.fellow import Fellow
from staff.staff import Staff


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
        self.allocated_spots = {}
        self.root_dir = os.path.dirname(os.path.abspath(__file__))

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
        gender = 'Male'  # TODO: Configure gender argument
        nationality = 'Ugandan'  # TODO: Configure gender
        age = 25  # TODO: Configure Gender
        person_type = person_type.title()

        if not ((person_type == 'Fellow') or (person_type == 'Staff')):
            import pdb
            pdb.set_trace()
        else:
            if self.check_if_person_exists(person_name, person_type) is True:
                print("Person Exists!")
                return
            else:
                if person_type == 'Fellow':
                    fellow = Fellow(person_name, gender, age, nationality)
                    if wants_accomodation is True:
                        fellow.request_accomodation()
                    self.fellows[person_name] = fellow
                elif person_type == 'Staff':
                    staff = Staff(person_name, gender, age, nationality)
                    self.staff[person_name] = staff
                    print(person_name + ' has been successfully added')

                self.add_to_room(person_name, person_type)
                print(self.available_living_slots)
                print(self.available_office_slots)

    def check_if_person_exists(self, person, person_type):
        """Function to check if user has already been added"""
        if person_type == 'Fellow':
            person_source = self.fellows
        elif person_type == 'Staff':
            person_source = self.staff

        if person in person_source:
            return True
        else:
            return False

    def check_if_room_exists(self, room, room_type):
        """Function to check if room has already been added"""
        if room_type == 'Living':
            space = self.living_spaces
        elif room_type == 'Office':
            space = self.office_spaces

        if room in space:
            return True
        else:
            return False

    def add_to_room(self, person, person_type):
        allocated = False
        person_source = []
        if person_type == 'Fellow':
            if self.fellows[person].wants_accomodation is True:
                living_allocated = False
                self.find_empty_slots('Living')
                while (living_allocated is False) and len(self.available_living_slots) > 0:
                    random_value = random.choice(
                        list(self.available_living_slots))
                    if self.available_living_slots[random_value] == 0:
                        del self.available_living_slots[random_value]
                        continue
                    else:
                        for i in range(0, len(self.living_spaces[random_value].room_mates)):
                            if 'X' == self.living_spaces[random_value].room_mates[i]:
                                self.living_spaces[
                                    random_value].room_mates[i] = person
                                self.available_living_slots[random_value] -= 1
                                break
                        print(person + ' has been allocated the living space ' +
                              self.living_spaces[random_value].name)
                        living_allocated = True
            person_source = self.fellows
        else:
            person_source = self.staff

        self.find_empty_slots('Office')
        while (allocated is False) and len(self.available_office_slots) > 0:
            random_value = random.choice(list(self.available_office_slots))
            if self.available_office_slots[random_value] == 0:
                del self.available_office_slots[random_value]
                continue
            else:
                for i in range(0, len(self.office_spaces[random_value].room_mates)):
                    if 'X' == self.office_spaces[random_value].room_mates[i]:
                        self.office_spaces[random_value].room_mates[i] = person
                        self.available_office_slots[random_value] -= 1
                    break

                # print(self.office_spaces[random_value].room_mates)
                # self.available_office_slots[random_value] -= 1
                # for x in range(0, len(self.office_spaces[random_value].room_mates) - 1):
                #     if self.office_spaces[random_value].room_mates[x] == 'X':
                #         self.office_spaces[random_value].room_mates[
                #             x] = self.fellows[person]
                #         print(self.office_spaces[
                #               random_value].room_mates[x])
                #         break
                print(person + ' has been allocated the office space ' +
                      self.office_spaces[random_value].name)
                allocated = True
        # print(self.available_office_slots)

    def find_empty_slots(self, room_type):
        if room_type == 'Living':

            self.available_living_slots = {}
            for i in self.living_spaces:
                for n in range(0, len(self.living_spaces[i].room_mates)):
                    if self.living_spaces[i].room_mates[n] == 'X':
                        if self.living_spaces[i].name in self.available_living_slots:
                            self.available_living_slots[
                                self.living_spaces[i].name] += 1
                        else:
                            self.available_living_slots[
                                self.living_spaces[i].name] = 1
        if room_type == 'Office':
            self.available_office_slots = {}
            for i in self.office_spaces:
                for n in range(0, len(self.office_spaces[i].room_mates)):
                    if self.office_spaces[i].room_mates[n] == 'X':
                        if self.office_spaces[i].name in self.available_office_slots:
                            self.available_office_slots[
                                self.office_spaces[i].name] += 1
                        else:
                            self.available_office_slots[
                                self.office_spaces[i].name] = 1

    def find_occupied_slots(self, room_type):
        if room_type == 'Living':

            self.available_living_slots = {}
            for i in self.living_spaces:
                for n in range(0, len(self.living_spaces[i].room_mates)):
                    if self.living_spaces[i].room_mates[n] == 'X':
                        continue
                    else:
                        print(self.living_spaces[i])
        if room_type == 'Office':
            self.available_office_slots = {}
            for i in self.office_spaces:
                for n in range(0, len(self.office_spaces[i].room_mates)):
                    if self.office_spaces[i].room_mates[n] == 'X':
                        continue
                    else:
                        print(self.office_spaces[i])

    def show_available_room(self, room_name, room_type):
        if room_type == 'living_space':
            print(self.living_spaces.find('room_name'))

    def print_allocations(self):
        file_name = input("Enter file to save to: ")
        allocated_data = ''
        allocated_data += "\n\n Living Spaces \n"
        for room_name, room in self.living_spaces.items():
            allocated_data += room_name
            allocated_data += "\n------------------------\n"
            spaces = self.living_spaces
            for x in range(0, len(spaces[room_name].room_mates)):
                if spaces[room_name].room_mates[x] == 'X':
                    continue
                else:
                    allocated_data += spaces[room_name].room_mates[x] + ', '
                allocated_data += "\n\n"
        allocated_data += "\n\n Office Spaces \n"
        allocated_data += "\n------------------------\n"
        for room_name, room in self.office_spaces.items():
            allocated_data += room_name
            allocated_data += "\n------------------------\n"
            spaces = self.office_spaces
            for x in range(0, len(spaces[room_name].room_mates)):
                if spaces[room_name].room_mates[x] == 'X':
                    continue
                else:
                    allocated_data += spaces[room_name].room_mates[x] + ', '
                allocated_data += "\n\n"
        print(allocated_data)
        self.print_to_file(allocated_data, file_name)

    def print_to_file(self, allocated_data, file_name):

        backroot = " \..\ "
        folder = "files\ "
        folder.strip()

        file_path = self.root_dir + "{}".format(backroot.strip()) + \
            "{}".format(folder.strip()) + file_name
        with open(file_path, "w") as f:
            f.write(allocated_data)

    def print_unallocated_people(self):
        file_path = self.root_dir + "../files/" + filename
        # = self._generate_unallocated_print_statement()

        with open(file_path, "w") as f:
            f.write(result_string)
