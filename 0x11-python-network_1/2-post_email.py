#!/usr/bin/python3
import urllib.request
import sys

"""
sends a POST request to the passed
    URL with the email as a parameter
"""

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as respond:
        print(response.read().decode('utf-8'))
