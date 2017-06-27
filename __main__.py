"""
Dojo Space Allocation

Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <person_name> <person_type> [wants_accomodation]
    dojo print_room <room_name>
    dojo print_allocations [-o=filename]
    dojo print_unallocated [-o=filename]
    dojo reallocate_person <person_identifier> <new_room_name>
    dojo save_state [--db=sqlite_database]
    dojo -h | --help
    dojo --version
    dojo close

Arguments:
    FELLOW|STAFF           Type of person to create/employ
    wants_accommodation    Specify if person(only fellow) wants living space

Options:
    -h, --help  Use with a command to show the command's help messsage
    --version  Show version
    --close -c   Close the program

Examples
    dojo create_room Office LLK
"""

import os
import cmd
from docopt import docopt, DocoptExit
from app.models.dojo import Dojo

dojo = Dojo('DOJO01', 'The Dojo')


def get_docopt_args(func):
    """
    Decorator to pass the results of the docscript command to the function
    """

    def func_wrapper(self, arg):
        try:
            opt = docopt(func_wrapper.__doc__, arg)
        except DocoptExit as e:
            return
        except SystemExit:
            return

        return func(opt)
    func_wrapper.__name__ = func.__name__
    func_wrapper.__doc__ = func.__doc__
    func_wrapper.__dict__.update(func.__dict__)
    return func_wrapper


class SpaceAllocation(cmd.Cmd):
    """
    Main Application Entry Point
    Type help to get a list of usage commands
    """
    os.system('cls')
    print("\nWelcome to the Dojo Space Allocation Program")
    print("______________________________________________")
    print('\nLocation Name: ' + dojo.name + '\n')

    prompt = 'SpaceAlloc:  '  # prompt to replace default cmd prompt message

    @get_docopt_args
    def do_create_room(params):
        """ Usage: create_room <room_type> <room_name>..."""
        return dojo.create_room(params["<room_type>"], params["<room_name>"])

    @get_docopt_args
    def do_add_person(params):
        """ Usage: add_person <person_name> <person_type> [<wants_accomodation>]"""
        wants_accomodation = params["<wants_accomodation>"]
        if wants_accomodation == 'Y':
            wants_accomodation = True
        else:
            wants_accomodation = False
        return dojo.add_person(params["<person_name>"], params["<person_type>"], wants_accomodation)

    @get_docopt_args
    def do_print_room(params):
        """ Usage: print_room <room_name> """
        room = params["<room_name>"]
        empty = True
        if room in dojo.living_spaces:
            spaces = dojo.living_spaces
        elif room in dojo.office_spaces:
            spaces = dojo.office_spaces
        else:
            print("Room not found")
            return

        for x in range(0, len(spaces[room].room_mates)):
            if spaces[room].room_mates[x] == 'X':
                continue
            else:
                print(spaces[room].room_mates[x])
                empty = False
        if empty is True:
            print("Empty")

    @get_docopt_args
    def do_print_allocations(params):
        """Usage: print_allocations [-o=filename] """
        return dojo.print_allocations()

    @get_docopt_args
    def do_print_unallocated(params):
        """Usage: print_unallocated [-o=filename]"""
        return dojo.print_unallocated_people()

    @get_docopt_args
    def do_reallocate_person(params):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        return dojo.reallocate_person(params["<person_identifier>"], params["<new_room_name>"])

    @get_docopt_args
    def do_load_people(params):
        """Usage: load_people """
        return dojo.load_people()

    @get_docopt_args
    def do_save_state(params):
        """Usage: save_state [--db=sqlite_database] """
        return dojo.save_state(params['--db'])

    @get_docopt_args
    def do_load_state(params):
        """load_state <sqlite_database>"""
        return dojo.load_state(params['sqlite_database'])


SpaceAllocation().cmdloop()

# Old Implementation
# if __name__ == '__main__':
#     opt = docopt(__doc__)
#     dojo = main()

#     """Usage: create_room <room_type> <room_name>..."""
#     try:
#         room_type = opt["<room_type>"]
#         room_names = opt["<room_name>"]
#         dojo.create_room(room_type, room_names)

#     except: ValueError
