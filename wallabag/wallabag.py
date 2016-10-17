#!/usr/bin/env python3

from sys import argv
from wallabag_help import show as help
import wallabag_config

def check_commands(command, options, allowed_options):
    for option in options:
        if not option in allowed_options:
            print("Invalid option {0} in command {1}.".format(option, command))
            print(
                "Use {0} {1} --help for a list of allowed options.".format(argv[0], command))
            print()
            return False
    return True

PROGRAM_VERSION = "0.0.0-alpha"

command = None

# Determine command or general standalone option
if len(argv) == 1 or argv[1] in {'-h', '--help'}:
    help(argv[0])
    exit(0)
elif argv[1] in {'-v', '--version'}:
    print(PROGRAM_VERSION)
    exit(0)
elif argv[1] in {'--about'}:
    print("wallabag-cli")
    print("© 2016 by Michael Scholz (https://mischolz.de)")
    print()
    print("This software is licensed under the GPLv3.")
    exit(0)
elif argv[1] == "config":
    command = "config"
elif argv[1][0] != '-':
    print("Invalid command \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of commands.".format(argv[0]))
    exit(-1)
else:
    print("Invalid option \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of options.".format(argv[0]))
    exit(-1)

optionlist = argv[2:len(argv)]

if command == "config":
    allowed_options = []
    if "-h" in optionlist or "--help" in optionlist:
        help(argv[0], command)
        exit(0)
    if not check_commands(command, optionlist, allowed_options):
        exit(-1)
    wallabag_config.start()
