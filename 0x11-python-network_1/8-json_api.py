#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    data = {'q': letter}
    r = requests.post(url, data)
    try:
        dic = r.json()
        if dic:
            id = dic["id"]
            name = dic["name"]
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
