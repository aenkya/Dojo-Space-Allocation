"""
Dojo Space Allocation

Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <person_name> <FELLOW|STAFF> [wants_accomodation]
    dojo -h | --help
    dojo --version

Options:
    -h --help  Show this screen
    --version  Show version

Examples
    dojo create_room Office LLK
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo.dojo import Dojo

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

        return func(self, opt)
    func_wrapper.__doc__ = func.__doc__
    return func_wrapper


class SpaceAllocation(cmd.Cmd):
    """Main Application Entry Point"""
    print("\nWelcome to the Dojo Space Allocation Program")
    print("______________________________________________")
    print('\nLocation Name: ' + dojo.name + '')

    prompt = 'SpaceAlloc:  '  # prompt to replace default cmd prompt message

    @get_docopt_args
    def do_create_room(self, params):
        """ Usage: create_room <room_type> <room_name>..."""

        return dojo.create_room(params["<room_type>"], params["<room_name>"])

    # def add_person(self, person_name, person_type, wants_accomodation):
    # return self.dojo.add_person(str(person_name), person_type,
    # wants_accomodation)


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
