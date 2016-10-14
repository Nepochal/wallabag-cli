"""
Interactive configuration tool for wallabag-cli.
"""
import conf


def start(ask_serverurl=True, ask_username=True, ask_password=True, ask_oauth2=True):
    conf.load()
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


def __serverurl(forced):
    print("Enter the url of your Wallabag instance.")
    print("e.g. https://www.wallabag.com")
    if not forced:
        print("(Leave the text empty to leave the url unchanged.)")
    value = input()
    return value


def __username(forced):
    print("Enter your Wallabag username.")
    if not forced:
        print("(Leave the text empty to leave the username unchanged.)")
    value = input()
    return value


def __password(forced):
    print("Enter your Wallabag password.")
    if not forced:
        print("(Leave the text empty to leave the password unchanged.)")
    value = input()
    return value


def __client(forced):
    print("Enter the client id of your Wallabag API.")
    if not forced:
        print("(Leave the text empty to not change the client id.)")
    value = input()
    return value


def __secret(forced):
    print("Enter the client secret of your Wallabag API.")
    if not forced:
        print("(Leave the text empty to not change the client secret.)")
    value = input()
    return value
