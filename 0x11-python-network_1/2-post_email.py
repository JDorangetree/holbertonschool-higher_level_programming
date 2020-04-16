#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urlencode(values)
    data = data.encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        mail = response.read()
    print(mail.decode('utf-8'))
