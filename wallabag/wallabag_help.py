"""
This is the internal help system of wallabag-cli.
"""


def show(startscript, command="main"):
    if command == "":
        command = "main"

    index = dict()

    # General help
    main_txt = """
Usage:
  {0} <command> [options]

Commands:
  config      Start the configuration.

General Options:
  -h, --help  Show help.

Use \"{0} <command> --help\" for further information.
And don't forget to be excellent to each other!
""".format(startscript)
    index['main'] = main_txt

    if not command in index:
        print("Error: Invalid command \"{0}\"!".format(command))
        command = "main"

    print(index[command])
