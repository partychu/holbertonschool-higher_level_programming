#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password)and uses the
GitHub API to display your id.
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    un = argv[1]
    pw = argv[2]

    r = requests.get(url, auth=(un, pw))
    r_json = r.json()
    print(r_json.get('id'))
