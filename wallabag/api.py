"""
Wallabag API accesses.
"""
from enum import Enum
import re
import requests
from conf import Configs
import conf


MINIMUM_API_VERSION = 2, 1, 1


class Error(Enum):
    undefined = -1
    ok = 0
    dns_error = 1
    http_not_found = 10
    http_forbidden = 11


class ApiMethod(Enum):
    token = "/oauth/v2/token"
    version = "/api/version"


class Response:
    http_code = 0
    error = Error.undefined
    error_text = ""
    error_description = ""

    response = ""

    def __init__(self, status_code, http_response):
        self.http_code = status_code
        self.response = http_response

        # DNS/HTTP cases:
        # DNS not found
        if self.http_code == 0:
            self.error = Error.dns_error
            self.error_text = "Name or service not known."
        # 404 not found
        elif self.http_code == 404:
            self.error = Error.http_not_found
            self.error_text = "API was not found."
        # 403 forbidden
        elif self.http_code == 403:
            self.error = Error.http_forbidden
            self.error_text = "Could not reach API due to rights issues."
        # 200 okay
        elif self.http_code == 200:
            self.error = Error.ok

    def is_rersponse_status_ok(self):
        return self.http_code == 200

    def hasError(self):
        return self.error != Error.ok


def __getApiUrl(api_method):
    if api_method in ApiMethod:
        return Configs.serverurl + api_method.value
    return None


def __requestGet(url, data=None):
    ret = None
    request = None

    try:
        if data == None:
            request = requests.get(url)
        else:
            request = requests.get(url, data)
        ret = Response(request.status_code, request.text)
    # dns error
    except requests.exceptions.ConnectionError:
        ret = Response(0, None)
    return ret


def is_minimum_version(version_response):
    versionstring = version_response.response

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
    response = __requestGet(url)
    return response
