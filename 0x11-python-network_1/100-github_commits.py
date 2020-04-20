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
    dic = r.json()
    for i in dic[:10]:
        sha = i.get('sha')
        commit = i.get('commit')
        if commit:
            author = commit.get('author')
        if author:
            name = author.get('name')
        print("{}: {}".format(sha, name))
