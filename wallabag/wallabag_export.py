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
    filemode = 't'

    x = outputfile.split(".")
    if len(x) > 1:
        ext = x[len(x)-1].lower()
        if ext == 'txt':
            form = 'txt'
            filemode = 't'
        elif ext == 'csv':
            form = 'csv'
            filemode = 't'
        elif ext == 'xml':
            form = 'xml'
            filemode = 't'
        elif ext == 'json':
            form = 'json'
            filemode = 't'
        elif ext == 'pdf':
            form = 'pdf'
            filemode = 'b'
        elif ext == 'epub':
            form = 'epub'
            filemode = 't'
        elif ext == 'mobi':
            form = 'mobi'
            filemode = 't'
        elif ext == 'azw':
            form = 'mobi'
            filemode = 't'

    try:
        request = api.api_export_entry(entry_id, form)
        __handle_request_error(request)
        # output = entry.Entry(json.loads(request.response))
        output = request.response
    except api.OAuthException as ex:
        print("Error: {0}".format(ex.text))
        print()
        exit(-1)

    filehandler = open(outputfile, 'w')
    filehandler.write(output)
    filehandler.close()

def __handle_request_error(request):
    if request.has_error():
        if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
            print("Error: Invalid entry id.")
            print()
            exit(-1)
        print("Error: {0} - {1}".format(request.error_text,
                                        request.error_description))
        exit(-1)
