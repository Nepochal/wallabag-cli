"""
List existing entries
"""
import api
import conf
import entry
import json
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

    if len(entries) > 0:
        size_entry_id = len(str(entries[0].entry_id))

    for item in entries:
        entry_id = str(item.entry_id).rjust(size_entry_id)
        title = item.title

        line = "{0} {1}".format(entry_id, title)
        print(line)

list_entries()
