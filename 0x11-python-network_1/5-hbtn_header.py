#!/usr/bin/python3
'''send request'''

import requests
from sys import argv

if __name__ == '__main__':
    '''response haeader'''

    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
