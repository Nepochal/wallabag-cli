import json

from wallabag import conf
from wallabag import api

from . import context


conf.load()

response = api.api_token()

print("HTTP Status: " + str(response.http_code))
print("Error: " + str(response.error))
print("Errortext: " + response.error_text)
print("Errordescription: " + response.error_description)
print("Body: " + str(response.response))

if response.error == api.Error.ok:
    print()
    value = json.loads(response.response)
    print("Access-token:" + value['access_token'])
    print("Validity:" + str(value['expires_in']) + "seconds")
