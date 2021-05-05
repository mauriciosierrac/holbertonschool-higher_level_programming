#!/usr/bin/python3
'''Write a Python script that takes in a URL'''

from sys import argv
import requests

if __name__ == "__main__":
    '''send a request to the URL and displayst the body of the response'''

    url = argv[1]
    req = requests.get(url)

    if req.status_code == 200:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))
