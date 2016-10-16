import context
import conf
import api

conf.load()

response = api.version()

print("HTTP Status: " + str(response.http_code))
print("Error: " + str(response.error))
print("Errortext: " + response.error_text)
print("Body: " + str(response.response))

if response.is_rersponse_status_ok():
    if api.is_minimum_version(response):
        print("Wallabag API is compatible.")
    else:
        print("Unsupported wallabag API.")
