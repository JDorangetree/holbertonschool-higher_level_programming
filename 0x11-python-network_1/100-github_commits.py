#!/usr/bin/python3
"""script that takes your Github credentials (username and password)"""

import requests
from sys import argv

if __name__ == "__main__":

    repo_name = argv[2]
    owner_name = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'
    r = requests.get(url.format(owner_name, repo_name))
    dic = r.json()
    j = 0
    for i in dic:
        if (j < 10):
            authors = i.get('commit')
            tree = authors.get('tree')
            sha = tree.get('sha')
            author = authors.get('author')
            name = author.get('name')
            j = j + 1
            print("{}: {}".format(sha, name))
