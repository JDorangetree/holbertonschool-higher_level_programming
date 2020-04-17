#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0."
    data = {'q': argv[1]}
    try:
        r = requests.post(url, data)
        dic = r._content.decode('utf-8')
        try:
            id = eval(dic)["id"]
            name = eval(dic)["name"]
            print("[{}] {}".format(id, name))
        except:
            print("No result")
    except:
        print("Not a valid JSON")
