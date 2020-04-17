#!/usr/bin/python3
""" Whats my status with requests """

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    r = requests.get(url)
    header = r.headers
    print(header.get("X-Request-Id"))
