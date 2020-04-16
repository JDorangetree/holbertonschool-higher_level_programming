#!/usr/bin/python3
"""request to the URL and displays the value of the X-Request-Id"""

from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        html = response.info()
    for i in html._headers:
        if i[0] == "X-Request-Id":
            tag = i[1]
    print(tag)
