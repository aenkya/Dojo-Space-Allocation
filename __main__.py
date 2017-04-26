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


def main():
    """Main Application Entry Point"""
    print("Welcome to the Dojo Space Allocation Program")
    print("--------------------XXXXXXXXX---------------")
    dojo = Dojo('DOJO-01', 'The Dojo')
    rooms = dojo.create_room('office', ['conference', 'work'])
    print(rooms)

if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:])
    main()
