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
from docopt import docopt, DocoptExit
from dojo.dojo import Dojo


class main(object):
    """Main Application Entry Point"""

    def __init__(self):
        print("\nWelcome to the Dojo Space Allocation Program")
        print("______________________________________________")
        self.dojo = Dojo('DOJO01', 'The Dojo')
        print('\nLocation Name: ' + self.dojo.name + '')

    def create_room(self, room_type, room_names):
        print (self.dojo.create_room(str(room_type), room_names))


if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:])
    dojo = main()

    """Usage: create_room <room_type> <room_name>..."""
    dojo.create_room(sys.argv[2], sys.argv[3:])