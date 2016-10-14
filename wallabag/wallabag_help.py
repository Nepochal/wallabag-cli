"""
This is the internal help system of wallabag-cli.
"""


def show_help(startscript, command="main"):
    if command == "":
        command = "main"

    index = dict()

    # General help
    main_txt = """
    Usage:
      {0} <command> [options]
    """.format(startscript)
    index['main'] = main_txt

    print(index[command])
