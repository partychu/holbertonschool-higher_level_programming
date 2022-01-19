#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to <URL> with the letter as a parameter
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    dataq = {'q': q}

    r = requests.post(url, data=dataq)

    try:
        r_json = r.json()
        id_ = r_json.get('id')
        name = r_json.get('name')

        if id_ and name:
            # If properly JSON formatted
            print("[{}] {}".format(id_, name))
        else:
            # If empty
            print("No result")
    except Exception:
        # If invalid
        print("Not a valid JSON")
