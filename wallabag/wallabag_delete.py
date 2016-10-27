"""
Module for deleting existing entries
"""
import api
import conf
import entry
import json
from sys import exit


def delete(entry_id, force=False):
    conf.load()

    if not force:
        try:
            request = api.api_get_entry(entry_id)
            __handle_request_error(request)
            entr = entry.Entry(json.loads(request.response))
            print("Do you really wish to delete the following entry?")
            i = input(entr.title + " [y/N] ")
            if str.lower(i) not in ["y", "yes"]:
                exit(0)
        except api.OAuthException as e:
            print("Error: {0}".format(e.text))
            print()
            exit(-1)

    try:
        request = api.api_delete_entry(entry_id)
        __handle_request_error(request)
        print("Entry successfully deleted.")
        exit(0)
    except api.OAuthException as e:
        print("Error: {0}".format(e.text))
        print()
        exit(-1)


def __handle_request_error(request):
    if(request.hasError()):
        if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
            print("Error: Invalid entry id.")
            exit(-1)
        print("Error: {0} - {1}".format(request.error_text,
                                        request.error_description))
        exit(-1)
