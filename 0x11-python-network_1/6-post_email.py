#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]
    email = {'email': argv[2]}

    r = requests.post(url, data=email)
    print(r.text)
