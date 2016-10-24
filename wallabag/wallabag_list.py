"""
List existing entries
"""
import api
import conf
#import json
import json
from sys import exit


def list_entries():
    conf.load()

    try:
        request = api.api_list_entries()
        if(request.hasError()):
            print("Error: {0} - {1}".format(request.error_text,
                                            request.error_description))
            exit(-1)
        response = json.loads(request.response)
    except api.OAuthException as e:
        print("Error: {0}".format(e.text))
        print()
        exit(-1)

    for item in response['_embedded']["items"]:
        print(item["title"].replace("\n", ""))


list_entries()
