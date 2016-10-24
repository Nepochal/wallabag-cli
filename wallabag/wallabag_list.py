"""
List existing entries
"""
import api
import conf
import entry
import json
import os
from sys import exit


def list_entries():
    conf.load()

    try:
        request = api.api_list_entries()
        if(request.hasError()):
            print("Error: {0} - {1}".format(request.error_text,
                                            request.error_description))
            exit(-1)
        response = json.loads(request.response)
    except api.OAuthException as e:
        print("Error: {0}".format(e.text))
        print()
        exit(-1)

    entries = entry.entrylist(response['_embedded']["items"])
    print_entries(entries)


def print_entries(entries):

    title_maxlength = os.get_terminal_size().columns
    size_entry_id = 0
    show_read_column = False
    show_starred_column = False

    if len(entries) > 0:
        size_entry_id = len(str(entries[0].entry_id))

    for item in entries:
        if(item.read):
            show_read_column = True
        if(item.starred):
            show_starred_column = True

    for item in entries:
        entry_id = str(item.entry_id).rjust(size_entry_id)

        read = " "
        if item.read:
            read = "✔"

        starred = " "
        if item.starred:
            starred = "*"

        title = item.title

        line = entry_id
        if show_read_column or show_starred_column:
            line = line + " "
            if show_read_column:
                line = line + read
            if show_starred_column:
                line = line + starred

        title = title[0:title_maxlength - len(line) - 1]
        line = line + " {0}".format(title)
        print(line)

list_entries()
