"""
Export a wallabag entry
"""
import io
import formatter
import json
import os
from sys import exit
import sys
import api
import conf
import entry


def export_entry(entry_id, outputfile=''):
    """
    Main function for exporting an entry.
    """
    conf.load()

    if outputfile == '':
        outputfile = 'wallabag_' + entry_id + '.txt'

    form = 'txt'

    x = outputfile.split(".")
    if len(x) > 1:
        ext = x[len(x)-1].lower()
        if ext == 'txt':
            form = 'txt'
        elif ext == 'csv':
            form = 'csv'
        elif ext == 'xml':
            form = 'xml'
        elif ext == 'json':
            form = 'json'
        elif ext == 'pdf':
            form = 'pdf'
        elif ext == 'epub':
            form = 'epub'
        elif ext == 'mobi':
            form = 'mobi'
        elif ext == 'azw':
            form = 'mobi'

    try:
        request = api.api_export_entry(entry_id, form)
        __handle_request_error(request)
        # output = entry.Entry(json.loads(request.response))
        output = request.response
    except api.OAuthException as ex:
        print("Error: {0}".format(ex.text))
        print()
        exit(-1)

    print(output)


def __handle_request_error(request):
    if request.has_error():
        if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
            print("Error: Invalid entry id.")
            print()
            exit(-1)
        print("Error: {0} - {1}".format(request.error_text,
                                        request.error_description))
        exit(-1)
