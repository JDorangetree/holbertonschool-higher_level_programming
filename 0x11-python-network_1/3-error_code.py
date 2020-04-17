#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            res = response.read()
            print(res.decode('utf-8'))

    except HTTPError as e:
        print("Error code: {}".format(e.code))
