"""
Module for adding new entries
"""
import re
import api
import conf


def add(target_url):
    conf.load()

    valid_url = False
    if not re.compile("(?i)https?:\\/\\/.+").match(target_url):
        for protocol in "https://", "http://":
            if api.is_valid_url("{0}{1}".format(protocol, target_url)):
                target_url = "{0}{1}".format(protocol, target_url)
                valid_url = True
                break
    else:
        valid_url = api.is_valid_url(target_url)

    if not valid_url:
        print("Error: Invalid url to add.")
        print()
        exit(-1)

    try:
        request = api.api_add_entry(target_url)
        if(request.hasError()):
            print("Error: {0} - {1}".format(request.error_text,
                                            request.error_description))
            exit(-1)
        else:
            print("Entry successfully added")
            exit(0)
    except api.OAuthException as e:
        print("Error: {0}".format(e.text))
        print()
        exit(-1)
