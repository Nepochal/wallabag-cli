import json

from wallabag import conf
from wallabag import api

from . import context


NEW_ENTRY = "https://en.wikipedia.org/wiki/Bill_%26_Ted%27s_Excellent_Adventure"
CUSTOM_TITLE = "Bogus!"

conf.load()

response = api.api_add_entry(NEW_ENTRY)

print("HTTP Status: " + str(response.http_code))
print("Error: " + str(response.error))
print("Errortext: " + response.error_text)
print("Errordescription: " + response.error_description)
print("Body: " + str(response.response))
