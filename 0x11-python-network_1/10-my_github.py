#!/usr/bin/python3
"""script that takes your Github credentials (username and password)"""

import requests
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    token = argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    dic = r.json()
    print(dic.get('id'))
