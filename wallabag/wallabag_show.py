"""
Show a wallabag entry
"""
import formatter
import json
import os
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

    for line in output.splitlines():
        __print_formatted(line)
        print()


def html2text(html):
    soup = BeautifulSoup(html, "html.parser")

    # Color h1-h3
    h1colors = '\033[93m'
    h1colore = '\033[0m'
    for h1 in soup.findAll('h1'):
        h1.string = "{0}{1}{2}\n".format(h1colors, h1.string, h1colore)
    for h2 in soup.findAll('h2'):
        h2.string = "{0}{1}{2}\n".format(h1colors, h2.string, h1colore)
    for h3 in soup.findAll('h3'):
        h3.string = "{0}{1}{2}\n".format(h1colors, h3.string, h1colore)

    # Replace hr with visual lines
    hrstring = "".ljust(os.get_terminal_size().columns, '-')
    for hr in soup.findAll('hr'):
        replace = soup.new_tag('p')
        replace.string = hrstring
        hr.insert_after(replace)
        hr.unwrap()

    # Replace images by information-texts
    for img in soup.findAll('img'):
        replace = soup.new_tag('p')
        try:
            alt = " \"{0}\"".format(img['alt'])
        except KeyError:
            alt = ""
        replace.string = "[IMAGE{0}]\n".format(alt)
        img.insert_after(replace)
        img.unwrap()

    return soup.text


def __print_formatted(text):
    maxcol = os.get_terminal_size().columns

    writer = formatter.DumbWriter(maxcol=maxcol)
    writer.send_flowing_data(text)


def __handle_request_error(request):
    if request.has_error():
        if request.error == api.Error.http_forbidden or request.error == api.Error.http_not_found:
            print("Error: Invalid entry id.")
            print()
            exit(-1)
        print("Error: {0} - {1}".format(request.error_text,
                                        request.error_description))
        exit(-1)
