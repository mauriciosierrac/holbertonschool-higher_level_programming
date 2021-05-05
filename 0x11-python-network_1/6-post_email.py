#!/usr/bin/python3
'''the script takes in a url and mail address send a post'''

import requests
from sys import argv

if __name__ == '__main__':
    '''POST request'''

    url = argv[1]
    mail = {"email": argv[2]}

    req = requests.post(url, mail)
    print(req.text)
