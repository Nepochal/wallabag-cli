"""
Wallabag API accesses.
"""
from enum import Enum
import json
import re
import requests
import time
import conf
from conf import Configs


MINIMUM_API_VERSION = 2, 1, 1
MINIMUM_API_VERSION_HR = "2.1.1"


class OAuthException(Exception):
    pass


class Error(Enum):
    undefined = -1
    ok = 0
    dns_error = 1
    http_bad_request = 400
    http_unauthorized = 401
    http_forbidden = 403
    http_not_found = 404
    unknown_error = 999


class ApiMethod(Enum):
    add_entry = "/api/entries"
    delete_entry = "/api/entries/{0}"
    entry_exists = "/api/entries/exists"
    list_entries = "/api/entries"
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
        # 401 unauthorized
        elif self.http_code == 401:
            self.error = Error.http_unauthorized
            errors = json.loads(self.response)
            if 'error' in errors:
                self.error_text = errors['error']
            if 'error_description' in errors:
                self.error_description = errors['error_description']
        # 403 forbidden
        elif self.http_code == 403:
            self.error = Error.http_forbidden
            self.error_text = "403: Could not reach API due to rights issues."
        # 404 not found
        elif self.http_code == 404:
            self.error = Error.http_not_found
            self.error_text = "404: API was not found."
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


def __get_api_url(api_method, different_url=None):
    if api_method in ApiMethod:
        if different_url != None:
            return different_url + api_method.value
        return Configs.serverurl + api_method.value
    return None


def __get_authorization_header():
    success, token_or_error = get_token()
    if not success:
        e = OAuthException
        e.text = token_or_error
        raise e
    else:
        return {'Authorization': "Bearer {0}".format(token_or_error)}


def __request_delete(url, headers=None):
    ret = None
    request = None

    try:
        request = requests.delete(url, headers=headers)
        ret = Response(request.status_code, request.text)
    # dns error
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
        ret = Response(0, None)
    return ret


def __request_get(url, headers=None, params=None):
    ret = None
    request = None

    try:
        request = requests.get(url, headers=headers, params=params)
        ret = Response(request.status_code, request.text)
    # dns error
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
        ret = Response(0, None)
    return ret


def __request_post(url, headers=None, data=None):
    ret = None
    request = None

    try:
        request = requests.post(url, data=data, headers=headers)
        ret = Response(request.status_code, request.text)
    # dns error
    except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
        ret = Response(0, None)
    return ret


def is_valid_url(url):
    response = __request_get(url)
    return not response.hasError()


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
            return z >= tz


def api_version(different_url=None):
    url = __get_api_url(ApiMethod.version, different_url)
    response = __request_get(url)
    return response


def api_token():
    url = __get_api_url(ApiMethod.token)
    data = dict()
    data['grant_type'] = "password"
    data['client_id'] = Configs.client
    data['client_secret'] = Configs.secret
    data['username'] = Configs.username
    data['password'] = Configs.password

    response = __request_get(url, params=data)
    return response


def api_add_entry(targeturl, title=None, star=False, read=False):
    url = __get_api_url(ApiMethod.add_entry)
    header = __get_authorization_header()
    data = dict()
    data['url'] = targeturl
    if title != None:
        data['title'] = title
    if star:
        data['starred'] = 1
    if read:
        data['archive'] = 1
    response = __request_post(url, header, data)
    return response


def api_delete_entry(entry_id, force=False):
    url = __get_api_url(ApiMethod.delete_entry).format(entry_id)
    header = __get_authorization_header()


def api_entry_exists(url):
    apiurl = __get_api_url(ApiMethod.entry_exists)
    header = __get_authorization_header()
    data = dict()
    data['url'] = url
    response = __request_get(apiurl, headers=header, params=data)
    return response


def api_list_entries(count, filter_read=None, filter_starred=None, oldest=False):
    url = __get_api_url(ApiMethod.list_entries)
    header = __get_authorization_header()
    params = dict()

    params['perPage'] = count

    if oldest:
        params['order'] = "asc"

    if filter_read != None:
        if filter_read:
            params['archive'] = 1
        else:
            params['archive'] = 0

    if filter_starred != None:
        if filter_starred:
            params['starred'] = 1
        else:
            params['starred'] = 0

    response = __request_get(url, headers=header, params=params)
    return response


def get_token(force_creation=False):
    """
    Returns a valid oauth token. Creates a new one if the old token is expired.

    Parameters:
    -----------
    force_creation [optional]bool
        Enforces the creation even if the old token is valid.

    Returns:
    --------
    bool
        Getting the token was successful.
    string
        A valid token or an error message.
    """
    if conf.is_token_expired() or force_creation:
        response = api_token()
        if not response.hasError():
            content = json.loads(response.response)
            Configs.access_token = content['access_token']
            Configs.expires = time.time() + content['expires_in']
            conf.save()
            return True, Configs.access_token
        else:
            if response.error_description == "":
                return False, response.error_text
            else:
                return False, "{0} - {1}".format(response.error_text, response.error_description)
    else:
        return True, Configs.access_token
