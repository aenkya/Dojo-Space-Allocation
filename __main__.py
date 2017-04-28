"""
Dojo Space Allocation

Usage:
    dojo create_room <room_type> <room_name>...
    dojo add_person <person_name> <person_type> [wants_accomodation]
    dojo -h | --help
    dojo --version
    dojo close

Options:
    -h --help  Show this screen
    --version  Show version
    --close -c   Close the program

Examples
    dojo create_room Office LLK
"""

import os
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

        return func(opt)
    func_wrapper.__name__ = func.__name__
    func_wrapper.__doc__ = func.__doc__
    func_wrapper.__dict__.update(func.__dict__)
    return func_wrapper


class SpaceAllocation(cmd.Cmd):
    """Main Application Entry Point"""
    os.system('cls')
    print("\nWelcome to the Dojo Space Allocation Program")
    print("______________________________________________")
    print('\nLocation Name: ' + dojo.name + '')

    prompt = 'SpaceAlloc:  '  # prompt to replace default cmd prompt message

    @get_docopt_args
    def do_create_room(params):
        """ Usage: create_room <room_type> <room_name>..."""
        return dojo.create_room(params["<room_type>"], params["<room_name>"])

    @get_docopt_args
    def do_add_person(params):
        """ Usage: add_person <person_name> <person_type> [wants_accomodation]"""
        wants_accomodation = params["wants_accomodation"]
        if wants_accomodation == 'Y':
            wants_accomodation = True
        else:
            wants_accomodation = False
        return dojo.add_person(params["<person_name>"], params["<person_type>"], wants_accomodation)


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
