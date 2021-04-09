#!/usr/bin/python3
''' this function send request to a URL and display the values
of x-request-id variable found in the header'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    """My status"""
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        r = response.headers
        print(r['X-Request-Id'])
