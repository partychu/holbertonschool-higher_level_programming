#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.request

if __name__ == "__main__":

    url = argv[1]
    email = {'email': argv[2]}

    e_email = urllib.parse.urlencode(email)
    e_email = e_email.encode('utf-8')
    with urllib.request.urlopen(url, e_email) as r:
        print(r.read().decode('utf-8'))
