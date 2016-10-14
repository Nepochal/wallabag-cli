#!/usr/bin/env python3

from sys import argv
from wallabag_help import show as help

command = None
show_help = False

# Determine command or general standalone option
if len(argv) == 1 or argv[1] in {'-h', '--help'}:
    help(argv[0])
    exit(0)
elif not argv[1][0] == '-':
    print("Invalid command \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of commands.".format(argv[0]))
    exit(-1)
else:
    print("Invalid option \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of options.".format(argv[0]))
    exit(-1)
