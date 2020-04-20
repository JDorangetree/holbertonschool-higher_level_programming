#!/usr/bin/python3
"""script that takes your Github credentials (username and password)"""

import requests
from sys import argv

if __name__ == "__main__":

    repo_name = argv[1]
    owner_name = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'
    r = requests.get(url.format(owner_name, repo_name))
    j = 0
    try:
        dic = r.json()
        for i in dic:
            if (j < 10):
                name = i.get('commit').get('author').get('name')
                sha = i.get('commit').get('tree').get('sha')
                j = j + 1
                print("{}: {}".format(sha, name))
    except ValueError:
        print("None")