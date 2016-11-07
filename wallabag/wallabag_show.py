"""
Show a wallabag entry
"""
import json
from bs4 import BeautifulSoup
import api
import conf
import entry

def show(entry_id):
    """
    Main function for showing an entry.
    """
    conf.load()
    try:
        request = api.api_get_entry(entry_id)
        __handle_request_error(request)
        entr = entry.Entry(json.loads(request.response))
    except api.OAuthException as ex:
        print("Error: {0}".format(ex.text))
        print()
        exit(-1)

    output = html2text(entr.content)
    print(output)


def html2text(html):
    soup = BeautifulSoup(html, "html.parser")

    return soup.text


def __handle_request_error(request):
    if request.has_error():
        if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
            print("Error: Invalid entry id.")
            print()
            exit(-1)
        print("Error: {0} - {1}".format(request.error_text,
                                        request.error_description))
        exit(-1)

show(602)
