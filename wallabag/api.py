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


def version():
    url = __getApiUrl(ApiMethod.version)
    response = requests.get(url)

    return response.status_code, Error.ok, response.text
