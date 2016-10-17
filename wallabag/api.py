"""
Wallabag API accesses.
"""
from enum import Enum
import re
import requests
import json
from conf import Configs


MINIMUM_API_VERSION = 2, 1, 1


class Error(Enum):
    undefined = -1
    ok = 0
    dns_error = 1
    http_not_found = 404
    http_forbidden = 403
    http_bad_request = 400
    unknown_error = 999


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

        # DNS not found
        if self.http_code == 0:
            self.error = Error.dns_error
            self.error_text = "Name or service not known."
        # 400 bad request
        elif self.http_code == 400:
            self.error = Error.http_bad_request
            errors = json.loads(self.response)
            if 'error' in errors:
                self.error_text = errors['error']
            if 'error_description' in errors:
                self.error_description = errors['error_description']
        # 404 not found
        elif self.http_code == 404:
            self.error = Error.http_not_found
            self.error_text = "404: API was not found."
        # 403 forbidden
        elif self.http_code == 403:
            self.error = Error.http_forbidden
            self.error_text = "403: Could not reach API due to rights issues."
        # 200 okay
        elif self.http_code == 200:
            self.error = Error.ok
        # unknown Error
        else:
            self.error = Error.unknown_error
            self.error_text = "An unknown error occured."

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


def token():
    url = __getApiUrl(ApiMethod.token)
    data = "grant_type=password"
    data = "{0}&client_id={1}".format(data, Configs.client)
    data = "{0}&client_secret={1}".format(data, Configs.secret)
    data = "{0}&username={1}".format(data, Configs.username)
    data = "{0}&password={1}".format(data, Configs.password)

    response = __requestGet(url, data)
    return response
