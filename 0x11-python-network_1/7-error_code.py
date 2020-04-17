#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    r = requests.get(url)
    error = r.status_code
    if (error >= 400):
        print("Error code: {}".format(error))
    else:
        print(r.text)
