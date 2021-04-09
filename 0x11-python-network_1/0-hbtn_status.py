#!/usr/bin/python3
'''This function fetches type, content and decode from a url'''

import urllib.request

if __name__ == "__main__":
    """My status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
