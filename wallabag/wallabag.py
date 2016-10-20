#!/usr/bin/env python3

import getopt
from sys import argv
from wallabag_help import show as help
import wallabag_config
import wallabag_add
import conf

PROGRAM_VERSION = "0.1.1-alpha"

command = None
need_config = False

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
elif argv[1] in ["config", "add"]:
    command = argv[1]
    need_config = command != "config"
elif argv[1][0] != '-':
    print("Error: Invalid command \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of commands.".format(argv[0]))
    exit(-1)
else:
    print("Invalid option \"{0}\".".format(argv[1]))
    print("Use \"{0}\" to see a full list of options.".format(argv[0]))
    exit(-1)

if need_config and not conf.is_valid():
    i = input(
        "Could not find a valid config. Would you like to create it now? [Y/n] ")
    if str.lower(i) in ["y", "yes", ""]:
        wallabag_config.start()
    else:
        exit(0)

if command == "config":
    optionlist = argv[2:len(argv)]
    try:
        args = getopt.getopt(optionlist, "h", ["help"])[0]
    except getopt.GetoptError as e:
        print("Error: Invalid option \"{0}\"".format(e.opt))
        print()
        exit(-1)
    for opt, arg in args:
        if opt in ('-h', '--help'):
            help(argv[0], command)
            exit(0)
    wallabag_config.start()

if command == "add":
    if "-h" in argv[2:len(argv)] or "--help" in argv[2:len(argv)]:
        help(argv[0], command)
        exit(0)

    if len(argv) < 3:
        print("Error: Missing URL to add")
        print()
        exit(-1)

    optionlist = argv[2:len(argv) - 1]
    url = argv[len(argv) - 1]
    title = None
    star = False
    read = False

    try:
        args = getopt.getopt(optionlist, "ht:sr", [
            "help", "title=", "starred", "read"])[0]
    except getopt.GetoptError as e:
        print("Error: Invalid option \"{0}\"".format(e.opt))
        print()
        exit(-1)
    for opt, arg in args:
        if opt in ('-t', '--title'):
            title = arg
        if opt in ('-s', '--starred'):
            star = True
        if opt in ('-r', '--read'):
            read = True
    wallabag_add.add(url, title, star, read)
