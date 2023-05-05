#!/usr/bin/python3
import urllib.request
import sys


"""displays the value of the X-Request-Id 
variable found in the header of the response.
"""
try:
    with urllib.request.urlopen(sys.argv[1]) as header_requist:
        print(header_requist.headers['X-Request-Id'])
except IndexError:
    pass
