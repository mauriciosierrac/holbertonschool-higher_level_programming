#!/usr/bin/python3
'''Write a Python script that takes in a URL'''

from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    ''' send POST '''
    url = argv[1]
    arg = {"email": argv[2]}
    mail = urllib.parse.urlencode(arg).encode('ascii')

    req = urllib.request.Request(url, mail)
    with urllib.request.urlopen(req) as response:
        r = response.read().decode('utf-8')
        print(r)
