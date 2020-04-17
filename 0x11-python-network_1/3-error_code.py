#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

from urllib.request import urlopen
from urllib import error
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
