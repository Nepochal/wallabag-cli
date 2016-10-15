"""
Wallabag API accesses.
"""
from enum import Enum
import requests
import conf


class Error(Enum):
    undefined = -1
    ok = 0


class ApiMethod(Enum):
    version = "/api/version"


def __getApiUrl(api_method):
    if api_method in ApiMethod:
        return conf.get_config('serverurl') + api_method.value
    return None


def version():
    url = __getApiUrl(ApiMethod.version)
    response = requests.get(url)

    return response.status_code, Error.ok, response.text
