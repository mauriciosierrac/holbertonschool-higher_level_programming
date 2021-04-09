#!/usr/bin/python3
'''Write a Python script that takes in a URL'''

from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    '''send a request to the URL and displayst the body of the response'''

    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            r = response.read().decode('ascii')
            print(r)
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)
