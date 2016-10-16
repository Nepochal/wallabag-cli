"""
Wallabag API accesses.
"""
from enum import Enum
import re
import requests
import conf


MINIMUM_API_VERSION = 2, 1, 1


class Error(Enum):
    undefined = -1
    ok = 0


class ApiMethod(Enum):
    version = "/api/version"


class Response:
    http_code = 0
    error = Error.undefined
    response = ""

    def __init__(self, api_response):
        self.http_code, self.error, self.response = api_response


def __getApiUrl(api_method):
    if api_method in ApiMethod:
        return conf.get_config('serverurl') + api_method.value
    return None


def is_minimum_version(versionstring):
    if not re.compile('"\\d+\\.\\d+\\.\\d+"').match(versionstring):
        return False

    ver = versionstring.strip('"').split('.')

    x = int(ver[0])
    y = int(ver[1])
    z = int(ver[2])
    tx, ty, tz = MINIMUM_API_VERSION

    if x > tx:
        return True
    elif x < tx:
        return False
    else:
        if y > ty:
            return True
        elif y < ty:
            return False
        else:
            if z >= tz:
                return True
            else:
                return False


def version():
    url = __getApiUrl(ApiMethod.version)
    response = requests.get(url)

    return response.status_code, Error.ok, response.text
