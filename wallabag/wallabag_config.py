"""
Interactive configuration tool for wallabag-cli.
"""
import conf


def start(ask_serverurl=True, ask_username=True, ask_password=True, ask_oauth2=True):
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

    if(serverurl != ""):
        conf.set_config('serverurl', serverurl)
    if(username != ""):
        conf.set_config('username', username)
    if(password != ""):
        conf.set_config('password', password)
    if(client != ""):
        conf.set_config('client', client)
    if(secret != ""):
        conf.set_config('secret', secret)

    print()
    if conf.save():
        print("The config was saved successfully.")
        exit(0)
    else:
        print("An error occured while saving the configuration. Please try again.")
        exit(-1)


def __serverurl(forced):
    error = False
    print()
    print("Enter the url of your Wallabag instance.")
    print("e.g. https://www.wallabag.com")
    if not forced:
        print("(Leave the text empty to leave the url unchanged.)")
    value = input()

    if forced and value == "":
        error = True

    if error:
        return __serverurl(forced)
    return value


def __username(forced):
    error = False
    print()
    print("Enter your Wallabag username.")
    if not forced:
        print("(Leave the text empty to leave the username unchanged.)")
    value = input()

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

    if forced and value == "":
        error = True

    if error:
        return __secret(forced)

    return value
