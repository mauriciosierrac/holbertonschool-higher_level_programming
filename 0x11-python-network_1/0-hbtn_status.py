#!/usr/bin/python3
'''This function fetches type, content and decode from a url'''

import urllib.request


with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
    content = response.read()


print('Body response:')
print('\t-type: {}'.format(type(content)))
print('\t-content: {}'.format(content))
print('\t-utf8 content: {}'.format(content.decode('utf-8')))
