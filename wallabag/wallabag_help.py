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
  config         Start the configuration.
  add            Add a new entry to wallabag.
  list           List the entries on the wallabag account.

General Options:
  -h, --help     Show help.
  --about        Show about information.
  -v, --version  Show version No.

Use \"{0} <command> --help\" for further information.
And don't forget to be excellent to each other!
""".format(startscript)
    index['main'] = main_txt

    # config
    config_txt = """
Usage:
  {0} config [options]

Description:
  Start the configuration.

Options:
  -h, --help      Show help
  -c, --check     Check the config for errors
  -p, --password  Change the wallabag password
  -o, --oauth     Change the wallabag client credentials
""".format(startscript)
    index['config'] = config_txt

    # add
    add_txt = """
Usage:
  {0} add [options] <url>

Description:
  Add a new link to wallabag.

Options:
  -h, --help           Show help
  -t, --title <title>  Add a custom title
  -s, --starred        Mark as starred
  -r, --read           Mark as read
""".format(startscript)
    index['add'] = add_txt

    # list
    list_txt = """
Usage:
  {0} list [options]

Description:
  Gives a summary of entries in wallabag. Use options to filter the results.

Options:
  -h, --help                  Show help
  -c, --count <"all"|number>  Set the number of entries to show
  --unread                    Show only unread entries (default)
  -r, --read                  Show only read entries
  -a, --all                   Show read as well as unread entries
  -s, --starred               Show only starred entries
  -u, --unstarred             Show only unstarred entries
""".format(startscript)
    index['list'] = list_txt

    if not command in index:
        print("Error: Invalid command \"{0}\"!".format(command))
        command = "main"

    print(index[command])
