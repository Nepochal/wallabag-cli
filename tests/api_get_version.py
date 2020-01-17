from wallabag import conf
from wallabag import api

from . import context


conf.load()

response = api.api_version()

print("HTTP Status: " + str(response.http_code))
print("Error: " + str(response.error))
print("Errortext: " + response.error_text)
print("Body: " + str(response.response))

if response.is_rersponse_status_ok():
    if api.is_minimum_version(response):
        print("Wallabag API is compatible.")
    else:
        print("Unsupported wallabag API.")
