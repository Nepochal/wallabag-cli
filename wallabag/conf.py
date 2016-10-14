"""
Settings and configuration for wallabag-api.
"""
import json
from collections import OrderedDict

CONFIG_FILENAME = ".wallabag-cli"


class Configs():
    """
    Static struct for storing the global configs.
    """

    serverurl = ""
    username = ""
    password = ""
    oa2client = ""
    oa2secret = ""


def __configs2dictionary():
    """
    Converts the configuration values to a json serializable dictionary.

    Returns
    -------
    bool
    Dictionary with the configurations
    """

    wallabag_api = OrderedDict()
    wallabag_api_oauth2 = OrderedDict()

    wallabag_api['serverurl'] = Configs.serverurl
    wallabag_api['username'] = Configs.username
    wallabag_api['password'] = Configs.password
    wallabag_api_oauth2['client'] = Configs.oa2client
    wallabag_api_oauth2['secret'] = Configs.oa2secret
    wallabag_api["oauth2"] = wallabag_api_oauth2

    return {"wallabag_api": wallabag_api}


def save(path=CONFIG_FILENAME):
    file = open(path, mode='w')

    jsonsave = json.dumps(__configs2dictionary(), indent=4)
    file.write(jsonsave)

    file.close()
