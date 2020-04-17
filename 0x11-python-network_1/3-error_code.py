#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    try:
        with urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))

    except HTTPError as e:
        print("Error code: {}".format(e.code))
