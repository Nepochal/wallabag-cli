"""
Module for deleting existing entries
"""
import api
import conf
from sys import exit

def delete(entry_id, force=False):
    conf.load()

    try:
        request = api.api_delete_entry(entry_id)
        if(request.hasError()):
            if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
                print("Error: Invalid entry id.")
                exit(-1)
            print("Error: {0} - {1}".format(request.error_text,
                                            request.error_description))
            exit(-1)
        else:
            print("Entry successfully deleted.")
            exit(0)
    except api.OAuthException as e:
        print("Error: {0}".format(e.text))
        print()
        exit(-1)
