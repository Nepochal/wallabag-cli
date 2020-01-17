"""
Interactive configuration tool for wallabag-cli.
"""
import re
from sys import exit

from . import api
from . import conf


def start(ask_serverurl=True, ask_username=True, ask_password=True, ask_oauth2=True):
    """
    Interactive configuration.
    """
    conf.load_or_create()

    serverurl = conf.get_config('serverurl')
    username = conf.get_config('username')
    password = conf.get_config('password')
    client = conf.get_config('client')
    secret = conf.get_config('secret')

    if ask_serverurl or serverurl == "":
        serverurl = __serverurl(serverurl == "")
    if ask_username or username == "":
        username = __username(username == "")
    if ask_password or password == "":
        password = __password(password == "")
    if ask_oauth2 or client == "" or secret == "":
        client = __client(client == "")
        secret = __secret(secret == "")

    if serverurl != "":
        conf.set_config('serverurl', serverurl)
    if username != "":
        conf.set_config('username', username)
    if password != "":
        conf.set_config('password', password)
    if client != "":
        conf.set_config('client', client)
    if secret != "":
        conf.set_config('secret', secret)

    # username/password and client/secret check
    testresponse = api.api_token()
    if testresponse.has_error():
        conf.save()
        if testresponse.error == api.Error.http_bad_request:
            print(testresponse.error_description)
            if testresponse.error_text == "invalid_grant":
                start(ask_serverurl=False, ask_oauth2=False)
                return
            elif testresponse.error_text == "invalid_client":
                start(ask_serverurl=False, ask_username=False, ask_password=False)
                return
        print("An unknown error occured on the server side. Please try again later.")
        print()
        exit(-1)

    print()
    if conf.save():
        print("The config was saved successfully.")
    else:
        print("An error occured while saving the configuration. Please try again.")
        print()
        exit(-1)


def check():
    """
    Checks if the config is suitable.
    """
    if not conf.is_valid():
        print("The config is missing or incomplete.")
        return False

    conf.load()

    response = api.api_version()
    if response.has_error():
        print("The server or the API is not reachable.")
        return False

    if not api.is_minimum_version(response):
        print("The version of the wallabag instance is too old.")
        return False

    response = api.api_token()
    if response.has_error():
        print(response.error_description)
        return False

    print("The config is suitable.")
    return True


def __serverurl(forced):
    print()
    print("Enter the url of your Wallabag instance.")
    print("e.g. https://www.wallabag.com")
    if not forced:
        print("(Leave the text empty to leave the url unchanged.)")
    value = input()

    # trim leading and following spaces
    value = value.strip()

    if value == "":
        if forced:
            return __serverurl(forced)
        else:
            return value

    # remove following slash
    if value[len(value) - 1] == '/':
        value = value[0:len(value) - 1]

    # add http:// if there is no http:// or https://
    if not re.compile("(?i)https?:\\/\\/.+").match(value):
        value = "http://" + value

    # dns and http status check
    testresponse = api.api_version(value)
    if testresponse.has_error():
        print(testresponse.error_text)
        return __serverurl(forced)

    # minimum api check
    if not api.is_minimum_version(testresponse):
        print("Your wallabag instance is too old. You need at least version {0}.".format(
            api.MINIMUM_API_VERSION_HR))
        exit(-1)

    return value


def __username(forced):
    error = False
    print()
    print("Enter your Wallabag username.")
    if not forced:
        print("(Leave the text empty to leave the username unchanged.)")
    value = input()

    # trim leading and following spaces
    value = value.strip()

    if forced and value == "":
        error = True

    if error:
        return __username(forced)

    return value


def __password(forced):
    error = False
    print()
    print("Enter your Wallabag password.")
    if not forced:
        print("(Leave the text empty to leave the password unchanged.)")
    value = input()

    if forced and value == "":
        error = True

    if error:
        return __password(forced)

    return value


def __client(forced):
    error = False
    print()
    print("Enter the client id of your Wallabag API.")
    if not forced:
        print("(Leave the text empty to not change the client id.)")
    value = input()

    # trim leading and following spaces
    value = value.strip()

    if forced and value == "":
        error = True

    if error:
        return __client(forced)

    return value


def __secret(forced):
    error = False
    print()
    print("Enter the client secret of your Wallabag API.")
    if not forced:
        print("(Leave the text empty to not change the client secret.)")
    value = input()

    # trim leading and following spaces
    value = value.strip()

    if forced and value == "":
        error = True

    if error:
        return __secret(forced)

    return value
